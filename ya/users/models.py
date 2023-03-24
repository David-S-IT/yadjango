from django.contrib.auth.models import User
from django.db import models

from core.models import ImageBaseModel


class Profile(ImageBaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField(
        'дата рождения',
        blank=True,
        null=True,
        help_text=(
            'Введите дату рождения вида: DD.MM.YYYY. '
            'Где D - день, M - месяц, Y - год.'
        ),
    )
    image = models.ImageField(
        'аватарка',
        upload_to='media/%Y/%m/',
        blank=True,
        null=True,
        help_text=(
            'По аватарке другие люди смогут вас узнавать, '
            'а вам будет проще определять, в какой аккаунт вы вошли.'
        ),
    )
    coffee_count = models.PositiveIntegerField(
        'количество попыток сварить кофе',
        default=0,
        help_text='Сколько чашек кофе вы пытались выпить.',
    )

    class Meta:
        default_related_name = 'profile'
        verbose_name = 'информация о пользователе'
        verbose_name_plural = 'информация о пользователях'

    def __str__(self):
        return str(self.user)
