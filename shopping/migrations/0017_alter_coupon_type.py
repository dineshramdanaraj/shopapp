# Generated by Django 3.2.19 on 2023-07-24 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0016_alter_coupon_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='type',
            field=models.CharField(choices=[('%', 'percentage'), ('Rs', 'amount'), ('N', 'none')], default='N', max_length=2),
        ),
    ]