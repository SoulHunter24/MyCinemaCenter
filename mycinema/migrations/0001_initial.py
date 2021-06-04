# Generated by Django 3.2.2 on 2021-06-04 07:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_description', models.CharField(default='', max_length=100)),
                ('main_description', models.TextField(blank=True)),
                ('total_rating', models.IntegerField(default=0)),
                ('is_accepted', models.BooleanField(default=False)),
                ('moderator', models.CharField(default='-', max_length=50)),
                ('opinion_counter', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=100)),
                ('genre', models.CharField(choices=[('Action', 'Action'), ('Adventure', 'Adventure'), ('Comedy', 'Comedy'), ('Crime', 'Crime'), ('Fantasy', 'Fantasy'), ('Historical', 'Historical'), ('Horror', 'Horror'), ('Musical', 'Musical'), ('Romance', 'Romance'), ('Science Fiction', 'Science Fiction'), ('Thriller', 'Thriller'), ('Western', 'Western')], max_length=50, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_description', models.CharField(default='', max_length=100)),
                ('main_description', models.TextField(blank=True)),
                ('total_rating', models.IntegerField(default=0)),
                ('is_accepted', models.BooleanField(default=False)),
                ('moderator', models.CharField(default='-', max_length=50)),
                ('opinion_counter', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('MOVIE', 'MOVIE'), ('TVSERIES', 'TVSERIES'), ('DIRECTORS', 'DIRECTORIES'), ('CINEMAS', 'CINEMAS'), ('ACTORS', 'ACTORS'), ('OTHERS', 'OTHERS')], max_length=50, null=True)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_description', models.CharField(default='', max_length=100)),
                ('main_description', models.TextField(blank=True)),
                ('total_rating', models.IntegerField(default=0)),
                ('is_accepted', models.BooleanField(default=False)),
                ('moderator', models.CharField(default='-', max_length=50)),
                ('opinion_counter', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=100)),
                ('profession', models.CharField(choices=[('Actor', 'Actor'), ('Director', 'Director'), ('Producer', 'Producer'), ('Director of Photography', 'Director of Photography'), ('Costume Designer', 'Costume Designer'), ('Movie Editor', 'Movie Editor'), ('Composer', 'Composer')], max_length=50, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
                ('related_films', models.ManyToManyField(to='mycinema.Film')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Opinions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opinion', models.TextField(blank=True)),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('authorek', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opinionss', to='mycinema.news')),
            ],
        ),
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_description', models.CharField(default='', max_length=100)),
                ('main_description', models.TextField(blank=True)),
                ('total_rating', models.IntegerField(default=0)),
                ('is_accepted', models.BooleanField(default=False)),
                ('moderator', models.CharField(default='-', max_length=50)),
                ('opinion_counter', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=100)),
                ('image', django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='cinema/cinema_default.png', force_format=None, keep_meta=True, quality=90, size=[256, 256], upload_to='cinema/')),
                ('localization', models.CharField(default='Unknown', max_length=60)),
                ('opening_hours', models.TextField(blank=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
