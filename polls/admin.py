from django.contrib import admin
from .models import Student, Application, SchoolStaff, Event

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    def full_name(obj):
        return obj.last_name + ' ' + obj.first_name + ' ' + obj.father_name

    list_display = ('id', full_name, 'address', 'birth_date', 'tel', 'email', 'grade')


class ApplicationAdmin(admin.ModelAdmin):
    def stud(obj):
        return obj.student.first_name + ' ' + obj.student.last_name + ' ' + str(obj.student.grade)
    list_display = ('creation_date', stud)
    list_filter = ('creation_date',)


admin.site.register(Student, StudentAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(SchoolStaff)
admin.site.register(Event)
