# Generated by Django 2.1.7 on 2019-08-05 14:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20190805_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='user_driver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='driver_orders', to=settings.AUTH_USER_MODEL),
        ),
    ]
