from rest_framework import serializers
from .models import Movie
class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class MoviesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["name", "Release Date", "imdb"]
