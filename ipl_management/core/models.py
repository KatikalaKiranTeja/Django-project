from django.db import models

# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=100)
    coach = models.CharField(max_length=100)
    home_ground = models.CharField(max_length=100)

class Player(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

class Match(models.Model):
    team1 = models.ForeignKey(Team, related_name='team1', on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, related_name='team2', on_delete=models.CASCADE)
    match_date = models.DateField()
    venue = models.CharField(max_length=100)
    winner = models.ForeignKey(Team, related_name='winner', on_delete=models.CASCADE)

class PointsTable(models.Model):
    team = models.OneToOneField(Team, on_delete=models.CASCADE)
    matches_played = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    points = models.IntegerField(default=0)