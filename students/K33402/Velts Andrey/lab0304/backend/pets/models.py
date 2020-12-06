from django.db import models
from .utils import path_and_rename


class Pet(models.Model):
    MALE = "Мальчик"
    FEMALE = "Девочка"
    CATEGORY = (
        (MALE, "Мальчик"),
        (FEMALE, "Девочка"),
    )
    name = models.CharField("Кличка", max_length=40)
    age = models.CharField("Возраст", max_length=20)
    gender = models.CharField("Пол", max_length=14, choices=CATEGORY, default=MALE)
    image = models.ImageField(
        "Изображение",
        upload_to=path_and_rename,
        default="avatar/default.png",
    )

    class Meta:
        verbose_name = "Питомец"
        verbose_name_plural = "Питомцы"

    def __str__(self):
        return f"{self.name} - {self.age}"
