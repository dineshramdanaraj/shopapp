# Generated by Django 3.2.19 on 2023-07-23 17:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shopping', '0012_alter_rating_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='reviews',
            fields=[
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now_add=True)),
                ('comment', models.TextField(null=True)),
                ('item_to_review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.item')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]