from django.contrib import admin
from .models import *

admin.site.register(Doctor)
admin.site.register(Cabinet)
admin.site.register(Schedule)
admin.site.register(Price)
admin.site.register(Patient)
admin.site.register(Diagnosis)
admin.site.register(Medcard)
admin.site.register(Meeting)