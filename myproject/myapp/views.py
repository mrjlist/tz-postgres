from rest_framework import viewsets
from .models import Student, Course, Semester, Teacher, StudentCard, SemesterCourse
from .serializers import StudentSerializer, CourseSerializer, SemesterSerializer, TeacherSerializer, SemesterCourseSerializer, StudentCardSerializer
from django_filters.rest_framework import DjangoFilterBackend

class StudentViewSet(viewsets.ModelViewSet):
    """
    ViewSet для обработки запросов к сущности 'Студент'.
    Поддерживает операции чтения, создания, обновления и удаления.
    Включает фильтрацию по имени и фамилии студента.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['first_name', 'last_name']

class CourseViewSet(viewsets.ModelViewSet):
    """
    ViewSet для обработки запросов к сущности 'Курс'.
    Поддерживает операции чтения, создания, обновления и удаления.
    Включает фильтрацию по названию курса и его номеру.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'number']

class SemesterViewSet(viewsets.ModelViewSet):
    """
    ViewSet для обработки запросов к сущности 'Семестр'.
    Поддерживает операции чтения, создания, обновления и удаления.
    Включает фильтрацию по номеру семестра.
    """
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['number']

class TeacherViewSet(viewsets.ModelViewSet):
    """
    ViewSet для обработки запросов к сущности 'Преподаватель'.
    Поддерживает операции чтения, создания, обновления и удаления.
    Включает фильтрацию по имени, фамилии и званию преподавателя.
    """
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['first_name', 'last_name', 'title']

class StudentCardViewSet(viewsets.ModelViewSet):
    """
    ViewSet для обработки запросов к сущности 'Студенческая карточка'.
    Поддерживает операции чтения, создания, обновления и удаления.
    Включает фильтрацию по имени карточки и связанному студенту.
    """
    queryset = StudentCard.objects.all()
    serializer_class = StudentCardSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'student']

class SemesterCourseViewSet(viewsets.ModelViewSet):
    """
    ViewSet для обработки запросов к сущности 'Семестровый курс'.
    Поддерживает операции чтения, создания, обновления и удаления.
    Включает фильтрацию по курсу, семестру и датам начала/окончания.
    """
    queryset = SemesterCourse.objects.all()
    serializer_class = SemesterCourseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['course', 'semester', 'start_date', 'end_date']
