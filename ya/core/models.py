from django.db import models


class NameBaseModel(models.Model):
    name = models.CharField(
        'название',
        unique=True,
        max_length=150,
        help_text='Максимальная длина 150 символов',
    )

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.name[:15]


class PublishedBaseModel(models.Model):
    is_published = models.BooleanField(
        'опубликовано',
        default=True,
        help_text='Статус публикации',
    )

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.name[:15]


class SlugBaseModel(models.Model):
    slug = models.SlugField(
        verbose_name='уникальный адрес',
        unique=True,
        max_length=200,
        help_text='Максимальная длина 200 символов',
    )

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.name[:15]
