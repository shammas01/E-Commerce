# Generated by Django 4.2 on 2023-05-18 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_wishlist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wishlist',
            old_name='product',
            new_name='Product',
        ),
    ]
