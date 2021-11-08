from main.models import Book, BookReplica, CustomUser, Librarian, LibraryHall, Reader
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ['id', 'email', 'is_staff', 'is_librarian']
    list_filter = ('is_staff', )

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Status', {'fields': ('is_librarian',)}),
		('Permissions', {'fields': ('is_staff',)}),
    )

    add_fieldsets = (
        (None, {'fields': ('email', 'password1', 'password2')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Status', {'fields': ('is_staff',)}),
	)

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


@admin.register(LibraryHall)
class LibraryHallAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', )


@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')


admin.site.register(Librarian)
admin.site.register(Book)
admin.site.register(BookReplica)

