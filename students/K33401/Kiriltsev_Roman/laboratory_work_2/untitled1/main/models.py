from django.db import models
from django.contrib.auth.models import User


class Conference(models.Model):
    SCIENCE = "Наука"
    MEDICINE = "Медицина"
    SPORT = "Спорт"
    TOPIC_CHOICES = [
        (SCIENCE, "Наука"),
        (MEDICINE, "Медицина"),
        (SPORT, "Спорт"),
    ]
    name = models.CharField("Конференция", max_length=80)
    topic = models.CharField("Тема", blank=True, choices=TOPIC_CHOICES, max_length=10)
    location = models.CharField("Место проведения", max_length=80)
    start_date = models.DateField("Начало конференции")
    end_date = models.DateField("Окончание конференции")
    description = models.CharField("Описание конференции", max_length=500)
    location_extra = models.CharField("Описание места проведения", max_length=500)
    terms = models.CharField("Условия участия", max_length=300)

    class Meta:
        verbose_name = "Конференция"
        verbose_name_plural = "Конференции"

    def __str__(self):
        return f"{self.name} - {self.topic}"


class Comment(models.Model):
    JOIN = "Принять участие"
    POST = "Опубликовать доклад"
    LOCATION = "Место проведения"
    DIFFERENT = "Другое"
    TOPIC_CHOICES = [
        (JOIN, "Принять участие"),
        (POST, "Опубликовать доклад"),
        (LOCATION, "Место проведения"),
        (DIFFERENT, "Другое"),
    ]
    conference = models.ForeignKey(
        Conference, on_delete=models.CASCADE, verbose_name="Конференция"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Автор комментария"
    )
    topic = models.CharField(
        "Тип комментария", blank=True, choices=TOPIC_CHOICES, max_length=50
    )
    text = models.CharField("Текст комментария", max_length=300)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return f"{self.author} - {self.topic}"