# Generated by Django 2.0.7 on 2019-12-23 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_checkin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Phone', models.CharField(max_length=10)),
            ],
        ),
    ]
