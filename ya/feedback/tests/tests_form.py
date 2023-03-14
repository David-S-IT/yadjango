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
            ('text', self.form.fields['text'].label),
            ('email', self.form.fields['email'].label),
        }
        labels_correct = {
            'text': 'Текст сообщения',
            'email': 'Ваш контактный email',
        }
        for name, field in labels:
            with self.subTest(name=name, field=field):
                self.assertEqual(field, labels_correct[name])

    def test_form_help_text(self):
        help_texts = {
            ('text', self.form.fields['text'].help_text),
            ('email', self.form.fields['email'].help_text),
        }
        help_texts_correct = {
            'text': 'Максимальная длина 200 символов.',
            'email': 'На этот адрес будет отправлен ответ.',
        }
        for name, field in help_texts:
            with self.subTest(name=name, field=field):
                self.assertEqual(field, help_texts_correct[name])

    def test_redirect(self):
        endpoint = reverse('feedback:feedback')
        form_data = {'text': 'тест', 'email': 'default@yandex.ru'}
        responce = Client().post(
            endpoint,
            data=form_data,
        )
        self.assertRedirects(responce, endpoint)
