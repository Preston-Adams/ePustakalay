# Generated by Django 3.1.4 on 2021-01-08 15:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('emanagement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 15, 15, 38, 5, 588288, tzinfo=utc), help_text='By defualt date is 7 days'),
        ),
    ]
