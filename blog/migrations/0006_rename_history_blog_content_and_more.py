# Generated by Django 4.1.1 on 2022-10-19 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_comment_customer_comment_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='history',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='desc',
            new_name='short_desc',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='desc_az',
            new_name='short_desc_az',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='desc_en',
            new_name='short_desc_en',
        ),
    ]
