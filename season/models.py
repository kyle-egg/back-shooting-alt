from django.db import models

class Season(models.Model):
    name = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return f'{self.year}'


class League(models.Model):
    season = models.ForeignKey(
        Season,
        related_name='leagues',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200)
    team = models.ManyToManyField(
        'club.Team',
        related_name='league',
        blank=True
    )

    def __str__(self):
        return f'{self.season} - {self.name}'
