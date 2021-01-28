from django.db import models

# Create your models here.
class Warrior(models.Model):
    race_types = (
        ("s", "student"),
        ("d", "developer"),
        ("t", "teamlead"),
    )
    race = models.CharField(max_length=1, choices=race_types, verbose_name="Race")
    name = models.CharField(max_length=120, verbose_name="Name")
    level = models.IntegerField(default=0, verbose_name="Level")
    skill = models.ManyToManyField(
        "Skill",
        verbose_name="Skills",
        through="SkillOfWarrior",
        related_name="warrior_skills",
    )
    profession = models.ForeignKey(
        "Profession",
        on_delete=models.CASCADE,
        verbose_name="Profession",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name


class Profession(models.Model):
    title = models.CharField(max_length=120, verbose_name="Name")
    description = models.TextField(verbose_name="Description")

    def __str__(self):
        return self.title


class Skill(models.Model):
    title = models.CharField(max_length=120, verbose_name="Name")

    def __str__(self):
        return self.title


class SkillOfWarrior(models.Model):
    skill = models.ForeignKey("Skill", verbose_name="Skill", on_delete=models.CASCADE)
    warrior = models.ForeignKey(
        "Warrior", verbose_name="Warrior", on_delete=models.CASCADE
    )
    level = models.IntegerField(verbose_name="Skill development level")

    def __str__(self):
        return self.skill.title
