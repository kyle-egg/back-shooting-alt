from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
      team = models.ManyToManyField(
        'club.Team',
        related_name='team',
        blank=True
    )
      club = models.ManyToManyField(
        'club.Club',
        related_name='club',
        blank=True
    )
