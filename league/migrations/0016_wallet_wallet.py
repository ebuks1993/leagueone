# Generated by Django 4.1.7 on 2023-08-19 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0015_wallet_trans'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallet',
            name='wallet',
            field=models.IntegerField(default=0),
        ),
    ]
