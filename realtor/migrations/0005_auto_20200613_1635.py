# Generated by Django 3.0.7 on 2020-06-13 11:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtor', '0004_auto_20200613_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='hire_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 13, 16, 35, 43, 124203)),
        ),
    ]
