# Generated by Django 5.0 on 2024-01-19 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0020_movie_vid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='vid',
        ),
        migrations.AddField(
            model_name='test',
            name='vid',
            field=models.FileField(default='~/Dev/datastore/poster/videos/', upload_to='~/Dev/datastore/poster/videos/'),
        ),
    ]