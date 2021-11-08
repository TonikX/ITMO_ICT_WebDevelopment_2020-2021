from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Newspaper)
admin.site.register(NewspapersParty)
admin.site.register(Print)
admin.site.register(Printery)
admin.site.register(PostOffice)
admin.site.register(DistributionReport)