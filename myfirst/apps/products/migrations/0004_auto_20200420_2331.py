# Generated by Django 3.0.5 on 2020-04-20 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_product_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productimg',
            options={'verbose_name': 'picture', 'verbose_name_plural': 'pictures'},
        ),
        migrations.AddField(
            model_name='product',
            name='short_product_description',
            field=models.CharField(blank=True, default=None, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='productimg',
            name='image',
            field=models.ImageField(upload_to='products_images'),
        ),
    ]
