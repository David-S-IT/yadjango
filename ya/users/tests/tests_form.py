from datetime import datetime
from unittest.mock import patch

import pytz
from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse
from django.utils import timezone

from ..forms import CustomUserCreationForm

User = get_user_model()


class FormTests(TestCase):
    @classmethod
    def setUp(self):
        super().setUpClass()
        self.form = CustomUserCreationForm()

    def tearDown(self):
        super().tearDown()
        User.objects.all().delete()

    @staticmethod
    def func_create_user():
        form_data = {
            User.username.field.name: 'test',
            User.email.field.name: 'default@ya.ru',
            'password1': 'login_pass',
            'password2': 'login_pass',
        }
        Client().post(reverse('users:sign_up'), data=form_data, follow=True)
        return form_data

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
            User.username.field.name: 'Обязательное поле. Не более 150 символов. Только буквы, цифры и символы @/./+/-/_.',
            User.email.field.name: 'На этот адрес будет отправлено письмо с подтверждением',
        }
        for name, field in help_texts:
            with self.subTest(name=name, field=field):
                self.assertEqual(field, help_texts_correct[name])

    def test_redirect(self):
        form_data = {
            User.username.field.name: 'test',
            User.email.field.name: 'default@ya.ru',
            'password1': 'login_pass',
            'password2': 'login_pass',
        }
        response = Client().post(
            reverse('users:sign_up'), data=form_data, follow=True
        )

        r1 = reverse('users:login')
        r2 = reverse('users:profile')
        redirect = f'{r1}?next={r2}'

        self.assertRedirects(response, redirect)

    def test_create_user(self):
        users_count = User.objects.count()

        form_data = self.func_create_user()

        self.assertEqual(
            User.objects.count(),
            users_count + 1,
            msg='Пользователь не создался.',
        )

        self.assertTrue(
            User.objects.filter(
                username=form_data[User.username.field.name],
                email=form_data[User.email.field.name],
                is_active=False,
            ).exists(),
            msg='Пользователь создался с неверными полями.',
        )

    def test_activate_user_success(self):
        for hour in range(0, 12):
            with self.subTest(hour=hour):
                form_data = self.func_create_user()

                with patch('django.utils.timezone.now') as mock_date:
                    now_hour = datetime.now().hour
                    mock_date.return_value = datetime(
                        datetime.now().year,
                        datetime.now().month,
                        datetime.now().day
                        + (1 if now_hour + hour > 23 else 0),
                        now_hour + (0 if now_hour + hour > 23 else hour),
                        tzinfo=pytz.UTC,
                    )

                    Client().get(
                        reverse(
                            'users:activate',
                            kwargs={
                                'username': form_data[User.username.field.name]
                            },
                        )
                    )

                    self.assertTrue(
                        User.objects.filter(
                            username=form_data[User.username.field.name],
                            email=form_data[User.email.field.name],
                            is_active=True,
                        ).exists()
                    )

    def test_activate_user_fail(self):
        form_data = self.func_create_user()

        with patch('django.utils.timezone.now') as mock_date:
            now_hour = datetime.now().hour
            mock_date.return_value = datetime(
                datetime.now().year,
                datetime.now().month,
                datetime.now().day + 1 if now_hour + 12 > 23 else 0,
                now_hour + 0 if now_hour + 12 > 23 else 12,
                tzinfo=pytz.UTC,
            )
            Client().get(
                reverse(
                    'users:activate',
                    kwargs={'username': form_data[User.username.field.name]},
                )
            )

            self.assertTrue(
                User.objects.filter(
                    username=form_data[User.username.field.name],
                    email=form_data[User.email.field.name],
                    is_active=False,
                ).exists()
            )
