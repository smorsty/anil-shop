# Generated by Django 4.1.1 on 2022-11-29 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0015_remove_orderitem_shoes_size"),
    ]

    operations = [
        migrations.RemoveField(model_name="orderitem", name="clothes_size",),
        migrations.AddField(
            model_name="orderitem",
            name="size",
            field=models.CharField(default="", max_length=10),
        ),
    ]