# Generated by Django 4.1.1 on 2022-10-11 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Properties',
            },
        ),
        migrations.RemoveField(
            model_name='product_version',
            name='cover_image',
        ),
        migrations.AddField(
            model_name='image',
            name='is_main',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='PropertyValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.property')),
            ],
        ),
        migrations.CreateModel(
            name='ProductPropertyValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product_version')),
                ('property_value', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.property')),
            ],
        ),
    ]
