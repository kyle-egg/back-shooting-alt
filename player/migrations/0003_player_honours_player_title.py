# Generated by Django 4.1.3 on 2022-11-20 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0002_player_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='honours',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='player',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]