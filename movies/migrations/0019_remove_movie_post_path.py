# Generated by Django 5.0 on 2024-01-19 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0018_movie_poster_alter_movie_post_path_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='post_path',
        ),
    ]
