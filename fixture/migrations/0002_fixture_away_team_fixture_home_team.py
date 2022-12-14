# Generated by Django 4.1.3 on 2022-11-20 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0004_team_is_active'),
        ('fixture', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fixture',
            name='away_team',
            field=models.ManyToManyField(blank=True, related_name='away_matches', to='club.team'),
        ),
        migrations.AddField(
            model_name='fixture',
            name='home_team',
            field=models.ManyToManyField(blank=True, related_name='home_matches', to='club.team'),
        ),
    ]
