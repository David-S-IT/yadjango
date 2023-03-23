from http import HTTPStatus

from django.test import Client, TestCase
from django.urls import reverse


class UrlsTests(TestCase):
    def test_sign_up_endpoint(self):
        response = Client().get(reverse('users:sign_up'))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_activate_endpoint(self):
        response = Client().get(
            reverse('users:activate', kwargs={'username': 'test'})
        )
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)
