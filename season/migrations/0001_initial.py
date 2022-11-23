# Generated by Django 4.1.3 on 2022-11-21 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('club', '0004_team_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveIntegerField(max_length=4, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leagues', to='season.season')),
                ('team', models.ManyToManyField(blank=True, related_name='league', to='club.team')),
            ],
        ),
    ]