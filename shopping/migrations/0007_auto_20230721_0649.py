# Generated by Django 3.2.19 on 2023-07-21 01:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0006_alter_cart_item_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='ph_no',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxLengthValidator(10)]),
        ),
    ]