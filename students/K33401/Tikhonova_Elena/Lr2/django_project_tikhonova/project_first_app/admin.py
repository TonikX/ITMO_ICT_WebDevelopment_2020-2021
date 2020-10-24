from django.contrib import admin
from .models import Car, Owner, License, Registration

class LicenseInline(admin.TabularInline):
	model = License
	extra = 1

class RegistrationInline(admin.TabularInline):
	model = Registration
	extra = 1

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
	list_display = ('number', 'brand', 'model', 'color')
	list_display_links = ('number',)
	list_filter = ('brand',)
	inlines = [RegistrationInline]

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'birthday')
	inlines = [LicenseInline, RegistrationInline]

class RegistrationAdmin(admin.ModelAdmin):
	list_display = ('owner', 'car', 'start_date', 'end_date')


#admin.site.register(Car, CarAdmin)
#admin.site.register(Owner, OwnerAdmin)
admin.site.register(License)
admin.site.register(Registration, RegistrationAdmin)
