from django.urls import path
from .views import (
  SeasonListView,
  SeasonDetailView,
  LeagueListView,
  LeagueAllView,
  LeagueDetailView
  
)

urlpatterns = [
    path('', SeasonListView.as_view()),
    path('<int:pk>/', SeasonDetailView.as_view()),
    path('<int:season_pk>/leagues/', LeagueListView.as_view()),
    path('leagues/', LeagueAllView.as_view()),
    path('<int:season_pk>/leagues/<int:pk>', LeagueDetailView.as_view()),
]
