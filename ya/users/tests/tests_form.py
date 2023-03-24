from django.contrib.auth import get_user_model
from django.test import TestCase

from ..forms import CustomUserCreationForm

User = get_user_model()


class FormTests(TestCase):
    @classmethod
    def setUp(cls):
        super().setUpClass()
        cls.form = CustomUserCreationForm()

    def tearDown(self):
        super().tearDown()
        User.objects.all().delete()

    def test_form_label(self):
        labels = {
            (
                User.username.field.name,
                self.form.fields[User.username.field.name].label,
            ),
            (
                User.email.field.name,
                self.form.fields[User.email.field.name].label,
            ),
        }
        labels_correct = {
            User.username.field.name: 'Имя пользователя',
            User.email.field.name: 'Адрес электронной почты',
        }
        for name, field in labels:
            with self.subTest(name=name, field=field):
                self.assertEqual(field, labels_correct[name])

    def test_form_help_text(self):
        help_texts = {
            (
                User.username.field.name,
                self.form.fields[User.username.field.name].help_text,
            ),
            (
                User.email.field.name,
                self.form.fields[User.email.field.name].help_text,
            ),
        }
        help_texts_correct = {
            User.username.field.name: 'Обязательное поле. '
            'Не более 150 символов. '
            'Только буквы, цифры и символы '
            '@/./+/-/_.',
            User.email.field.name: 'На этот адрес будет отправлено письмо с '
            'подтверждением.',
        }
        for name, field in help_texts:
            with self.subTest(name=name, field=field):
                self.assertEqual(field, help_texts_correct[name])
