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

    def __str__(self):
        return f'{self.name}'