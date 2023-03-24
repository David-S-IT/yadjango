from datetime import datetime
from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.test import Client, override_settings, TestCase
from django.urls import reverse
import pytz

from ..forms import CustomUserCreationForm

User = get_user_model()


@override_settings(IS_ACTIVE=False)
class FormTests(TestCase):
    @classmethod
    def setUp(cls):
        super().setUpClass()
        cls.form = CustomUserCreationForm()

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

    @override_settings(IS_ACTIVE=False)
    def test_create_user_is_active_false(self):
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

    @override_settings(IS_ACTIVE=True)
    def test_create_user_is_active_true(self):
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
                is_active=True,
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
                        datetime.now().minute + 1,
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
                datetime.now().day + (1 if now_hour + 12 > 23 else 0),
                now_hour + (0 if now_hour + 12 > 23 else 12),
                datetime.now().minute + 1,
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
