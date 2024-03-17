# Generated by Django 5.0 on 2023-12-27 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_movie_path_alter_movie_imdb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='path',
        ),
        migrations.AddField(
            model_name='movie',
            name='post_path',
            field=models.FilePathField(allow_folders=True, default='/home/j1roscope/Dev/djangoProject/movies_data/poster/download.jpeg', path='/home/j1roscope/Dev/djangoProject/movies_data/poster/', recursive=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='vid_path',
            field=models.FilePathField(allow_folders=True, default='/home/j1roscope/Dev/djangoProject/movies_data/videos/test.mp4', path='/home/j1roscope/Dev/djangoProject/movies_data/videos/', recursive=True),
        ),
    ]
