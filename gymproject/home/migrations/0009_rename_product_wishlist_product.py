# Generated by Django 4.2 on 2023-05-18 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_rename_product_wishlist_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wishlist',
            old_name='Product',
            new_name='product',
        ),
    ]
