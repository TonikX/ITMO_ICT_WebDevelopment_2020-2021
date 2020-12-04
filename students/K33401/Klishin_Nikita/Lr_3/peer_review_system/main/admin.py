from django.contrib import admin

from .models import (
	Task, 
	TaskExecutor,
	TaskInspection,
	Criterion, 
	StudentsClass
)


# class StudentsInline(admin.TabularInline):
# 	model = StudentProfile


class TaskAdmin(admin.ModelAdmin):
	list_display = ['title', 'description']

	#inlines = [
	# 	CriterionInline,
	# ]

# class StudentInline(admin.TabularInline):
#     model = CustomUser

class StudentsClassAdmin(admin.ModelAdmin):
	list_display = ['title']
	# inlines = [
	# 	StudentsInline
	# ]



admin.site.register(Task, TaskAdmin)
admin.site.register(Criterion)
admin.site.register(TaskExecutor)
admin.site.register(TaskInspection)
admin.site.register(StudentsClass, StudentsClassAdmin)

# admin.site.register(StudentProfile)
