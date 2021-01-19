from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class userProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    is_organizer=models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Student(models.Model):
   firstname = models.CharField(max_length=120, verbose_name='Имя')
   lastname = models.CharField(max_length=120, verbose_name='Фамилия')
   group = models.CharField(max_length=120, verbose_name='Группа')
   mark = models.ManyToManyField('Mark', verbose_name='Оценка', through='MarkOfStudent',
                                  related_name='student_mark')
   def __str__(self):
       return self.lastname

class Teacher(models.Model):
   firstname = models.CharField(max_length=120, verbose_name='Имя')
   lastname = models.CharField(max_length=120, verbose_name='Фамилия')
   room = models.IntegerField(verbose_name='кабинет', default=0)
   discipline = models.ManyToManyField('Discipline', verbose_name='Дисциплина', through='DisciplineOfTeacher',
                                  related_name='teacher_discipline')
   def __str__(self):
       return self.lastname

class Discipline(models.Model):
   title = models.CharField(max_length=120, verbose_name='Название')
   def __str__(self):
       return self.title


class DisciplineOfTeacher(models.Model):
    discipline = models.ForeignKey('Discipline', verbose_name='Дисциплина', on_delete=models.CASCADE)
    teacher = models.ForeignKey('Teacher', verbose_name='Учитель', on_delete=models.CASCADE)
    def __str__(self):
        return '{} {}'.format(self.discipline.title, self.teacher.lastname)



class Mark(models.Model):
    teacher = models.ForeignKey('Teacher', verbose_name='Учитель', on_delete=models.CASCADE)
    mark = models.IntegerField(verbose_name='Оценка')
    def str(self):
       return self.mark

class MarkOfStudent(models.Model):
    mark = models.ForeignKey('Mark', verbose_name='Оценка', on_delete=models.CASCADE)
    student = models.ForeignKey('Student', verbose_name='Студент', on_delete=models.CASCADE)
    def __str__(self):
        return '{} {}'.format(self.mark.mark, self.mark.student.lastname)

class Pair(models.Model):
    days = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    )
    day = models.CharField(max_length=10, choices=days, verbose_name='День')
    time = models.CharField(max_length=120, verbose_name='Время')
    group = models.CharField(max_length=120, verbose_name='Группа')
    discipline = models.ForeignKey('DisciplineOfTeacher', verbose_name='Дисциплина', on_delete=models.CASCADE)

    def __str__(self):
       return self.discipline.discipline.title

class Schedule(models.Model):
    group = models.CharField(max_length=120, verbose_name='Группа')
    pair = models.ManyToManyField('Pair', verbose_name='Пара', through='PairOfSchedule',
                                  related_name='schedule_pair')

class PairOfSchedule(models.Model):
    pair = models.ForeignKey('Pair', verbose_name='Пара', on_delete=models.CASCADE)
    schedule = models.ForeignKey('Schedule', verbose_name='Расписание', on_delete=models.CASCADE)