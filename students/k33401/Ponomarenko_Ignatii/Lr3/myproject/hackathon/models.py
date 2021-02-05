from django.db import models
from django.contrib.auth.models import AbstractUser


class Member(AbstractUser):
	# name = models.CharField(max_length=30)
	age = models.IntegerField(default=18)
	is_admin = models.BooleanField(default=False)
	is_curator = models.BooleanField(default=False)


class Team(models.Model):
	captain = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="teams")
	people = models.ManyToManyField(Member)
	title = models.CharField(max_length=20)
	description = models.TextField()


class Jury(models.Model):
	people = models.ManyToManyField(Member)


class Task(models.Model):
	text = models.TextField()
	upload = models.FileField(upload_to='uploads/')


class Comment(models.Model):
	text = models.TextField()
	solution = models.ForeignKey("Solution", on_delete=models.CASCADE)


class Solution(models.Model):
	text = models.TextField()
	task = models.ForeignKey(Task, on_delete=models.CASCADE)
	team = models.ForeignKey(Team, on_delete=models.CASCADE)
	correct = models.BooleanField(default=False)
	date = models.DateTimeField(auto_now_add=True)