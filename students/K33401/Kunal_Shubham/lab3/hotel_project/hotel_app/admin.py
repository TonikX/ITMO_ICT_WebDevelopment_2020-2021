from django.contrib import admin
from .models import Employee, Room, Resident, BookingRecord, CleaningSchedule


# Register your models here.
admin.site.register(Employee)
admin.site.register(Room)
admin.site.register(Resident)
admin.site.register(BookingRecord)
admin.site.register(CleaningSchedule)