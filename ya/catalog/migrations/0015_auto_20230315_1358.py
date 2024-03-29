# Generated by Django 3.2.18 on 2023-03-15 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_alter_category_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text='Максимальная длина 64 символ', max_length=64, unique=True, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(help_text='Максимальная длина 64 символ', max_length=64, unique=True, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(help_text='Максимальная длина 64 символ', max_length=64, unique=True, verbose_name='название'),
        ),
    ]
