"""
Django settings for ya project.

Generated by 'django-admin startproject' using Django 3.2.17.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path

import dotenv

dotenv.load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', 'not_so_secret')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', 'True').capitalize() == 'True'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '*').split(',')

ADMIN_EMAIL = os.getenv('ADMIN_EMAIL', 'default@example.com')

IS_ACTIVE = (
    os.getenv('IS_ACTIVE', 'True' if DEBUG else 'False').capitalize() == 'True'
)

if DEBUG:
    from django.contrib.messages import constants as message_constants

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_cleanup.apps.CleanupConfig',
    'sorl.thumbnail',
    'ckeditor',
    'ckeditor_uploader',
    'about.apps.AboutConfig',
    'catalog.apps.CatalogConfig',
    'core.apps.CoreConfig',
    'feedback.apps.FeedbackConfig',
    'homepage.apps.HomepageConfig',
    'users.apps.UsersConfig',
]
if DEBUG:
    INSTALLED_APPS.append('debug_toolbar')

INTERNAL_IPS = [
    '127.0.0.1',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'ya.middlewares.middleware.ReverseTextMiddleware',
]
if DEBUG:
    MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')

MIDDLEWARE_CUSTOM_REVERSE_RU_TEXT = (
    os.getenv('MIDDLEWARE_CUSTOM_REVERSE_RU_TEXT', 'False').capitalize()
    == 'True'
)

ROOT_URLCONF = 'ya.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.context_processors.year.year',
            ],
        },
    },
]
if DEBUG:
    TEMPLATES[0]['OPTIONS']['context_processors'].append(
        'django.template.context_processors.debug'
    )

WSGI_APPLICATION = 'ya.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.'
        'password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.'
        'password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.'
        'password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.'
        'password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [BASE_DIR / 'static_dev']
STATIC_ROOT = BASE_DIR / 'static'
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

CKEDITOR_UPLOAD_PATH = '/ckeditor/%Y/%m'

CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        # 'skin': 'office2013',
        'toolbar_Basic': [['Source', '-', 'Bold', 'Italic']],
        'toolbar_YourCustomToolbarConfig': [
            {
                'name': 'document',
                'items': [
                    'Source',
                    '-',
                    'Save',
                    'NewPage',
                    'Preview',
                    'Print',
                    '-',
                    'Templates',
                ],
            },
            {
                'name': 'clipboard',
                'items': [
                    'Cut',
                    'Copy',
                    'Paste',
                    'PasteText',
                    'PasteFromWord',
                    '-',
                    'Undo',
                    'Redo',
                ],
            },
            {
                'name': 'editing',
                'items': ['Find', 'Replace', '-', 'SelectAll'],
            },
            {
                'name': 'forms',
                'items': [
                    'Form',
                    'Checkbox',
                    'Radio',
                    'TextField',
                    'Textarea',
                    'Select',
                    'Button',
                    'ImageButton',
                    'HiddenField',
                ],
            },
            '/',
            {
                'name': 'basicstyles',
                'items': [
                    'Bold',
                    'Italic',
                    'Underline',
                    'Strike',
                    'Subscript',
                    'Superscript',
                    '-',
                    'RemoveFormat',
                ],
            },
            {
                'name': 'paragraph',
                'items': [
                    'NumberedList',
                    'BulletedList',
                    '-',
                    'Outdent',
                    'Indent',
                    '-',
                    'Blockquote',
                    'CreateDiv',
                    '-',
                    'JustifyLeft',
                    'JustifyCenter',
                    'JustifyRight',
                    'JustifyBlock',
                    '-',
                    'BidiLtr',
                    'BidiRtl',
                    'Language',
                ],
            },
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {
                'name': 'insert',
                'items': [
                    'Image',
                    'Flash',
                    'Table',
                    'HorizontalRule',
                    'Smiley',
                    'SpecialChar',
                    'PageBreak',
                    'Iframe',
                ],
            },
            '/',
            {
                'name': 'styles',
                'items': ['Styles', 'Format', 'Font', 'FontSize'],
            },
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            {'name': 'about', 'items': ['About']},
            '/',  # put this to force next toolbar on new line
            {
                'name': 'yourcustomtools',
                'items': [
                    # put the name of your editor.ui.addButton here
                    'Preview',
                    'Maximize',
                ],
            },
        ],
        'toolbar': 'YourCustomToolbarConfig',
        'tabSpaces': 4,
        'extraPlugins': ','.join(
            [
                'uploadimage',  # the upload image feature
                # your extra plugins here
                'div',
                'autolink',
                'autoembed',
                'embedsemantic',
                'autogrow',
                # 'devtools',
                'widget',
                'lineutils',
                'clipboard',
                'dialog',
                'dialogui',
                'elementspath',
            ]
        ),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = BASE_DIR / 'send_mail'
EMAIL_URL = '/uploads/'

MESSAGE_TAGS = {
    message_constants.SUCCESS: 'w-100 alert alert-success text-center',
    message_constants.ERROR: 'w-100 alert alert-danger text-center',
}

LOGIN_URL = '/auth/login/'
LOGIN_REDIRECT_URL = '/'
