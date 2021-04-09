from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Conference(models.Model):
    SCIENCE = 'Наука'
    MEDICINE = 'Медицина'
    SPORT = 'Спорт'
    TOPICS = [
        (SCIENCE, 'Наука'),
        (MEDICINE, 'Медицина'),
        (SPORT, 'Спорт')
    ]

    name = models.CharField('Конференция', max_length=64)
    topic = models.CharField('Тема', blank=True, choices=TOPICS, max_length=10)
    location = models.CharField('Место', max_length=64)
    start_date = models.DateField("Начало")
    end_date = models.DateField("Окончание")
    description = models.CharField("Описание конференции", max_length=512)
    location_desc = models.CharField("Описание места", max_length=512)
    terms = models.CharField("Условия участия", max_length=256)

    class Meta:
        verbose_name = 'Конференция'
        verbose_name_plural = 'Конференции'

    def __str__(self):
        return  f'{self.name} - {self.topic}'


class Comment(models.Model):
    JOIN = 'Принять участие'
    POST = 'Опубликовать доклад'
    LOCATION = 'Место проведения'
    OTHER = 'Другое'
    TOPIC_CHOICES = [
        (JOIN, 'Принять участие'),
        (POST, 'Опубликовать доклад'),
        (LOCATION, 'Место проведения'),
        (OTHER, 'Другое')
    ]

    conference = models.ForeignKey(Conference, on_delete=models.CASCADE, verbose_name='Конференция')
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец комментария')
    comment_type = models.CharField('Тип комментария', blank=True, choices=TOPIC_CHOICES, max_length=64)
    comment_text = models.CharField('Текст комментария', max_length=512)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.comment_author} - {self.comment_type}'
