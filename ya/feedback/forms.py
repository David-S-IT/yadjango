from django import forms

from .models import Feedback


class FeedbackForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

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
            Feedback.email.field.name: 'На этот адрес будет отправлен ответ.',
        }
        widgets = {
            Feedback.email.field.name: forms.EmailInput(
                attrs={'placeholder': Feedback.email.field.default}
            )
        }
