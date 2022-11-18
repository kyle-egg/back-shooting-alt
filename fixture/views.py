from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)

from .models import Fixture
from .serializers import FixtureSerializer

class FixtureListView(ListCreateAPIView):
    ''' List View for /match GET'''
    queryset = Fixture.objects.all()
    serializer_class = FixtureSerializer

class FixtureDetailView(RetrieveUpdateDestroyAPIView):
    ''' Detail View for /match/id SHOW UPDATE DELETE'''
    queryset = Fixture.objects.all()
    serializer_class = FixtureSerializer

