# Generated by Django 4.1.1 on 2022-10-19 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_rename_history_blog_content_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='tag_title',
            new_name='title',
        ),
    ]
