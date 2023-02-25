from django.test import Client, TestCase, override_settings


class StaticURLTests(TestCase):
    def test_coffee_endpoint_status(self):
        response = Client().get('/coffee/')
        self.assertEqual(
            response.status_code,
            418,
            msg=f'Статус код: {response.status_code} != 418',
        )

    @override_settings(MIDDLEWARE_CUSTOM_REVERSE_RU_TEXT=True)
    def test_coffee_on_endpoint_text(self):
        url = '/coffee/'
        for i in range(10):
            response = Client().get(url)
            response_text = response.content.decode('utf-8')
            if response_text == 'Я кинйач':
                break
        else:
            self.assertEqual(
                response_text,
                'Я кинйач',
                msg=f'Неверный текст: {response_text} != Я кинйач',
            )

    @override_settings(MIDDLEWARE_CUSTOM_REVERSE_RU_TEXT=False)
    def test_coffee_off_endpoint_text(self):
        url = '/coffee/'
        for i in range(10):
            response = Client().get(url)
            response_text = response.content.decode('utf-8')
            if response_text == 'Я чайник':
                break
        else:
            self.assertEqual(
                response_text,
                'Я чайник',
                msg=f'Неверный текст: {response_text} != Я чайник',
            )
