# Generated by Django 4.1.1 on 2022-10-19 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_rename_tag_title_tag_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='blogTag',
            new_name='tag',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='blog_title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='blog_title_az',
            new_name='title_az',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='blog_title_en',
            new_name='title_en',
        ),
    ]
