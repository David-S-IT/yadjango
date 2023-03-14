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

    text = models.CharField(
        'Текст',
        max_length=200,
        help_text='Максимальная длина 200 символов.',
    )
    created_on = models.DateTimeField('Дата создания', auto_now_add=True)
    email = models.EmailField(
        'Почта',
        max_length=150,
        default='default@example.com',
        help_text='Максимум 150 символов.',
    )
    status = models.CharField(
        'Статус обработки',
        max_length=3,
        choices=STATUSES,
        default=GET,
    )

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'

    def __str__(self):
        return f'{self.text[:20]}...'
