# Generated by Django 3.0 on 2020-01-06 11:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0027_auto_20200106_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='exit',
            name='Pswd',
            field=models.CharField(default='', max_length=32),
        ),
        migrations.AlterField(
            model_name='checkin',
            name='itime',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 6, 11, 58, 58, 454964, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='otime',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 6, 11, 58, 58, 458967, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='exit',
            name='otime',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 6, 11, 58, 58, 458967, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='host',
            name='itime',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 6, 11, 58, 58, 454964, tzinfo=utc)),
        ),
    ]
