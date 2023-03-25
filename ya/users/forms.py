from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    UserChangeForm,
    UserCreationForm,
)

from .models import Profile

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = (
            User.username.field.name,
            User.email.field.name,
        )
        help_texts = {
            User.email.field.name: 'На этот адрес будет отправлено письмо с '
            'подтверждением.',
        }


class CustomUserChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    password = None

    class Meta:
        model = User
        fields = (
            User.email.field.name,
            User.first_name.field.name,
            User.last_name.field.name,
        )


class ProfileChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    password = None

    class Meta:
        model = Profile
        fields = (
            Profile.birthday.field.name,
            Profile.image.field.name,
        )
