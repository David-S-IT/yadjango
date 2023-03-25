from django.test import TestCase

from ..forms import FeedbackForm
from ..models import Feedback


class FormTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.form = FeedbackForm()

    def tearDown(self):
        super().tearDown()

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
