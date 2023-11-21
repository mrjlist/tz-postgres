import os
import django
from django_seed import Seed
from random import randint, choice
from datetime import timedelta, date

# Настройте настройки Django для скрипта
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from myapp.models import Student, Teacher, Course, Semester, SemesterCourse, StudentCard

# Инициализируем seeder
seeder = Seed.seeder()

# Определяем функцию для генерации случайных дат в заданном диапазоне
def random_date_for_semester(semester):
    if semester.number == 1:
        start_date = date(2022, 9, 1)
        end_date = date(2023, 2, 28)
    elif semester.number == 2:
        start_date = date(2023, 2, 15)
        end_date = date(2023, 7, 15)
    else:
        raise ValueError("Неподдерживаемый номер семестра")
    random_days = randint(0, (end_date - start_date).days)
    return start_date + timedelta(days=random_days)

# Добавляем сиды для студентов
seeder.add_entity(Student, 100, {
    'first_name': lambda x: seeder.faker.first_name(),
    'last_name': lambda x: seeder.faker.last_name(),
})

# Добавляем сиды для преподавателей
seeder.add_entity(Teacher, 20, {
    'first_name': lambda x: seeder.faker.first_name(),
    'last_name': lambda x: seeder.faker.last_name(),
    'title': lambda x: choice(['Доцент', 'Профессор', 'Старший преподаватель']),
})

# Выполнить сидирование для студентов, преподавателей, курсов и семестров
inserted_pks = seeder.execute()


# Для связанных сущностей, таких как StudentCard и SemesterCourse, нам нужно будет вручную создать связи
# Создаем личные карты для каждого студента
course_names = ['Програмист', 'Юрист', 'Адвокат', "Логист", "Маркетолог", "Экономист", "Строитель", "Гениколог"]

for name in course_names:
    for number in range(1, 6):  # Для каждого курса создаем номера от 1 до 5
        Course.objects.create(name=name, number=number)

for number in range(1, 3):  # Для каждого курса создаем номера от 1 до 5
    Semester.objects.create(number=number)

for student_pk in inserted_pks[Student]:
    student = Student.objects.get(pk=student_pk)
    StudentCard.objects.create(
        student=student,
        name=student.first_name
    )

# Создаем семестровые курсы и связываем их со случайными курсами и семестрами
for semester in Semester.objects.all():
    for course in Course.objects.all():
        start_date = random_date_for_semester(semester)
        end_date = start_date + timedelta(days=120)  # Примерное продолжительность курса

        SemesterCourse.objects.create(
            course=course,
            semester=semester,
            start_date=start_date,
            end_date=end_date
        )

# Выведем сообщение об успешном завершении сидирования
print("База данных успешно заполнена начальными данными!")
