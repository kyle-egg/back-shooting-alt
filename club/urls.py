from django.urls import path
from .views import (
  ClubListView,
  ClubDetailView,
  TeamListView,
  TeamDetailView
)

urlpatterns = [
    path('', ClubListView.as_view()),
    path('<int:pk>/', ClubDetailView.as_view()),
    path('teams/', TeamListView.as_view()),
    path('teams/<int:pk>/', TeamDetailView.as_view()),
]
