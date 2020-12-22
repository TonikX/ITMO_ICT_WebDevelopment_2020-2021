from django.db import models
from django.db.models.query import QuerySet
from django.utils import timezone


class EventQuerySet(QuerySet):
    def is_live(self):
        now = timezone.now()
        return self.filter(start_date__lt=now, end_date__gt=now).exists()

    def upcoming(self):
        return self.filter(end_date__gt=timezone.now()).earliest('start_date')

    def completed(self):
        return self.filter(end_date__lt=timezone.now()).order_by('-start_date')


class Event(models.Model):
    PHYSICAL = 'physical'
    MEETING = 'meeting'
    CATEGORY = (
        (PHYSICAL, 'Физическое'),
        (MEETING, 'Встреча'),
    )
    title = models.CharField("Название", max_length=100)
    description = models.CharField("Описание конференции",
                                   max_length=250,
                                   blank=True)
    start_date = models.DateTimeField("Дата начала")
    end_date = models.DateTimeField("Дата окончания")
    category = models.CharField("Категория мерпориятия",
                                max_length=14,
                                choices=CATEGORY,
                                default=PHYSICAL)

    objects = EventQuerySet.as_manager()

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"

    def __str__(self):
        return f"{self.category} - {self.title}"
