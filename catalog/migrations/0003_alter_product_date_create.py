# Generated by Django 4.2.3 on 2023-08-01 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_product_date_create_alter_product_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_create',
            field=models.DateField(auto_now=True, verbose_name='дата создания'),
        ),
    ]