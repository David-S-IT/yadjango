from django.test import Client, TestCase
from django.urls import reverse

from catalog.models import Category, Item, Tag


class CatalogViewsTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name='Category',
            slug='category-slug',
            is_published=True,
            weight=100,
        )
        self.tag = Tag.objects.create(
            name='Tag',
            slug='tag-slug',
            is_published=True,
        )
        self.item = Item.objects.create(
            name='Test',
            text='роскошно',
            category=self.category,
        )
        super(CatalogViewsTests, self).setUp()

    def tearDown(self):
        Item.objects.all().delete()
        Tag.objects.all().delete()
        Category.objects.all().delete()

        super(CatalogViewsTests, self).tearDown()

    def test_catalog_have_correct_context_item_list(self):
        """
        Тест views item_list возвращает корректный словарь context
        """
        response = Client().get(reverse('catalog:items_list'))
        self.assertIn('items', response.context)

    def test_catalog_have_correct_context_item_detail(self):
        """
        Тест views item_detail возвращает корректный словарь context
        """
        response = Client().get(
            reverse('catalog:item_detail', kwargs={'pk': self.item.id})
        )
        self.assertIn('item', response.context)

    def test_response_have_correct_field_from_model(self):
        """
        Тест - менеджер моделей обращается к прописанным полям Item.
        """
        reverse_obj = (
            reverse('catalog:items_list'),
            reverse('homepage:index'),
        )
        fields_set = {'category__name', 'name', 'text'}
        for reverse_name in reverse_obj:
            with self.subTest(reverse_name=reverse_name):
                response = Client().get(reverse_name)
                fields = response.context['items'].query.deferred_loading[0]
                self.assertEqual(fields, fields_set)

    def test_response_have_no_correct_field_from_model(self):
        """
        Тест - отсутствия полей, к которым не было обращения в ответе.
        """
        reverse_obj = (
            reverse('catalog:items_list'),
            reverse('homepage:index'),
        )
        fields_set = {'is_published', 'tags', 'is_on_main'}
        for reverse_name in reverse_obj:
            with self.subTest(reverse_name=reverse_name):
                response = Client().get(reverse_name)
                fields = response.context['items'].query.deferred_loading[0]
                self.assertNotEqual(fields, fields_set)
