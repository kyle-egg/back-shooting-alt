from club.serializers import ClubSerializer, TeamSerializer
from rest_framework import serializers
from .models import Player


class PlayerSerializer(serializers.ModelSerializer):
    club_players = ClubSerializer(many=True)
    team_players = TeamSerializer(many=True)

    class Meta:
        model = Player
        fields ='__all__'
