# Generated by Django 4.0.5 on 2022-06-24 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0002_category_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]