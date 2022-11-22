from django.contrib import admin

from .models import Fixture, Result

admin.site.register(Fixture)
admin.site.register(Result)