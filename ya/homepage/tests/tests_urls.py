from http import HTTPStatus

from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_homepage_endpoint(self):
        url = '/'
        client = Client()
        response = client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
