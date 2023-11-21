from django.contrib import admin
from .models import Student, StudentCard, Teacher, Course, Semester, SemesterCourse

# Регистрация моделей для управления через админ-панель
admin.site.register(Student)
admin.site.register(StudentCard)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Semester)
admin.site.register(SemesterCourse)
