from django.shortcuts import render
from rest_framework.views import APIView , Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticated


from .models import User
from .serializers import UserSerializer
from .utils import GetUserId

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


# Create your views here.


class Signup(APIView):
    def post(self, request):
        data = request.data.copy()
        if "password" in data:
            print(data['password'])
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)



