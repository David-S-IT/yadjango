from http import HTTPStatus

from django.test import Client, TestCase

QUANTITY_CATALOGS = 1_000_000

urls_status = [
    (
        '',
        '',
        HTTPStatus.OK
    ),
    (
        '0/',
        '',
        HTTPStatus.OK
    ),
    (
        '-1/',
        '-1/',
        HTTPStatus.NOT_FOUND
    ),
    (
        're/1/',
        'converter/1/',
        HTTPStatus.OK
    ),
    (
        're/100/',
        'converter/100/',
        HTTPStatus.OK
    ),
    (
        're/0/',
        'converter/0/',
        HTTPStatus.NOT_FOUND
    ),
    (
        're/-1/',
        'converter/-1/',
        HTTPStatus.NOT_FOUND
    ),
]


class StaticURLTests(TestCase):
    def test_catalog_and_re_endpoint(self):
        """
        Тестируем регулярное выражение и конвертер в ендпоинте.
        """
        for url, converter, status in urls_status:
            with self.subTest(url=url):
                client = Client()
                response1 = client.get(f'/catalog/{url}')
                response2 = client.get(f'/catalog/{converter}')
                self.assertEqual(response1.status_code, status)
                self.assertEqual(response2.status_code, status)
