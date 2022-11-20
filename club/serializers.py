from rest_framework import serializers
from django.contrib.auth import get_user_model
from player.models import Player

from .models import Club, Team
User = get_user_model()

class NestedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('team', 'club')

class NestedPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'
        
class TeamSerializer(serializers.ModelSerializer):
    players = NestedPlayerSerializer(many=True, read_only=True)
    
    class Meta:
        model = Team
        fields = '__all__'

class PopulatedTeamSerializer(TeamSerializer):
    owner = NestedUserSerializer()

class ClubSerializer(serializers.ModelSerializer):
    teams = PopulatedTeamSerializer(many=True, read_only=True)
    owners = NestedUserSerializer(many=True, read_only=True)
    players = NestedPlayerSerializer(many=True, read_only=True)
    
    class Meta:
        model = Club
        fields = '__all__'
