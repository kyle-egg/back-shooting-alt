from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)

from .models import Club
from .serializers import ClubSerializer

class ClubListView(ListCreateAPIView):
    ''' List View for /teams GET'''
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

class ClubDetailView(RetrieveUpdateDestroyAPIView):
    ''' Detail View for /teams/id SHOW UPDATE DELETE'''
    queryset = Club.objects.all()
    serializer_class = ClubSerializer