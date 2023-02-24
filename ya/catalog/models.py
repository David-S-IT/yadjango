from catalog.validators import ValidateMustContain
from core.models import NameBaseModel, PublishedBaseModel, SlugBaseModel
from django.core.validators import MaxValueValidator
from django.db import models


class Category(NameBaseModel, PublishedBaseModel, SlugBaseModel):
    weight = models.PositiveSmallIntegerField(
        'вес',
        default=100,
        validators=[MaxValueValidator(32767)],
        help_text='Максимальная длина 100 символов',
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Tag(NameBaseModel, PublishedBaseModel, SlugBaseModel):
    class Meta:
        default_related_name = 'tags'
        ordering = ['name']
        verbose_name = 'тег'
        verbose_name_plural = 'теги'


class Item(NameBaseModel, PublishedBaseModel):
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='категория',
        help_text='Категория, к которой относится товар',
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        verbose_name='тег',
        help_text='Тег для товара',
    )
    text = models.TextField(
        verbose_name='описание товара',
        validators=[ValidateMustContain('роскошно', 'превосходно')],
        help_text=(
            'Описание товара обязательно должно содержать'
            ' слова: роскошно или превосходно'
        ),
    )

    class Meta:
        ordering = ['name']
        default_related_name = 'items'
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
