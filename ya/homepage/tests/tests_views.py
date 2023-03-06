from django.test import Client, TestCase
from django.urls import reverse


class HomePagesViewsTests(TestCase):
    def test_home_page_have_correct_context(self):
        """
        Тест views home возвращает корректный словарь context
        """
        response = Client().get(reverse('homepage:index'))
        self.assertIn('items', response.context)
