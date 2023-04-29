from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import gameSerializer
from .models import games

# Create your views here.

class gameViewset(ModelViewSet):
    queryset=games.objects.all()
    serializer_class=gameSerializer