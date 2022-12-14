# Generated by Django 4.1.1 on 2022-11-28 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0009_alter_product_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="discount_price",
            field=models.DecimalField(
                blank=True, decimal_places=0, max_digits=20, null=True
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.DecimalField(
                blank=True, decimal_places=0, max_digits=20, null=True
            ),
        ),
    ]
