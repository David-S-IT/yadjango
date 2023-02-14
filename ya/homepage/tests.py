from http import HTTPStatus

from bs4 import BeautifulSoup

from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_homepage_endpoint(self):
        response = Client().get('/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_coffee_endpoint(self):
        response = Client().get('/coffee/')
        content = BeautifulSoup(response.content, 'html.parser')
        body_content = content.find('body').get_text()

        self.assertEqual(body_content, 'Я чайник')
        self.assertEqual(response.status_code, 418)
