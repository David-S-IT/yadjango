# Generated by Django 3.2.18 on 2023-03-14 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='status',
            field=models.CharField(default='получено', max_length=11, verbose_name='Статус обработки'),
        ),
    ]