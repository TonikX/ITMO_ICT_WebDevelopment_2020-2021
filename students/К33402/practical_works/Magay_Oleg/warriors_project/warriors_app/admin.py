from django.contrib import admin

# Register your models here.
from warriors_app.models import Warrior, Profession, Skill, SkillOfWarrior

admin.site.register(Warrior)
admin.site.register(Profession)
admin.site.register(Skill)
admin.site.register(SkillOfWarrior)
