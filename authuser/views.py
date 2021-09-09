from django.shortcuts import render
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, generics
from .serializers import UserSerializer


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
