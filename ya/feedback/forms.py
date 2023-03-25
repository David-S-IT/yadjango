from django import forms

from core.forms import BootstrapFormMixin
from .models import Feedback


class FeedbackForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Feedback
        fields = (
            Feedback.text.field.name,
            Feedback.email.field.name,
        )
        labels = {
            Feedback.text.field.name: 'Текст сообщения',
            Feedback.email.field.name: 'Ваш контактный email',
        }
        help_texts = {
            Feedback.email.field.name: 'На этот адрес будет отправлен ответ',
        }
        widgets = {
            Feedback.email.field.name: forms.EmailInput(
                attrs={'placeholder': 'default@example.com'}
            )
        }
