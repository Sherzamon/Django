# Generated by Django 4.2.1 on 2023-07-04 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangosignals', '0024_alter_productshop_product_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productshop',
            name='product_code',
            field=models.BigIntegerField(blank=True, default=3199645818, null=True, unique=True),
        ),
    ]
