from http import HTTPStatus

from django.test import Client, TestCase

# urls_status_item_detail = [
#     ('0/', HTTPStatus.OK),
#     ('01/', HTTPStatus.OK),
#     ('010/', HTTPStatus.OK),
#     ('1/', HTTPStatus.OK),
#     ('10/', HTTPStatus.OK),
#     ('100/', HTTPStatus.OK),
#     ('-0/', HTTPStatus.NOT_FOUND),
#     ('-1/', HTTPStatus.NOT_FOUND),
#     ('-10/', HTTPStatus.NOT_FOUND),
#     ('-100/', HTTPStatus.NOT_FOUND),
#     ('100.1/', HTTPStatus.NOT_FOUND),
#     ('1.12394/', HTTPStatus.NOT_FOUND),
#     ('10a/', HTTPStatus.NOT_FOUND),
#     ('1a0/', HTTPStatus.NOT_FOUND),
#     ('10a10/', HTTPStatus.NOT_FOUND),
#     ('a10/', HTTPStatus.NOT_FOUND),
#     ('a10a/', HTTPStatus.NOT_FOUND),
#     ('1$/', HTTPStatus.NOT_FOUND),
#     ('1%/', HTTPStatus.NOT_FOUND),
#     ('1^/', HTTPStatus.NOT_FOUND),
# ]

urls_status_item_detail_positive_integer = [
    ('1/', HTTPStatus.OK),
    ('10/', HTTPStatus.OK),
    ('100/', HTTPStatus.OK),
    ('0/', HTTPStatus.NOT_FOUND),
    ('01/', HTTPStatus.NOT_FOUND),
    ('010/', HTTPStatus.NOT_FOUND),
    ('-0/', HTTPStatus.NOT_FOUND),
    ('-1/', HTTPStatus.NOT_FOUND),
    ('-10/', HTTPStatus.NOT_FOUND),
    ('-100/', HTTPStatus.NOT_FOUND),
    ('100.1/', HTTPStatus.NOT_FOUND),
    ('1.12394/', HTTPStatus.NOT_FOUND),
    ('10a/', HTTPStatus.NOT_FOUND),
    ('1a0/', HTTPStatus.NOT_FOUND),
    ('10a10/', HTTPStatus.NOT_FOUND),
    ('a10/', HTTPStatus.NOT_FOUND),
    ('a10a/', HTTPStatus.NOT_FOUND),
    ('1$/', HTTPStatus.NOT_FOUND),
    ('1%/', HTTPStatus.NOT_FOUND),
    ('1^/', HTTPStatus.NOT_FOUND),
]


class StaticURLTests(TestCase):
    def test_catalog_endpoint(self):
        response = Client().get('/catalog/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    # def test_catalog_item_detail_endpoint(self):
    #     for url, status in urls_status_item_detail:
    #         with self.subTest(url=url, status=status):
    #             response = Client().get(f'/catalog/{url}')
    #             self.assertEqual(response.status_code, status)

    def test_catalog_item_detail_positive_integer_endpoint(self):
        """
        Тестируем регулярное выражение и конвертер в ендпоинте.
        """
        for url, status in urls_status_item_detail_positive_integer:
            with self.subTest(url=url, status=status):
                client = Client()
                response1 = client.get(f'/catalog/re/{url}')
                response2 = client.get(f'/catalog/converter/{url}')
                self.assertEqual(response1.status_code, status)
                self.assertEqual(response2.status_code, status)
