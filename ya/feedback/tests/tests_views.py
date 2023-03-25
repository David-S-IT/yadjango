from django.test import Client, TestCase
from django.urls import reverse

from ..forms import FeedbackForm
from ..models import Feedback


class ViewsTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.form = FeedbackForm()

    def tearDown(self):
        super().tearDown()
        Feedback.objects.all().delete()

    def test_context_correct(self):
        """
        Тест views feedback возвращает корректный словарь context
        """
        response = Client().get(reverse('feedback:feedback'))
        self.assertIn('form', response.context)

    def test_redirect(self):
        endpoint = reverse('feedback:feedback')
        form_data = {
            Feedback.text.field.name: 'тест',
            Feedback.email.field.name: 'default@yandex.ru',
        }
        response = Client().post(
            endpoint,
            data=form_data,
        )
        self.assertRedirects(response, endpoint)

    def test_create_feedback(self):
        feedbacks_count = Feedback.objects.count()

        form_data = {
            Feedback.text.field.name: 'тест',
            Feedback.email.field.name: 'default@yandex.ru',
        }
        Client().post(
            reverse('feedback:feedback'),
            data=form_data,
        )

        self.assertEqual(
            Feedback.objects.count(),
            feedbacks_count + 1,
            msg='Отзыв не создался.',
        )

        self.assertTrue(
            Feedback.objects.filter(
                text=form_data[Feedback.text.field.name],
                email=form_data[Feedback.email.field.name],
                status=Feedback.GET,
            ).exists(),
            msg='Отзыв создался с неверными полями.',
        )
