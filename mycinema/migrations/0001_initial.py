# Generated by Django 3.2.3 on 2021-05-21 21:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=100)),
                ('actors', models.CharField(max_length=100)),
                ('short_description', models.CharField(max_length=100)),
                ('duration_in_minutes', models.IntegerField()),
                ('date_posted', models.DateTimeField(default=datetime.datetime(2021, 5, 21, 21, 43, 1, 763790, tzinfo=utc))),
            ],
        ),
    ]