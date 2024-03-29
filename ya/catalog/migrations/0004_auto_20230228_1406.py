# Generated by Django 3.2.18 on 2023-02-28 14:06

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20230225_1341'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='catalog/', verbose_name='Будет приведено к ширине 1280px')),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='weight',
            field=models.PositiveSmallIntegerField(default=100, help_text='Максимальная длина 100 символов', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(32767)], verbose_name='вес'),
        ),
        migrations.AddField(
            model_name='item',
            name='main_image',
            field=models.ForeignKey(blank=True, help_text='Фото товара', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items', to='catalog.image', verbose_name='картинка'),
        ),
    ]
