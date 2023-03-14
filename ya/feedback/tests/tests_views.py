from django.test import Client, TestCase
from django.urls import reverse


class FormTests(TestCase):
    def test_context_correct(self):
        """
        Тест views feedback возвращает корректный словарь context
        """
        response = Client().get(reverse('feedback:feedback'))
        self.assertIn('form', response.context)
