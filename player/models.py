from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=100, unique=False)
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.CharField(max_length=500, blank=True)
    is_active = models.BooleanField(default=True)
    title = models.CharField(max_length=100, blank=True)
    honours = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return f'{self.name}'