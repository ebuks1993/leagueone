from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import gameSerializer
from .models import games
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class gameViewset(ModelViewSet):
    queryset=games.objects.all()
    serializer_class=gameSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['Date']