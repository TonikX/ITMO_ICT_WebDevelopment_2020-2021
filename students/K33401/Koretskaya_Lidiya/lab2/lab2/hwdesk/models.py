from django.db import models
from django.contrib.auth.models import AbstractUser


subject_choices = [
    ('Математические', (
        ('Алгебра', 'Алгебра'),
        ('Геометрия', 'Геометрия'),
        ('Математика', 'Математика'),
        ('Информатика', 'Информатика'),
        )
     ),
    ('Гуманитарные', (
        ('История', 'История'),
        ('Обществознание', 'Обществознание'),
        )
     ),
    ('Естественно-научные', (
        ('Физика', 'Физика'),
        ('Химия', 'Химия'),
        ('География', 'География'),
        ('Астрономия', 'Астрономия'),
        ('Биология', 'Биология'),
        ('ОБЖ', 'ОБЖ'),
        ('Экология', 'Экология'),
        )
     ),
    ('Филологические', (
        ('Русский язык', 'Русский язык'),
        ('Литература', 'Литература'),
        ('Иностранный язык', 'Иностранный язык'),
        )
     ),
    ('Искусство', (
        ('Музыка', 'Музыка'),
        ('ИЗО', 'ИЗО'),
        )
     ),
    ('Физкультура', 'Физкультура'),
]

class_name_choices = [
    ('1', (
        ('1А', '1А'),
        ('1Б', '1Б'),
        ('1В', '1В'),
        ('1Г', '1Г'),
        ('1Д', '1Д'),
        )
     ),
    ('2', (
        ('2А', '2А'),
        ('2Б', '2Б'),
        ('2В', '2В'),
        ('2Г', '2Г'),
        ('2Д', '2Д'),
        )
     ),
    ('3', (
        ('3А', '3А'),
        ('3Б', '3Б'),
        ('3В', '3В'),
        ('3Г', '3Г'),
        ('3Д', '3Д'),
    )
     ),
    ('4', (
        ('4А', '4А'),
        ('4Б', '4Б'),
        ('4В', '4В'),
        ('4Г', '4Г'),
        ('4Д', '4Д'),
        )
     ),
    ('5', (
        ('5А', '5А'),
        ('5Б', '5Б'),
        ('5В', '5В'),
        ('5Г', '5Г'),
        )
     ),
    ('6', (
        ('6А', '6А'),
        ('6Б', '6Б'),
        ('6В', '6В'),
        ('6Г', '6Г'),
        )
     ),
    ('7', (
        ('7А', '7А'),
        ('7Б', '7Б'),
        ('7В', '7В'),
        ('7Г', '7Г'),
        )
     ),
    ('8', (
        ('8А', '8А'),
        ('8Б', '8Б'),
        ('8В', '8В'),
        ('8Г', '8Г'),
        )
     ),
    ('9', (
        ('9А', '9А'),
        ('9Б', '9Б'),
        ('9В', '9В'),
        ('9Г', '9Г'),
        )
     ),
    ('10', (
        ('10.1', '10.1'),
        ('10.2', '10.2'),
        ('10.3', '10.3'),
        )
     ),
    ('11', (
        ('11.1', '11.1'),
        ('11.2', '11.2'),
        ('11.3', '11.3'),
        )
     ),
]
class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    subject = models.CharField(max_length=50, choices=subject_choices)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

class Pupil(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    class_name = models.CharField(max_length=10, choices=class_name_choices)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Task(models.Model):
    class_name = models.CharField(max_length=10, choices=class_name_choices)
    subject = models.CharField(max_length=50, choices=subject_choices)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    date_of_publication = models.DateField()
    deadline = models.DateField()
    task_text = models.TextField(max_length=10000)
    fines_info = models.TextField(max_length=1000)

    def __str__(self):
        return '{} {} {}'.format(self.class_name, self.subject, self.date_of_publication)


class LoadTask(models.Model):
    pupil = models.ForeignKey(Pupil, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    decision = models.TextField(max_length=10000)

    def __str__(self):
        return '{} - {} {}'.format(self.pupil, self.task.subject, self.task.date_of_publication)


class CheckTask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    pupil = models.ForeignKey(Pupil, on_delete=models.CASCADE)
    mark = models.CharField(max_length=2)
    comment = models.TextField(max_length=100)


    def __str__(self):
        return '{} - {} {}'.format(self.pupil, self.task.subject, self.task.date_of_publication)


class CustomUser(AbstractUser):
    type_choices = [
        ('teacher', 'учитель'),
        ('pupil', 'ученик'),
    ]
    type = models.CharField(max_length=10, choices=type_choices)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

