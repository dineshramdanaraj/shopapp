# Generated by Django 3.2.19 on 2023-07-20 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0005_alter_cart_item_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart_item',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]