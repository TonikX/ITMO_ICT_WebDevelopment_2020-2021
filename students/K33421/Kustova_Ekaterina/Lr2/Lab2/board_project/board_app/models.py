
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class Participant(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    experience = models.CharField(max_length=30)
    team = models.ForeignKey('Team', on_delete=models.SET_NULL, null=True)
    car = models.CharField(max_length=20)
    def __str__(self):
        return self.username

class Team(models.Model):
    team_name = models.CharField(max_length=30)
    def __str__(self):
        return self.team_name


class Race(models.Model):
    race_name = models.CharField(max_length=30)
    race_date = models.DateField()
    def __str__(self):
        return self.race_name

class Race_Registration(models.Model):
    race = models.ForeignKey('Race', on_delete=models.CASCADE)
    participant = models.ForeignKey('Participant', on_delete=models.CASCADE)
    def __str__(self):
        return self.participant

class Win(models.Model):
    race = models.ForeignKey('Race', on_delete=models.CASCADE)
    winner = models.ForeignKey('Race_Registration', on_delete=models.CASCADE)


class Comment(models.Model):
    user = models.ForeignKey('Participant', on_delete=models.SET_NULL, null=True)
    race = models.ForeignKey('Race', on_delete=models.CASCADE)

    class CommentType(models.IntegerChoices):
        partnership = 1
        race_question = 2
        other = 3
    comment_type = models.IntegerField(choices=CommentType.choices, null=True)
    class Rating(models.IntegerChoices):
        disgusted = 1
        very_unsatisfied = 2
        unsatisfied = 3
        below_neutral = 4
        neutral = 5
        above_neutral = 6
        satisfied = 7
        very_satisfied = 8
        amazed = 9
        best_of_the_best = 10

    rating_list = models.IntegerField(choices=Rating.choices, null=True)
    comment = models.CharField(max_length=3000)
