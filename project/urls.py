from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/matches/', include('fixture.urls')),
    path('api/profile/', include('jwt_auth.urls')),
    path('api/clubs/', include('club.urls')),
    path('api/players/', include('player.urls'))
]
