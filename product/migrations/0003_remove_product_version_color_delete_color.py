# Generated by Django 4.1.1 on 2022-10-11 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_property_remove_product_version_cover_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_version',
            name='color',
        ),
        migrations.DeleteModel(
            name='color',
        ),
    ]