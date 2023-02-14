from http import HTTPStatus
from random import randint

from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_client_endpoint(self):
        response = Client().get('/catalog/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_client_item_detail_endpoint(self):
        response = Client().get(f'/catalog/{randint(0, 1_000_000)}')
        self.assertEqual(response.status_code, HTTPStatus.OK)
