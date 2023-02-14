from http import HTTPStatus
from random import randint

from django.test import Client, TestCase

QUANTITY_CATALOGS = 1_000_000


class StaticURLTests(TestCase):
    def test_catalog_endpoint(self):
        url = '/catalog/'
        response = Client().get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_catalog_item_detail_endpoint(self):
        url = f'/catalog/{randint(0, QUANTITY_CATALOGS)}/'
        response = Client().get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_catalog_item_detail_number_negative_endpoint(self):
        url = f'/catalog/{randint(-QUANTITY_CATALOGS, -1)}/'
        response = Client().get(url)
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_catalog_re_number_one_endpoint(self):
        url = f'/catalog/re/{randint(1, 9)}/'
        response = Client().get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_catalog_re_number_any_endpoint(self):
        url = f'/catalog/re/{randint(1, QUANTITY_CATALOGS)}/'
        response = Client().get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_catalog_re_number_zero_endpoint(self):
        url = '/catalog/re/0/'
        response = Client().get(url)
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_catalog_re_number_negative_endpoint(self):
        url = f'/catalog/re/{randint(-QUANTITY_CATALOGS, -1)}/'
        response = Client().get(url)
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_catalog_converter_number_one_endpoint(self):
        url = f'/catalog/converter/{randint(1, 9)}/'
        response = Client().get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_catalog_converter_number_any_endpoint(self):
        url = f'/catalog/converter/{randint(1, QUANTITY_CATALOGS)}/'
        response = Client().get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_catalog_converter_number_zero_endpoint(self):
        url = '/catalog/converter/0/'
        response = Client().get(url)
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_catalog_converter_number_negative_endpoint(self):
        url = f'/catalog/converter/{randint(-QUANTITY_CATALOGS, -1)}/'
        response = Client().get(url)
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)
