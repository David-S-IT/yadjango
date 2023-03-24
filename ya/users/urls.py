from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeDoneView,
    PasswordChangeView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
)
from django.urls import path, register_converter

from catalog import converter
from . import views

register_converter(converter.PositiveIntegerConverter, 'PosIntConv')

app_name = 'users'

urlpatterns = [
    path(
        'login/',
        LoginView.as_view(
            template_name='users/login.html',
        ),
        name='login',
    ),
    path(
        'logout/',
        LogoutView.as_view(
            template_name='users/logged_out.html',
        ),
        name='logout',
    ),
    path(
        'password_change/',
        PasswordChangeView.as_view(
            template_name='users/password_change_form.html',
        ),
        name='password_change',
    ),
    path(
        'password_change/done/',
        PasswordChangeDoneView.as_view(
            template_name='users/password_change_done.html',
        ),
        name='password_change_done',
    ),
    path(
        'password_reset/',
        PasswordResetView.as_view(
            template_name='users/password_reset_form.html',
        ),
        name='password_reset',
    ),
    path(
        'password_reset/done/',
        PasswordResetDoneView.as_view(
            template_name='users/password_reset_done.html',
        ),
        name='password_reset_done',
    ),
    path(
        'reset/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
            template_name='users/password_reset_confirm.html',
        ),
        name='password_reset_confirm',
    ),
    path(
        'reset/done/',
        PasswordResetCompleteView.as_view(
            template_name='users/password_reset_complete.html',
        ),
        name='password_reset_complete',
    ),
    path(
        'sign_up/',
        views.sign_up,
        name='sign_up',
    ),
    path(
        'activate/<str:username>/',
        views.activate,
        name='activate',
    ),
    path(
        'users_list/',
        views.users_list,
        name='users_list',
    ),
    path(
        'user_detail/<PosIntConv:pk>/',
        views.user_detail,
        name='user_detail',
    ),
    path(
        'profile/',
        views.profile,
        name='profile',
    ),
]
