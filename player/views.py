from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)

from .models import Player
from .serializers import PlayerSerializer

class PlayerListView(ListCreateAPIView):
    ''' List View for /teams GET'''
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class PlayerDetailView(RetrieveUpdateDestroyAPIView):
    ''' Detail View for /teams/id SHOW UPDATE DELETE'''
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
