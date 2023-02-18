from http import  HTTPStatus

from django.core.cache import cache
from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_homepage_endpoint(self):
        url = '/'
        client = Client()
        response = client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_coffee_endpoint_status(self):
        cache.clear()
        response = Client().get('/coffee/')
        self.assertEqual(response.status_code, 418,
                         msg=f'Статус код: {response.status_code} != 418')

    def test_coffee_endpoint_text(self):
        cache.clear()
        url = '/coffee/'
        response = Client().get(url)
        for i in range(9):
            Client().get(url)
        response_text = response.content.decode('utf-8')
        self.assertEqual(response_text, 'Я чайник',
                         msg=f'Неверный текст: {response_text} != Я кинйач')
