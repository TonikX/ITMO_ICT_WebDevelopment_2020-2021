from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField()
    answers = models.ManyToManyField('Answer', blank=True, through='UserToAnswer')
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    def __str__(self):
        return "{} {} {} {}".format(self.username, self.first_name, self.last_name, self.email)


class Question(models.Model):
    description = models.CharField(max_length=100)
    poll = models.ForeignKey('Poll', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.description


class Answer(models.Model):
    description = models.CharField(max_length=100)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.description


class Poll(models.Model):
    title = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=200)
    voting_time = models.IntegerField()
    creator = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    theme = models.CharField(max_length=100)

    def __str__(self):
        return "{} {} {}".format(self.title, self.description, self.create_date)


class UserToAnswer(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    def __str__(self):
        return "User: {}\nAnswer: {}".format(self.user, self.answer)
