# Generated by Django 3.2.18 on 2023-02-28 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20230228_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryimage',
            name='image',
            field=models.ImageField(default='', upload_to='media/%Y/%m', verbose_name='Будет приведено к ширине 300px'),
        ),
        migrations.AlterField(
            model_name='mainimage',
            name='image',
            field=models.ImageField(default='', upload_to='media/%Y/%m', verbose_name='Будет приведено к ширине 300px'),
        ),
    ]
