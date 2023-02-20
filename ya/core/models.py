from django.core.validators import RegexValidator
from django.db import models


class CategoryBase(models.Model):
    name = models.CharField('Название', max_length=150)
    slug = models.SlugField(
        verbose_name='Уникальный адрес',
        unique=True,
        max_length=200,
        validators=[RegexValidator(r'^[\w-]+$')],
    )
    is_published = models.BooleanField(
        'Опубликовано',
        default=True,
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        abstract = True
