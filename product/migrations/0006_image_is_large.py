# Generated by Django 4.1.1 on 2022-10-16 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_productcategory_category_name_az_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='is_large',
            field=models.BooleanField(default=False),
        ),
    ]
