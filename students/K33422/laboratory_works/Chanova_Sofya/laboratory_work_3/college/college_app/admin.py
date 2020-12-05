from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(StudentGroup)
admin.site.register(Room)
admin.site.register(ScheduleEntry)
admin.site.register(Subject)
admin.site.register(Teaching)
admin.site.register(SemesterGrade)
