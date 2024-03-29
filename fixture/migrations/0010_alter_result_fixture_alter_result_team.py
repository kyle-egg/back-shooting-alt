# Generated by Django 4.1.3 on 2023-01-28 17:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fixture', '0009_alter_fixture_date_alter_fixture_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='fixture',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='results', to='fixture.fixture'),
        ),
        migrations.AlterField(
            model_name='result',
            name='team',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_results', to=settings.AUTH_USER_MODEL),
        ),
    ]
