from django.db import models


class Feedback(models.Model):
    GET = 'get'
    IN_PROCESSING = 'saw'
    ANSWERED = 'ans'
    STATUSES = [
        (GET, 'получено'),
        (IN_PROCESSING, 'в обработке'),
        (ANSWERED, 'ответ дан'),
    ]

    text = models.TextField(
        'текст',
        max_length=200,
        help_text='Максимальная длина 200 символов',
    )
    created_on = models.DateTimeField(
        'дата создания',
        auto_now_add=True,
        help_text='Когда был написан отзыв',
    )
    email = models.EmailField(
        'почта',
        max_length=254,
        help_text='Максимум 150 символов',
    )
    status = models.CharField(
        'статус обработки',
        max_length=3,
        choices=STATUSES,
        default=GET,
        help_text='Что сейчас происходит с отзывом',
    )

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'

    def __str__(self):
        return f'{self.text[:20]}...'
