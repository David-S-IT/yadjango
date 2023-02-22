from django.core import exceptions
from django.test import TestCase

from ..models import Category, Item, Tag


class CatalogModelsTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.category = Category.objects.create(
            name='Category_name',
            slug='category-name-slug',
            is_published=True,
            weight=100,
        )
        cls.tag = Tag.objects.create(
            name='Tag_name',
            slug='tag-name-slug',
            is_published=True,
        )

    def func_for_tests(
        self, obj, model, item_count, bool_, val=None, slug=None
    ):
        if bool_:
            obj.full_clean()
            obj.save()
            self.assertEqual(model.objects.count(), item_count + 1)
            if val:
                self.assertEqual(model.objects.get(weight=val), obj)
            self.assertEqual(model.objects.get(slug=slug), obj)
        else:
            self.assertNotEqual(model.objects.count(), item_count + 1)
            self.assertNotIn(obj, model.objects.all())

    def test_validation_is_none_correct_model_item_field_text(self):
        """
        Тестируем поле text, ошибка если не содержит (роскошно|превосходно).
        """
        item_count = Item.objects.count()
        with self.assertRaises(exceptions.ValidationError):
            self.item = Item(
                name='Item_name2',
                is_published=True,
                text='Item',
                category=self.category,
            )
            self.item.full_clean()
            self.item.save()
            self.item.tags.add(self.tag)

        self.assertEqual(Item.objects.count(), item_count)

    def test_validation_is_correct_model_item_field_text_created(self):
        """
        Тестируем поле text, корректно если содержит (роскошно|превосходно).
        """
        words = ('роскошно', 'превосходно')
        item_count = Item.objects.count()
        for text in words:
            with self.subTest(text=text):
                self.item = Item(
                    name='Item_name2',
                    is_published=True,
                    text=text,
                    category=self.category,
                )
                self.item.full_clean()
                self.item.save()
                self.item.tags.add(self.tag)

                self.assertEqual(Item.objects.count(), item_count + 1)
                item_count += 1
                self.assertEqual(Item.objects.get(text=text), self.item)

    def test_validation_slug_is_correct(self):
        """
        Тест валидации поля slug в Tag и Category содержит только 0-9,A-z,-,_.
        """
        slugs = (
            ('correct0A-_', Tag, True),
            ('correct0A-_', Category, True),
            ('не корректный слаг', Tag, False),
            ('не корректный слаг', Category, False),
        )

        for slug, model, bool_ in slugs:
            item_count = model.objects.count()
            with self.subTest(slug=slug, model=model):
                self.obj = model(
                    name=f'Name - {slug}',
                    is_published=True,
                    slug=slug,
                )
                self.func_for_tests(
                    self.obj, model, item_count, bool_, slug=slug
                )

    def test_category_validator_value_of_weight(self):
        """
        Тестируем валидацию значения weight поля Catalog в диапазоне [0,32767].
        """
        values = ((0, True), (300, True), (40000, False), (-1, False))
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
                self.func_for_tests(
                    self.obj, Category, item_count, bool_, val, slug
                )
