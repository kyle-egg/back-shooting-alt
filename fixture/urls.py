from django.urls import path
from .views import (
    FixtureListView,
    FixtureDetailView,
    ResultListView,
    ResultDetailView
)

urlpatterns = [
    path('', FixtureListView.as_view()),
    path('<int:pk>/', FixtureDetailView.as_view()),
    path('<int:fixture_pk>/results/', ResultListView.as_view()),
    path('<int:fixture_pk>/results/<int:pk>/', ResultDetailView.as_view())
]
