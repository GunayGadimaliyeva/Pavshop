# Generated by Django 4.1.1 on 2022-10-08 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_title_az',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_title_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='desc_az',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='desc_en',
            field=models.TextField(null=True),
        ),
    ]
