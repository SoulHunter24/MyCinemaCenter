# Generated by Django 3.2.2 on 2021-05-23 12:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mycinema', '0006_rename_post_news'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='description',
            new_name='main_description',
        ),
        migrations.RemoveField(
            model_name='news',
            name='actors',
        ),
        migrations.RemoveField(
            model_name='news',
            name='director',
        ),
        migrations.RemoveField(
            model_name='news',
            name='type',
        ),
        migrations.AddField(
            model_name='news',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='news',
            name='short_description',
            field=models.TextField(blank=True),
        ),
    ]