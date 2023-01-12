from django.db import models
from django.core.validators import MaxValueValidator


class Fixture(models.Model):
    name = models.CharField(max_length=100, null=True)
    season = models.ManyToManyField(
        'season.Season',
        related_name='seasons',
        blank=True
    )
    league = models.ManyToManyField(
        'season.League',
        related_name='leagues',
        blank=True
    )
    date = models.DateField(blank=True)
    time = models.TimeField(blank=True)
    home_team = models.ManyToManyField(
        'club.Team',
        related_name='home_fixture',
        blank=True
    )
    away_team = models.ManyToManyField(
        'club.Team',
        related_name='away_fixture',
        blank=True
    )
    home_total_score = models.PositiveIntegerField(default=0, null=True)
    away_total_score = models.PositiveIntegerField(default=0, null=True)
    
    def __str__(self):
        return f'{self.date} - {self.name}'
    
class Result(models.Model):
    player_name = models.CharField(max_length=50, blank=True)
    player_id = models.PositiveIntegerField(default=0, blank=True)
    player = models.ManyToManyField(
        'player.Player',
        related_name='score',
        blank=True
    )
    shot_one = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)], null=True)
    shot_two = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)], null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    fixture = models.ForeignKey(
        Fixture,
        related_name='results',
        on_delete=models.CASCADE,
        blank=True
    )
    team = models.ForeignKey(
        'jwt_auth.User',
        related_name='team_results',
        on_delete=models.CASCADE,
        blank=True
    )
    
    def __str__(self):
        return f'{self.fixture} - {self.team} - {self.player_name} [{self.shot_one}][{self.shot_two}]'