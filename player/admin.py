from django.contrib import admin
from .models import Player

class PlayerAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active")

admin.site.register(Player, PlayerAdmin)