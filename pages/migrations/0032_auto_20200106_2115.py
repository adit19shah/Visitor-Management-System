# Generated by Django 3.0 on 2020-01-06 15:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0031_auto_20200106_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkin',
            name='itime',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 6, 21, 15, 26, 456797)),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='otime',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 6, 21, 15, 26, 457796)),
        ),
        migrations.AlterField(
            model_name='exit',
            name='otime',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 6, 21, 15, 26, 458796)),
        ),
        migrations.AlterField(
            model_name='host',
            name='itime',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 6, 21, 15, 26, 454798)),
        ),
    ]
