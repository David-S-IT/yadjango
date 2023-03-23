from django.test import Client, TestCase
from django.urls import reverse

from ..forms import FeedbackForm
from ..models import Feedback


class FormTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.form = FeedbackForm()

    def tearDown(self):
        super().tearDown()
        Feedback.objects.all().delete()

    def test_form_label(self):
        labels = {
            (
                Feedback.text.field.name,
                self.form.fields[Feedback.text.field.name].label,
            ),
            (
                Feedback.email.field.name,
                self.form.fields[Feedback.email.field.name].label,
            ),
        }
        labels_correct = {
            Feedback.text.field.name: 'Текст сообщения',
            Feedback.email.field.name: 'Ваш контактный email',
        }
        for name, field in labels:
            with self.subTest(name=name, field=field):
                self.assertEqual(field, labels_correct[name])

    def test_form_help_text(self):
        help_texts = {
            (
                Feedback.text.field.name,
                self.form.fields[Feedback.text.field.name].help_text,
            ),
            (
                Feedback.email.field.name,
                self.form.fields[Feedback.email.field.name].help_text,
            ),
        }
        help_texts_correct = {
            Feedback.text.field.name: 'Максимальная длина 200 символов',
            Feedback.email.field.name: 'На этот адрес будет отправлен ответ',
        }
        for name, field in help_texts:
            with self.subTest(name=name, field=field):
                self.assertEqual(field, help_texts_correct[name])

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
