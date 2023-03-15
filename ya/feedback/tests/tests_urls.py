from http import HTTPStatus

from django.test import Client, TestCase
from django.urls import reverse


class UrlsTests(TestCase):
    def test_feedback_endpoint(self):
        response = Client().get(reverse('feedback:feedback'))
        self.assertEqual(response.status_code, HTTPStatus.OK)
