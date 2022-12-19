from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import Fixture, Result
from .serializers import FixtureSerializer, ResultSerializer

class FixtureListView(ListCreateAPIView):
    ''' List View for /match GET'''
    queryset = Fixture.objects.all()
    serializer_class = FixtureSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class FixtureDetailView(RetrieveUpdateDestroyAPIView):
    ''' Detail View for /match/id SHOW UPDATE DELETE'''
    queryset = Fixture.objects.all()
    serializer_class = FixtureSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class ResultListView(APIView):
    ''' List View for /fixtures/fixtureId/results CREATE fixturess'''

    permission_classes = (IsAuthenticated, )

    def post(self, request, fixture_pk):
        request.data['fixture'] = fixture_pk
        request.data['team'] = request.user.id
        created_result = ResultSerializer(data=request.data)
        if created_result.is_valid():
            created_result.save()
            return Response(created_result.data, status=status.HTTP_201_CREATED)
        return Response(created_result.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class ResultDetailView(RetrieveUpdateDestroyAPIView):
    ''' DELETE COMMENT VIEW '''

    permission_classes = (IsAuthenticated, )

    def delete(self, _request, **kwargs):
        result_pk = kwargs['result_pk']
        try:
            result_to_delete = Result.objects.get(pk=result_pk)
            result_to_delete.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Result.DoesNotExist:
            raise NotFound(detail='Result Not Found')