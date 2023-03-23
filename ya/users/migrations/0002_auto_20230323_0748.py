# Generated by Django 3.2.18 on 2023-03-23 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'default_related_name': 'profile', 'verbose_name': 'информация о пользователе', 'verbose_name_plural': 'информация о пользователях'},
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/%Y/%m/', verbose_name='аватарка'),
        ),
    ]
