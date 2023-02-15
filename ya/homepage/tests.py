from http import HTTPStatus

from bs4 import BeautifulSoup
from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_homepage_endpoint(self):
        url = '/'
        response = Client().get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_coffee_endpoint(self):
        url = '/coffee/'
        response = Client().get(url)
        content = BeautifulSoup(response.content, 'html.parser')
        body_content = content.find('body').get_text()

        self.assertEqual(body_content, 'Я чайник')
        self.assertEqual(response.status_code, 418)

    def test_middleware_text_reverse(self):
        url = '/coffee/'
        for _ in range(9):
            Client().get(url)
        response = Client().get(url)
        content = BeautifulSoup(response.content, 'html.parser')
        body_content = content.find('body').get_text()

        self.assertEqual(body_content, 'Я кинйач')
        self.assertEqual(response.status_code, 418)
