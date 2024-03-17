from django.db import models
from djangoProject.settings import MEDIA_URL
from user.models import User
# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    release_date = models.DateField(name="Release Date", null=True)
    imdb = models.DecimalField(decimal_places=1, max_digits=2, null=True)
    poster = models.ImageField(upload_to="~/Dev/datastore/poster/", default='~/Dev/datastore/poster/download.jpeg')
    vid = models.FileField(upload_to="~/Dev/datastore/poster/videos/", default="~/Dev/datastore/poster/videos/")

    def __str__(self):
        return self.name
class MovieUserRelation(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movies = models.ForeignKey(Movie, on_delete=models.CASCADE)
    pause_time = models.DurationField(null=True)

