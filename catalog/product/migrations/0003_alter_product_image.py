# Generated by Django 4.2.3 on 2023-08-01 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default=None, unique=True, upload_to='media/Products-Avatar/'),
            preserve_default=False,
        ),
    ]
