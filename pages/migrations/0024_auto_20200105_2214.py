# Generated by Django 3.0 on 2020-01-05 16:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0023_auto_20200105_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkin',
            name='itime',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 5, 16, 44, 56, 491146, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='otime',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 5, 16, 44, 56, 491146, tzinfo=utc)),
        ),
    ]
