from ckeditor.fields import RichTextField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.safestring import mark_safe
from sorl.thumbnail import get_thumbnail

from core.models import (
    ImageBaseModel,
    NameBaseModel,
    PublishedBaseModel,
    SlugBaseModel,
)
from .managers import ItemManager
from .validators import ValidateMustContain


class Category(NameBaseModel, PublishedBaseModel, SlugBaseModel):
    weight = models.PositiveSmallIntegerField(
        'вес',
        default=100,
        validators=[MinValueValidator(1), MaxValueValidator(32767)],
        help_text='Максимальная длина 100 символов',
    )

    class Meta:
        default_related_name = 'categories'
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
    objects = ItemManager()

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
    text = RichTextField(
        verbose_name='описание товара',
        validators=[ValidateMustContain('роскошно', 'превосходно')],
        help_text=(
            'Описание товара обязательно должно содержать'
            ' слова: роскошно или превосходно'
        ),
    )
    is_on_main = models.BooleanField(
        'опубликовано на главной',
        default=False,
        help_text='Включить публикацию на главной',
    )

    class Meta:
        ordering = ['name']
        default_related_name = 'items'
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def main_image_tmb(self):
        if self.main_image:
            return mark_safe(
                f'<img src="{self.main_image.get_small_img.url}">'
            )
        return 'Нет изображения'

    main_image_tmb.short_description = 'превью'
    main_image_tmb.allow_tags = True


class GalleryImage(ImageBaseModel):
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        verbose_name='товар',
        null=True,
        help_text='Наименование товара',
    )

    def image_tmb(self):
        if self.image:
            return mark_safe(f'<img src="{self.get_image_300x300.url}">')
        return 'Нет изображения'

    image_tmb.short_description = 'изображение для галереи'
    image_tmb.allow_tags = True

    class Meta:
        default_related_name = 'gallery'
        verbose_name = 'изображение для галереи'
        verbose_name_plural = 'изображения для галереи'

    def __str__(self):
        return f'Изображение - {self.item}'


class MainImage(ImageBaseModel):
    item = models.OneToOneField(
        Item,
        on_delete=models.CASCADE,
        verbose_name='товар',
        null=True,
        help_text='Наименование товара',
    )

    class Meta:
        default_related_name = 'main_image'
        verbose_name = 'главное изображение'
        verbose_name_plural = 'главные изображения'

    @property
    def get_small_img(self):
        return get_thumbnail(self.image, '100x100', crop='center', quality=51)

    def image_tmb(self):
        if self.image:
            return mark_safe(f'<img src="{self.get_image_300x300.url}">')
        return 'Нет изображения'

    image_tmb.short_description = 'основное фото товара'
    image_tmb.allow_tags = True

    def __str__(self):
        return f'Основное изображение для {self.item}'
