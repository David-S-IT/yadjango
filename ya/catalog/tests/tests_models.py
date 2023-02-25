from django.core import exceptions
from django.test import TestCase

from ..models import Category, Item, Tag


class CatalogModelsTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name='Category_name',
            slug='category-name-slug',
            is_published=True,
            weight=100,
        )
        self.tag = Tag.objects.create(
            name='Tag_name',
            slug='tag-name-slug',
            is_published=True,
        )
        super(CatalogModelsTests, self).setUp()

    def tearDown(self):
        Item.objects.all().delete()
        Tag.objects.all().delete()
        Category.objects.all().delete()
        super(CatalogModelsTests, self).tearDown()

    def func_for_tests_validate_fields(
        self, obj, model, item_count, bool_, val=None, slug=None
    ):
        if bool_:
            self.obj.full_clean()
            self.obj.save()
            self.assertEqual(model.objects.count(), item_count + 1)
            if val:
                self.assertEqual(model.objects.get(weight=val), self.obj)
            self.assertEqual(model.objects.get(slug=slug), self.obj)
        else:
            self.assertNotEqual(model.objects.count(), item_count + 1)
            self.assertNotIn(self.obj, model.objects.all())

    def func_for_test_model_item(self, text):
        self.item = Item(
            name=f'Item{text}',
            is_published=True,
            text=text,
            category=self.category,
        )
        self.item.full_clean()
        self.item.save()
        self.item.tags.add(self.tag)

    def test_validation_is_correct_model_item_field_text_created(self):
        """
        Тестируем поле text, корректно если содержит (роскошно|превосходно).
        """
        words = ('роскошно', 'превосходно', 'Роскошно', 'Превосходно')
        item_count = Item.objects.count()
        for text in words:
            with self.subTest(text=text):
                self.func_for_test_model_item(text)
                self.assertEqual(Item.objects.count(), item_count + 1)
                item_count += 1
                self.assertEqual(Item.objects.get(text=text), self.item)

    def test_validation_is_none_correct_model_item_field_text(self):
        """
        Тестируем поле text, ошибка если не содержит (роскошно|превосходно).
        """
        item_count = Item.objects.count()
        texts = (
            'Not correct text',
            'роскошный',
            'превосходный',
            'роскошно1ыфв',
            'превосходно1фыва',
            'фывароскошно1',
            'фывапревосходно1',
            'фывароскошно',
            'фывапревосходно',
            'роскошнопревосходно',
        )
        for text in texts:
            with self.assertRaises(exceptions.ValidationError):
                text = text
                self.func_for_test_model_item(text)
        self.assertEqual(Item.objects.count(), item_count)

    def test_category_validator_value_of_weight(self):
        """
        Тестируем валидацию значения weight поля Catalog в диапазоне [1,32766].
        """
        values = (
            (1, True),
            (0, False),
            (300, True),
            (40000, False),
            (32767, False),
            (-1, False),
        )
        for val, bool_ in values:
            item_count = Category.objects.count()
            with self.subTest(value=val):
                slug = f'slug{val}'
                self.obj = Category(
                    name=f'Name: {val}',
                    is_published=True,
                    slug=slug,
                    weight=val,
                )
                self.func_for_tests_validate_fields(
                    self.obj, Category, item_count, bool_, val, slug
                )
