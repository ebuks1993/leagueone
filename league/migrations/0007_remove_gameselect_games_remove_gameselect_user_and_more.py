# Generated by Django 4.1.7 on 2023-05-14 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0006_games_pitch_sport_gameselect_games_pitch_games_sport'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gameselect',
            name='games',
        ),
        migrations.RemoveField(
            model_name='gameselect',
            name='user',
        ),
        migrations.DeleteModel(
            name='Games',
        ),
        migrations.DeleteModel(
            name='GameSelect',
        ),
        migrations.DeleteModel(
            name='Pitch',
        ),
        migrations.DeleteModel(
            name='Sport',
        ),
    ]
