from django.db import models


class Club(models.Model):
    name = models.CharField(max_length=50, unique=True)
    country = models.CharField(max_length=56)
    contact_person = models.CharField(max_length=60)
    e_mail = models.EmailField(max_length=60)
    phone_number = models.DecimalField(max_digits=15, decimal_places=0)

    def __str__(self):
        return self.name


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    club = models.ForeignKey(
        Club, on_delete=models.CASCADE, related_name='members')

    def __str__(self):
        return '{} {}, id={}'.format(self.first_name, self.last_name, self.id)


class Peak(models.Model):
    name = models.CharField(max_length=80, unique=True)
    country = models.CharField(max_length=56)
    height = models.DecimalField(max_digits=5, decimal_places=0)
    climbing_duration = models.DecimalField(max_digits=5, decimal_places=0)
    route_description = models.TextField()

    def __str__(self):
        return self.name


class Climbing(models.Model):
    start_time = models.DateTimeField()
    finish_time = models.DateTimeField(null=True)
    peak = models.ForeignKey(
        Peak, on_delete=models.CASCADE, related_name='climbings')
    participants = models.ManyToManyField(
        Person, through='Participation', related_name='climbings')
    information = models.TextField(blank=True)

    def __str__(self):
        return '{}. From {} to {}'.format(self.peak.name, self.start_time, self.finish_time)


# не уверена, нужны ли отдельные нештатные ситуации
# вероятно, можно было обойтись полем "результат" у участия


class Participation(models.Model):
    participant = models.ForeignKey(
        Person, on_delete=models.CASCADE, related_name='groups')
    climbing = models.ForeignKey(Climbing, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('participant', 'climbing')


class EmergencySituation(models.Model):
    # чтобы был смысл существования этих эмердженсис эз дифферент класс,
    # сделаю возможным делать много этих ситуций для пары альпинист-восхождение
    # не юник тугезе
    climbing = models.ForeignKey(
        Climbing, on_delete=models.CASCADE, related_name='emergencies')
    person = models.ForeignKey(
        Person, on_delete=models.CASCADE, related_name='emergencies')
    description = models.TextField()
