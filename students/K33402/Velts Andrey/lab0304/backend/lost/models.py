from django.db import models
from .utils import path_and_rename


class Lost(models.Model):
    MALE = "Мальчик"
    FEMALE = "Девочка"
    CATEGORY = (
        (MALE, "Мальчик"),
        (FEMALE, "Девочка"),
    )
    name = models.CharField("Кличка", max_length=40)
    age = models.CharField("Возраст", max_length=20)
    gender = models.CharField("Пол", max_length=14, choices=CATEGORY, default=MALE)
    city = models.CharField("Город", max_length=30)
    description = models.CharField("Описание", max_length=300, blank=True, null=True)
    location = models.CharField("Место", max_length=40, blank=True, null=True)
    contacts = models.CharField("Контакты", max_length=60, blank=True, null=True)
    image = models.ImageField(
        "Изображение",
        upload_to=path_and_rename,
        default="lost/default.png",
    )

    class Meta:
        verbose_name = "Потерянный питомец"
        verbose_name_plural = "Потерянные питомцы"

    def __str__(self):
        return f"{self.name} / {self.age} - г. {self.city}"
