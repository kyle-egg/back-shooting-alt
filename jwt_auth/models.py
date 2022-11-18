from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    team_name = models.CharField(max_length=50)
    logo = models.CharField(max_length=500)

class Player(models.Model):
    team = models.ForeignKey(
        User,
        related_name='players',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=50, blank=True)
    honours = models.CharField(max_length=200, blank=True)
    image = models.CharField(max_length=200, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    is_active = models.BooleanField()

    def __str__(self):
        return f'{self.name}'