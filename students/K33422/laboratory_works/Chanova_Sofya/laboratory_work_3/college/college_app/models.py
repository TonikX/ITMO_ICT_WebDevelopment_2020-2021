from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    roles = (
        ('a', 'admin'),
        ('d', 'dispatcher'),
        ('s', 'student'),
        ('t', 'teacher'),
    )

    role = models.CharField(choices=roles, max_length=1)

    student_group = models.ForeignKey('StudentGroup', on_delete=models.CASCADE, blank=True, null=True)
    student_sem_grade = models.ManyToManyField('Teaching', through='SemesterGrade', related_name='semester_grade')

    teacher_qualification = models.CharField(max_length=40, blank=True, null=True)
    teacher_subject = models.ManyToManyField('Subject', through='Teaching', related_name='subject_taught')

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'role']

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class StudentGroup(models.Model):

    group_number = models.CharField(max_length=10)
    course_number = models.IntegerField()
    department = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.group_number


class Subject(models.Model):

    subject_name = models.CharField(max_length=50)
    types = (
        ('p', 'pass'),
        ('e', 'exam')
    )
    control_type = models.CharField(choices=types, max_length=1)
    academic_hours = models.IntegerField(default=36)
    description = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.subject_name


class Room(models.Model):

    room_number = models.IntegerField(unique=True)
    seats_quantity = models.IntegerField()
    themes = (
        ('chl', 'chemistry lab'),
        ('cc', 'computer class'),
        ('h', 'hall'),
        ('phl', 'physics lab'),
        ('n', 'none')
    )
    subject_theme = models.CharField(choices=themes, max_length=3, blank=True, null=True)

    def __str__(self):
        return str(self.room_number)


class ScheduleEntry(models.Model):

    lessons = (
        ('0', '8:20'),
        ('1', '10:00'),
        ('2', '11:40'),
        ('3', '13:30'),
        ('4', '15:20'),
        ('5', '17:00'),
        ('6', '18:40')
    )
    weekdays = (
        ('0', 'Monday'),
        ('1', 'Tuesday'),
        ('2', 'Wednesday'),
        ('3', 'Thursday'),
        ('4', 'Friday'),
        ('5', 'Saturday'),
        ('6', 'Sunday')
    )

    weekday = models.CharField(max_length=1, choices=weekdays)
    time = models.CharField(max_length=1, choices=lessons)
    room_number = models.ForeignKey('Room', on_delete=models.CASCADE, blank=True, null=True, related_name='room')
    group_number = models.ForeignKey('StudentGroup', on_delete=models.CASCADE,
                                     blank=True, null=True, related_name='group')
    teacher = models.ForeignKey('User', on_delete=models.CASCADE, blank=True, null=True,
                                related_name='teacher', limit_choices_to={'role': 't'})
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, blank=True, null=True, related_name='subject')

    def __str__(self):
        return "{} {} - {} - {}".format(self.get_weekday_display(),
                                        self.get_time_display(), self.subject, self.group_number)


class Teaching(models.Model):

    teacher = models.ForeignKey('User', on_delete=models.CASCADE, blank=True, null=True)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return "{} ({})".format(str(self.subject), str(self.teacher))


class SemesterGrade(models.Model):

    student = models.ForeignKey('User', on_delete=models.CASCADE, blank=True, null=True)
    teaching = models.ForeignKey('Teaching', on_delete=models.CASCADE, blank=True, null=True)

    grades = (
        ('A', 'excellent'),
        ('B', 'good'),
        ('C', 'satisfactory'),
        ('D', 'marginal'),
        ('F', 'failure')
    )

    grade = models.CharField(max_length=1, choices=grades)

    def __str__(self):
        return "{} - {}".format(self.teaching, self.grade)
