from django.http import HttpResponseBadRequest
from django.contrib.postgres.search import SearchVector
from django.shortcuts import render
from django.http import FileResponse, StreamingHttpResponse, HttpResponse
from rest_framework import status
from rest_framework.views import APIView , Response, Http404
from rest_framework.permissions import IsAuthenticated
from .models import Movie
from .serializers import MoviesSerializer, MoviesListSerializer
import logging
from django.core.mail import send_mail
from django.conf import settings


logger = logging.getLogger(__name__)

CHUNK_SIZE = 1024 * 1024
# Create your views here.
class MoviesList(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        queryset = Movie.objects.all()
        try:
            serializer = MoviesListSerializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            print(f"exception found {e}")
            return Response(status=status.HTTP_400_BAD_REQUEST)

class MoviePull(APIView):
    permission_classes = [IsAuthenticated]
    def movie_maker(self, filepath):
        with open(filepath[1:], 'rb') as video:
            while True:
                video_data = video.read(1024 * 1024)
                if not video_data:
                    break
                yield video_data

    def get(self, request, name):
        try:
            movie = name
            queryset = Movie.objects.get(name=movie)
            serializer = MoviesSerializer(queryset)
            filepath = serializer.data['vid']
            vid_data = self.movie_maker(filepath)
            response = StreamingHttpResponse(vid_data, content_type='video/mp4')
            return response
        except Movie.DoesNotExist:
            raise Http404
class LoginStatus(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response("", status=status.HTTP_200_OK)


class MovieTile(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request, name):
        try:
            queryset = Movie.objects.get(name=name)
            serializer = MoviesSerializer(queryset)
            filepath = serializer.data["poster"][1:]
            with open(filepath, 'rb') as image:
                image_data = image.read()
            response = HttpResponse(image_data, content_type='image/jpeg')
            return response
        except Movie.DoesNotExist:
            raise Http404

class EmailTest(APIView):
    def get(self, request):
        try:
            send_mail(
                "Test",
                "Testing email for confirmation \n"
                "testing 123 testing 123",
                settings.EMAIL_HOST_USER,
                ["ishaansangwan@gmail.com"],
                fail_silently=False,
                )
            return HttpResponse("hello")
        except Exception as e:
            print(e)
            raise Http404

class Filter(APIView):
    def post(self,request):
        try:
            data = request.data.copy()
            print(data["name"])
            queryset = Movie.objects.annotate(search=SearchVector("name")).filter(search=data['name'])
            serializer = MoviesSerializer(queryset,many=True)
            # print(serializer.data)
            return Response(serializer.data)
        except Exception as e:
            print(e)
            return HttpResponseBadRequest()