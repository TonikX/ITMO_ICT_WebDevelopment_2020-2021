from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    date_of_birth = models.DateField(blank=True, null=True)
    answers = models.ManyToManyField('Answer', blank=True)

    def __str__(self):
        return "{} {} {} {}".format(self.username, self.name, self.email, self.date_of_birth)


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
