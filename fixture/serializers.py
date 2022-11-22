from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Fixture, Result
from club.models import Team
User = get_user_model()
from player.models import Player
from season.models import League, Season

class NestedLeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = '__all__'

class NestedSeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = '__all__'

class NestedPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

class NestedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'team')

class NestedTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class ResultSerializer(serializers.ModelSerializer):
  player = NestedPlayerSerializer(many=True, read_only=True)

  class Meta:
        model = Result
        fields = '__all__'

class PopulatedResultSerializer(ResultSerializer):
    team = NestedUserSerializer()


class FixtureSerializer(serializers.ModelSerializer):
  home_team = NestedTeamSerializer(many=True, read_only=True)
  away_team = NestedTeamSerializer(many=True, read_only=True)
  results = PopulatedResultSerializer(many=True, read_only=True)
  league = NestedLeagueSerializer(many=True, read_only=True)  
  season = NestedSeasonSerializer(many=True, read_only=True) 
  
  class Meta:
        model = Fixture
        fields = '__all__'
