from rest_framework.test import APITestCase
from rest_framework import status
from myapp.models import Student, Course, Semester, Teacher, StudentCard, SemesterCourse
from django.utils import timezone
import datetime

class StudentTests(APITestCase):
    """Тесты для сущности 'Студент'"""

    def setUp(self):
        """Инициализация тестового студента"""
        self.student = Student.objects.create(first_name='Иван', last_name='Иванов')
        self.student_id = self.student.id

    def test_add_student(self):
        """Тест добавления студента"""
        response = self.client.post('/api/student/', {'first_name': 'Алиса', 'last_name': 'Смирнова'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_students(self):
        """Тест получения списка студентов"""
        response = self.client.get('/api/student/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_student(self):
        """Тест просмотра данных студента"""
        response = self.client.get(f'/api/student/{self.student_id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_student(self):
        """Тест обновления данных студента"""
        response = self.client.put(f'/api/student/{self.student_id}/', data={'first_name': 'Иван', 'last_name': 'Смирнов'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_student_by_name(self):
        """Тест фильтрации студентов по имени"""
        response = self.client.get('/api/student/', {'first_name': self.student.first_name})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_student_by_surname(self):
        """Тест фильтрации студентов по фамилии"""
        response = self.client.get('/api/student/', {'last_name': self.student.last_name})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_student(self):
        """Тест удаления студента"""
        response = self.client.delete(f'/api/student/{self.student_id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class CourseTests(APITestCase):
    """Тесты для сущности 'Курс'"""

    def setUp(self):
        """Инициализация тестового курса"""
        self.course = Course.objects.create(name='Web-Dev', number=3)
        self.course_id = self.course.id

    def test_add_course(self):
        """Тест добавления курса"""
        response = self.client.post('/api/course/', {'name': 'Web-Dev1', 'number': 4})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_courses(self):
        """Тест получения списка курсов"""
        response = self.client.get('/api/course/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_course(self):
        """Тест просмотра данных курса"""
        response = self.client.get(f'/api/course/{self.course_id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_course(self):
        """Тест обновления данных курса"""
        response = self.client.put(f'/api/course/{self.course_id}/', {'name': 'WebDev3', 'number': 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_course_by_name(self):
        """Тест фильтрации курсов по названию"""
        response = self.client.get('/api/course/', {'name': self.course.name})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_course_by_number(self):
        """Тест фильтрации курсов по номеру"""
        response = self.client.get('/api/course/', {'number': self.course.number})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_delete_course(self):
        """Тест удаления курса"""
        response = self.client.delete(f'/api/course/{self.course_id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class SemesterTests(APITestCase):
    """Тесты для сущности 'Семестр'"""

    def setUp(self):
        """Инициализация тестового семестра"""
        self.semester = Semester.objects.create(number=3)
        self.semester_id = self.semester.id

    def test_add_semester(self):
        """Тест добавления семестра"""
        response = self.client.post('/api/semester/', {'number': 4})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_semesters(self):
        """Тест получения списка семестров"""
        response = self.client.get('/api/semester/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_semester(self):
        """Тест просмотра данных семестра"""
        response = self.client.get(f'/api/semester/{self.semester_id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_semester(self):
        """Тест обновления данных семестра"""
        response = self.client.put(f'/api/semester/{self.semester_id}/', {'number': 5})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_semester_by_number(self):
        """Тест фильтрации семестров по номеру"""
        response = self.client.get('/api/semester/', {'number': self.semester.number})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_delete_semester(self):
        """Тест удаления семестра"""
        response = self.client.delete(f'/api/semester/{self.semester_id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class TeacherTests(APITestCase):
    """Тесты для сущности 'Учитель'"""

    def setUp(self):
        """Инициализация тестового учителя"""
        self.teacher = Teacher.objects.create(first_name='Иван', last_name='Иванов', title='Ректор')
        self.teacher_id = self.teacher.id

    def test_add_teacher(self):
        """Тест добавления учителя"""
        response = self.client.post('/api/teacher/', {'first_name': 'Вадим', 'last_name': 'Владимирович', 'title': 'Директор'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_teachers(self):
        """Тест получения списка учителей"""
        response = self.client.get('/api/teacher/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_teacher(self):
        """Тест просмотра данных учителя"""
        response = self.client.get(f'/api/teacher/{self.teacher_id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_teacher(self):
        """Тест обновления данных учителя"""
        response = self.client.put(f'/api/teacher/{self.teacher_id}/', {'first_name': 'Максим', 'last_name': 'Максимович', 'title': 'Куратор'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_teacher_by_name(self):
        """Тест фильтрации учителей по имени"""
        response = self.client.get('/api/teacher/', {'first_name': self.teacher.first_name})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_teacher_by_surname(self):
        """Тест фильтрации учителей по фамилии"""
        response = self.client.get('/api/teacher/', {'last_name': self.teacher.last_name})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_teacher_by_title(self):
        """Тест фильтрации учителей по должности"""
        response = self.client.get('/api/teacher/', {'title': self.teacher.title})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_delete_teacher(self):
        """Тест удаления учителя"""
        response = self.client.delete(f'/api/teacher/{self.teacher_id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class StudentCardTests(APITestCase):
    """Тесты для сущности 'Студенческая карточка'"""

    def setUp(self):
        """Инициализация тестовой студенческой карточки"""
        self.student = Student.objects.create(first_name='Иван', last_name='Иванов')
        self.student_card = StudentCard.objects.create(student=self.student, name='Карточка Ивана')

    def test_add_student_card(self):
        """Тест добавления студенческой карточки"""
        student = Student.objects.create(first_name='Петр', last_name='Петров')
        response = self.client.post('/api/studentcard/', {'name': 'Карточка Петра', 'student': student.id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_student_cards(self):
        """Тест получения списка студенческих карточек"""
        response = self.client.get('/api/studentcard/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_student_card(self):
        """Тест просмотра данных студенческой карточки"""
        response = self.client.get(f'/api/studentcard/{self.student_card.student_id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_student_card(self):
        """Тест обновления студенческой карточки"""
        response = self.client.put(f'/api/studentcard/{self.student_card.student_id}/', {'name': 'Обновленная карточка', 'student': self.student_card.student_id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_student_card_by_name(self):
        """Тест фильтрации студенческих карточек по имени"""
        response = self.client.get('/api/studentcard/', {'name': self.student_card.name})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_student_card_by_student(self):
        """Тест фильтрации студенческих карточек по студенту"""
        response = self.client.get('/api/studentcard/', {'student': self.student_card.student_id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_student_card(self):
        """Тест удаления студенческой карточки"""
        response = self.client.delete(f'/api/studentcard/{self.student_card.student_id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class SemesterCourseTests(APITestCase):
    """Тесты для сущности 'Семестровый курс'"""

    def setUp(self):
        """Инициализация тестового семестрового курса"""
        self.course = Course.objects.create(name='Mathematics', number=101)
        self.semester = Semester.objects.create(number=1)
        self.semester_course = SemesterCourse.objects.create(course=self.course, semester=self.semester, start_date=timezone.now().date(), end_date=timezone.now().date() + datetime.timedelta(days=100))

    def test_add_semester_course(self):
        """Тест добавления семестрового курса"""
        new_course = Course.objects.create(name='Physics', number=102)
        new_semester = Semester.objects.create(number=2)
        response = self.client.post('/api/semestercourse/', {
            'course': new_course.id,
            'semester': new_semester.id,
            'start_date': '2023-01-01',
            'end_date': '2023-06-01'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_semester_courses(self):
        """Тест получения списка семестровых курсов"""
        response = self.client.get('/api/semestercourse/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_semester_course(self):
        """Тест просмотра данных семестрового курса"""
        response = self.client.get(f'/api/semestercourse/{self.semester_course.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_semester_course(self):
        """Тест обновления семестрового курса"""
        response = self.client.put(f'/api/semestercourse/{self.semester_course.id}/', {
            'course': self.course.id,
            'semester': self.semester.id,
            'start_date': '2023-01-01',
            'end_date': '2023-06-01'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_semester_course_by_course(self):
        """Тест фильтрации семестровых курсов по курсу"""
        response = self.client.get('/api/semestercourse/', {'course': self.course.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_semester_course_by_semester(self):
        """Тест фильтрации семестровых курсов по семестру"""
        response = self.client.get('/api/semestercourse/', {'semester': self.semester.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_semester_course_by_date_range(self):
        """Тест фильтрации семестровых курсов по диапазону дат"""
        response = self.client.get('/api/semestercourse/', {
            'start_date': '2023-01-01',
            'end_date': '2023-06-01'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_semester_course(self):
        """Тест удаления семестрового курса"""
        response = self.client.delete(f'/api/semestercourse/{self.semester_course.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
