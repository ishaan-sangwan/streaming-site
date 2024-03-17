from django.contrib import admin
from .models import Movie, MovieUserRelation
# Register your models here.
admin.site.register(Movie)
admin.site.register(MovieUserRelation)