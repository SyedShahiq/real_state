# Generated by Django 3.0.8 on 2020-09-17 10:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 9, 17, 10, 27, 41, 612423)),
        ),
    ]
