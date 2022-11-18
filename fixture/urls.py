from django.urls import path
from .views import (
    FixtureListView,
    FixtureDetailView
)

urlpatterns = [
    path('', FixtureListView.as_view()),
    path('<int:pk>/', FixtureDetailView.as_view()),
]
