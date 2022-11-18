from django.db import models

class Fixture(models.Model):
    name = models.CharField(max_length=100, null=True)
    date = models.DateField()
    time = models.TimeField()
    def __str__(self):
        return f'{self.date} - {self.name}'