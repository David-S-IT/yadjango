import django.core.validators
from core.models import CategoryBase
from django.db import models


class Category(CategoryBase):
    weight = models.IntegerField(
        default=100,
        validators=[
            django.core.validators.MinValueValidator(0),
            django.core.validators.MaxValueValidator(32767),
        ],
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Tag(CategoryBase):
    class Meta:
        ordering = ['name']
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Item(CategoryBase):
    text = models.TextField(
        verbose_name='Описание товара',
        validators=[
            django.core.validators.RegexValidator(r'(роскошно|превосходно)')
        ],
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='category',
        verbose_name='Категория',
        help_text='Категория, к которой относится товар',
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name='tags',
        verbose_name='Тег',
        help_text='Тег для товара',
    )
    slug = None

    class Meta:
        ordering = ['name']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
