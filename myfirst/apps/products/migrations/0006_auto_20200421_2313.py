# Generated by Django 3.0.5 on 2020-04-21 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_productimg_is_main'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productimg',
            options={'verbose_name': 'Фото', 'verbose_name_plural': 'Фотографии'},
        ),
    ]
