from django.db import models

class Room(models.Model):
    def status_default(self):
        return {"status": "free"}

    typeRoom = [
        ('one', 'одноместный'),
        ('two', 'двухместный'),
        ('three', 'трехместный'),
    ]
    statusRoom = [
        ('free', 'свободен'),
        ('busy', 'занят')
    ]
    number = models.IntegerField()
    type = models.CharField(max_length=15, choices=typeRoom)
    price = models.IntegerField(verbose_name=u"Price per day")
    phone = models.CharField(max_length=20)
    status = models.CharField(max_length=15, choices=statusRoom)
    total = models.IntegerField(verbose_name=u"Total income")

    def __str__(self):
        return '№{}, {} {}$ {}, id: {}'.format(self.number, self.type, self.price, self.status, self.id)

class Guest(models.Model):
    passport = models.IntegerField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    start_date = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE, limit_choices_to={'status': 'free'})

    def __str__(self):
        return '{} {} {}'.format(self.first_name, self.last_name, self.room)

class Staff(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    cleaning = models.ManyToManyField('CleaningParams', through='StaffCleaning')

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class CleaningParams(models.Model):
    day_choices = [
        ('mon', 'Понедельник'),
        ('tue', 'Вторник'),
        ('wed', 'Среда'),
        ('thu', 'Четверг'),
        ('fri', 'Пятница'),
        ('sat', 'Суббота'),
        ('sun', 'Воскресенье'),
    ]
    day = models.CharField(max_length=30, choices=day_choices)
    floor = models.IntegerField()

    def __str__(self):
        return '{} {}'.format(self.day, self.floor)


class StaffCleaning(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    params = models.ForeignKey(CleaningParams, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.staff, self.params)
