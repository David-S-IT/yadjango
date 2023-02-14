from http import HTTPStatus
from random import randint

from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_catalog_endpoint(self):
        response = Client().get('/catalog/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_catalog_item_detail_endpoint(self):
        response = Client().get(f'/catalog/{randint(0, 1_000_000)}/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_catalog_item_detail_number_negative_endpoint(self):
        response = Client().get(f'/catalog/{randint(-1_000_000, -1)}/')
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_catalog_re_number_one_endpoint(self):
        response = Client().get(f'/catalog/re/{randint(1, 9)}/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_catalog_re_number_any_endpoint(self):
        response = Client().get(f'/catalog/re/{randint(1, 1_000_000)}/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_catalog_re_number_zero_endpoint(self):
        response = Client().get('/catalog/re/0/')
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_catalog_re_number_negative_endpoint(self):
        response = Client().get(f'/catalog/re/{randint(-1_000_000, -1)}/')
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)
