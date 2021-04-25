from django.db import models

class Warrior(models.Model):
  
  race_types = (
    ('s', 'student'),
    ('d', 'developer'),
    ('t', 'teamlead'),
  )

  race = models.CharField(max_length=1, choices=race_types, verbose_name='Pacca')
  name = models.CharField('Name', max_length=120)
  level = models.IntegerField('Level', default=0)
  skill = models.ManyToManyField('Skill', through='SkillOfWarrior', related_name='warrior_skills')
  profession = models.ForeignKey('Profession', on_delete=models.CASCADE, verbose_name='Profession', blank=True, null=True)

  def __str__(self):
    return self.get_race_display()


class Profession(models.Model):
  """
  Описание профессии
  """

  title = models.CharField(max_length=120, verbose_name='Название')
  description = models.TextField(verbose_name='Описание')


class Skill(models.Model):
  """
  Описание умений
  """

  title = models.CharField(max_length=120, verbose_name='Наименование')

  def __str__(self):
    return self.title


class SkillOfWarrior(models.Model):
  """
  Описание умений война
  """

  skill = models.ForeignKey('Skill', verbose_name='Умение', on_delete=models.CASCADE)
  warrior = models.ForeignKey('Warrior', verbose_name='Воин', on_delete=models.CASCADE)
  level = models.IntegerField(verbose_name='Уровень освоения умения')