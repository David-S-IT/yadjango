from http import HTTPStatus

# from bs4 import BeautifulSoup
from django.core.cache import cache
from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_homepage_endpoint(self):
        url = '/'
        client = Client()
        response = client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_coffee_endpoint(self):
        cache.clear()
        url = '/coffee/'
        client = Client()
        response = client.get(url)
        # content = BeautifulSoup(response.content, 'html.parser')
        # body_content = content.find('body').get_text()

        self.assertEqual(response.content.decode('utf-8'), 'Я чайник')
        self.assertEqual(response.status_code, 418)


class MiddlewareReverseTextTests(TestCase):
    def test_middleware_text_reverse(self):
        """
        Тестирую реверс в middleware текста из HttpResponse.
        """
        url = '/coffee/'
        cache.clear()
        client = Client()
        for i in range(9):
            client.get(url)

        response = client.get(url)
        body_content = response.content.decode('utf-8')
        self.assertEqual(body_content, 'Я кинйач')
        self.assertEqual(response.status_code, 418)
