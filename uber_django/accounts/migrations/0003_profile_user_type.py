# Generated by Django 2.1.7 on 2019-07-22 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190722_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_type',
            field=models.IntegerField(choices=[(1, 'Driver'), (2, 'Client')], default=2),
        ),
    ]
