# Generated by Django 4.1.7 on 2023-08-19 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0016_wallet_wallet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trans',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='league.gameselect'),
        ),
    ]