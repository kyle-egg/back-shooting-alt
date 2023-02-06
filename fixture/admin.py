from django.contrib import admin

from .models import Fixture, Result

class FixtureAdmin(admin.ModelAdmin):
    list_display = ("name", "date")

admin.site.register(Fixture, FixtureAdmin)

class ResultAdmin(admin.ModelAdmin):
    list_display = ("player_name", "fixture", "shot_one", "shot_two")

admin.site.register(Result, ResultAdmin)