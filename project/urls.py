from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/matches/', include('fixture.urls')),
    path('api/player/', include('jwt_auth.urls')),
    path('api/teams/', include('club.urls'))
]
