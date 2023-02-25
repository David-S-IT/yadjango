# Generated by Django 3.2.18 on 2023-02-25 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_item_text'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': 'категория', 'verbose_name_plural': 'категории'},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'default_related_name': 'items', 'ordering': ['name'], 'verbose_name': 'товар', 'verbose_name_plural': 'товары'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'default_related_name': 'tags', 'ordering': ['name'], 'verbose_name': 'тег', 'verbose_name_plural': 'теги'},
        ),
        migrations.AlterField(
            model_name='category',
            name='is_published',
            field=models.BooleanField(default=True, help_text='Статус публикации', verbose_name='опубликовано'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(help_text='Максимальная длина 200 символов', max_length=200, unique=True, verbose_name='уникальный адрес'),
        ),
        migrations.AlterField(
            model_name='item',
            name='is_published',
            field=models.BooleanField(default=True, help_text='Статус публикации', verbose_name='опубликовано'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='is_published',
            field=models.BooleanField(default=True, help_text='Статус публикации', verbose_name='опубликовано'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(help_text='Максимальная длина 200 символов', max_length=200, unique=True, verbose_name='уникальный адрес'),
        ),
    ]