from django.db import models
from django_cleanup.signals import cleanup_pre_delete
from sorl.thumbnail import delete, get_thumbnail


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


class SlugBaseModel(models.Model):
    slug = models.SlugField(
        verbose_name='уникальный адрес',
        unique=True,
        max_length=200,
        help_text='Максимальная длина 200 символов',
    )

    class Meta:
        abstract = True


class ImageBaseModel(models.Model):
    image = models.ImageField(
        'Будет приведено к ширине 300px',
        upload_to='media/%Y/%m',
        default=''
    )

    class Meta:
        abstract = True

    @property
    def get_image_300x300(self):
        return get_thumbnail(self.image, '300x300', crop='center', quality=51)

    def sorl_delete(**kwargs):
        delete(kwargs['file'])

    cleanup_pre_delete.connect(sorl_delete)
