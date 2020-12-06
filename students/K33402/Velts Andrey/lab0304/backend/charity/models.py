from django.db import models
from django.core.validators import MaxValueValidator
from .utils import path_and_rename


class Charity(models.Model):
    title = models.CharField("Название", max_length=40)
    description = models.CharField("Описание сбора", max_length=300)
    goal_money = models.PositiveIntegerField(
        "Цель сбора", validators=[MaxValueValidator(1000000)], default=0
    )
    current_money = models.PositiveIntegerField(
        "Собрано денег", validators=[MaxValueValidator(1000000)], default=0
    )
    donation_times = models.PositiveIntegerField(
        "Число пожертвований", validators=[MaxValueValidator(100000)], default=0
    )
    image = models.ImageField(
        "Изображение",
        upload_to=path_and_rename,
        default="avatar/default.png",
    )

    class Meta:
        verbose_name = "Пожертвование"
        verbose_name_plural = "Пожертвования"

    def __str__(self):
        return f"{self.title} - {self.current_money}/{self.goal_money} руб."
