from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)

from .models import Fixture, Result
from .serializers import FixtureSerializer, ResultSerializer

class FixtureListView(ListCreateAPIView):
    ''' List View for /match GET'''
    queryset = Fixture.objects.all()
    serializer_class = FixtureSerializer

class FixtureDetailView(RetrieveUpdateDestroyAPIView):
    ''' Detail View for /match/id SHOW UPDATE DELETE'''
    queryset = Fixture.objects.all()
    serializer_class = FixtureSerializer

class ResultListView(ListCreateAPIView):
    ''' List View for /result GET'''
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

class ResultDetailView(RetrieveUpdateDestroyAPIView):
    ''' Detail View for /result/id SHOW UPDATE DELETE'''
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

