from django.contrib import admin
from .models import Season, League

admin.site.register(Season)

class LeagueAdmin(admin.ModelAdmin):
    list_display = ("name", "season")

admin.site.register(League, LeagueAdmin)