from django.db import models


class Item(models.Model):
    BIKEPART = "Запчасть"
    BIKE = "Велосипед"
    CLOTHES = "Одежда"
    CATEGORY = (
        (BIKEPART, "Запчасть"),
        (BIKE, "Велосипед"),
        (CLOTHES, "Одежда"),
    )
    name = models.CharField("Название", max_length=40)
    type = models.CharField("Тип", max_length=14, choices=CATEGORY, default=BIKEPART)
    description = models.TextField("Описание", max_length=200)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return f"{self.name}"
