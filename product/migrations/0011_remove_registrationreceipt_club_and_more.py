# Generated by Django 4.1.1 on 2022-10-19 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_remove_club_members'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrationreceipt',
            name='club',
        ),
        migrations.RemoveField(
            model_name='registrationreceipt',
            name='person',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categor', to='product.productcategory'),
        ),
        migrations.DeleteModel(
            name='Club',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='RegistrationReceipt',
        ),
    ]