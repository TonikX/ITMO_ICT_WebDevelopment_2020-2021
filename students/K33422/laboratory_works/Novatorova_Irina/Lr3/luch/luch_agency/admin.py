from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Application)
admin.site.register(Application_list)
admin.site.register(Client)
admin.site.register(Manufactory)
admin.site.register(Material)
admin.site.register(Payment_order)
admin.site.register(Service)
admin.site.register(Worker)