from http import HTTPStatus

from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_about_endpoint(self):
        client = Client()
        response = client.get('/about/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
