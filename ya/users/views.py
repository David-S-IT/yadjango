from datetime import timedelta

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone

from .forms import (
    CustomUserChangeForm,
    CustomUserCreationForm,
    ProfileChangeForm,
)
from .models import Profile

User = get_user_model()


def sign_up(request):
    template = 'users/sign_up.html'
    form = CustomUserCreationForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data[User.username.field.name]
        email = form.cleaned_data[User.email.field.name]

        user = form.save()
        user.is_active = settings.IS_ACTIVE
        user.save()

        if not settings.IS_ACTIVE:
            mail_text = f"""Здравствуйте!

Вы получили это сообщение, так как зарегистрировались на Yadjango.

Для активации своего профиля перейдите по ссылке:
{request.build_absolute_uri(reverse('users:activate',
                                    kwargs={'username': username}))}

Спасибо, что присоединились к нам!

© Yadjango
"""
            send_mail(
                'Yadjango company',
                mail_text,
                settings.ADMIN_EMAIL,
                [email],
                fail_silently=False,
            )
        else:
            Profile.objects.get_or_create(user=user)

        return redirect('users:profile')

    context = {'form': form}
    return render(request, template, context)


def activate(request, username):
    user = get_object_or_404(
        User.objects.get_queryset(),
        username=username,
        is_active=0,
    )

    is_link_expired = timezone.now() - user.date_joined > timedelta(hours=12)

    if is_link_expired:
        raise Http404

    user.is_active = 1
    user.save()

    Profile.objects.get_or_create(user=user)

    template = 'users/activate.html'
    context = {'username': username}
    return render(request, template, context)


def users_list(request):
    users = (
        User.objects.get_queryset()
        .select_related(
            User.profile.related.name,
        )
        .filter(is_active=True)
        .order_by(User.username.field.name)
        .only(
            User.username.field.name,
            User.first_name.field.name,
            User.last_name.field.name,
        )
    )
    template = 'users/users_list.html'
    context = {'users': users}
    return render(request, template, context)


def user_detail(request, pk):
    user = get_object_or_404(
        User.objects.get_queryset()
        .select_related(
            User.profile.related.name,
        )
        .only(
            User.username.field.name,
            User.email.field.name,
            User.first_name.field.name,
            User.last_name.field.name,
        ),
        id=pk,
        is_active=1,
    )

    template = 'users/user_detail.html'
    context = {'user_pk': user}
    return render(request, template, context)


@login_required
def profile(request):
    user = get_object_or_404(
        User.objects.get_queryset()
        .select_related(
            User.profile.related.name,
        )
        .only(
            User.username.field.name,
            User.email.field.name,
            User.first_name.field.name,
            User.last_name.field.name,
        ),
        id=request.user.id,
        is_active=1,
    )

    profile_object = get_object_or_404(
        Profile.objects.get_queryset(),
        user=user,
    )

    form = CustomUserChangeForm(request.POST or None, instance=user)

    form_profile = ProfileChangeForm(
        request.POST or None,
        files=request.FILES or None,
        instance=profile_object,
    )

    if form.is_valid() and form_profile.is_valid():
        form.save()
        form_profile.save()

        messages.success(request, 'Изменения сохранены')

        return redirect('users:profile')

    template = 'users/profile.html'
    context = {'form': form, 'form_profile': form_profile, 'user_me': user}
    return render(request, template, context)


class CustomLoginView(LoginView):
    redirect_authenticated_user = True
