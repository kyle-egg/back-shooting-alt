from django.urls import path
from .views import RegisterView, LoginView, TeamView, TeamDetailView, PlayerListView, PlayerDetailView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('team/', TeamView.as_view()),
    path('team/<int:pk>/', TeamDetailView.as_view()),
    path('player/', PlayerListView.as_view()),
    path('player/<int:pk>/', PlayerDetailView.as_view()),
]
