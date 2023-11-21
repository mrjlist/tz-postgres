from django.db import models

class Student(models.Model):
    """
    Модель Студента.
    Содержит информацию о имени и фамилии студента.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f'Студент {self.first_name} {self.last_name}'

class Course(models.Model):
    """
    Модель Курса.
    Содержит информацию о названии курса и его номере.
    """
    name = models.CharField(max_length=100)
    number = models.IntegerField()

    def __str__(self):
        return f'{self.name}, курс {self.number}'

class Semester(models.Model):
    """
    Модель Семестра.
    Хранит уникальный номер семестра.
    """
    number = models.IntegerField(unique=True)

    def __str__(self):
        return f'Семестр {self.number}'

class Teacher(models.Model):
    """
    Модель Преподавателя.
    Содержит информацию о имени, фамилии и звании преподавателя.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.title} {self.first_name} {self.last_name}'

class StudentCard(models.Model):
    """
    Модель Личной карты студента.
    Связывает студента с его личной карточкой.
    """
    student = models.OneToOneField(Student, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'Карта студента: {self.name}'

class SemesterCourse(models.Model):
    """
    Модель Семестрового курса.
    Описывает связь между курсом и семестром, включая даты начала и окончания.
    """
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'{self.semester.number} семестр, курс {self.course.name}'
