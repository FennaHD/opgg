# Generated by Django 2.2.2 on 2019-06-25 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SummonerStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summoner_name', models.CharField(max_length=50)),
                ('summomer_id', models.CharField(max_length=100)),
                ('summoner_level', models.CharField(max_length=50)),
            ],
        ),
    ]
