# Generated by Django 3.2.2 on 2021-06-04 08:18

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mycinema', '0002_filmopinion'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FilmOpinion',
            new_name='FilmOpinions',
        ),
    ]