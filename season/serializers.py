from rest_framework import serializers

from .models import Season, League
from club.models import Team

class NestedTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class LeagueSerializer(serializers.ModelSerializer):
    team = NestedTeamSerializer(many=True, read_only=True)

    class Meta:
        model = League
        fields = '__all__'

class SeasonSerializer(serializers.ModelSerializer):
    leagues = LeagueSerializer(many=True, read_only=True)
    
    class Meta:
        model = Season
        fields = '__all__'

