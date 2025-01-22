from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Recipe)
admin.site.register(StudentID)
admin.site.register(Student)
admin.site.register(Department)
# report card
admin.site.register(Subject)
class SubjectMarksAdmin(admin.ModelAdmin):
    list_display = ['student','subject','marks']
    search_fields = ['student__student_name','subject__subject_name']
    list_filter = ['subject']
    list_per_page = 10

admin.site.register(SubjectMarks,SubjectMarksAdmin)