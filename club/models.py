from django.db import models

class Club(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(max_length=500, blank=True)
    logo = models.CharField(max_length=500)
    website = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    address = models.TextField(max_length=500, blank=True)
    maps = models.CharField(max_length=500, blank=True)
    players = models.ManyToManyField(
        'player.Player',
        related_name='club_players',
        blank=True
    )

    def __str__(self):
        return f'{self.name}'

class Team(models.Model):
    name = models.CharField(max_length=100)
    logo = models.CharField(max_length=500, blank=True)
    club = models.ForeignKey(
        Club,
        related_name='teams',
        on_delete=models.CASCADE
    )
    players = models.ManyToManyField(
        'player.Player',
        related_name='team_players',
        blank=True
    )
    owner = models.ForeignKey(
        'jwt_auth.User',
        related_name='owner',
        on_delete=models.CASCADE
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'