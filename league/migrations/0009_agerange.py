# Generated by Django 4.1.7 on 2023-05-14 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0008_games_pitch_sport_gameselect_games_pitch_games_sport'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agerange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AgeGrade', models.CharField(max_length=1500)),
            ],
        ),
    ]
