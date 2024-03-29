
# Разработка API и базы данных

Разработан API по архитектуре описанной в UML-диаграмме

## Начало работы

Эти инструкции помогут вам запустить копию проекта на вашем локальном компьютере для разработки и тестирования.

### Предварительные требования

```
Docker
Python 3.10+
```

### Установка

Шаг за шагом расскажу, как запустить разработочную среду:

1. **Установка зависимостей:**

   ```
   pip install -r requirements.txt
   ```

2. **Деплой базы данных:**

   ```
   docker-compose up -d
   ```
   
3. **Перейдите в деррикторию проекта**
   
   ```
   cd myproject
   ```
   
5. **Выполнение миграций:**

   ```
   python manage.py migrate
   ```

6. **Создание суперпользователя:**

   ```
   python manage.py createsuperuser
   ```

7. **Заполнение базы данных:**

   ```
   python seeds.py
   ```

8. **Тестирование API на работоспособность:**

   ```
   python manage.py test myapp
   ```

9. **Запуск проекта:**

   ```
   python manage.py runserver
   ```

## Документация API

Документация по API доступна по следующему адресу:

```
http://127.0.0.1:8000/api/docs/
```

## Авторы

* **Андрей Лукашенко** - *[Тестовое задание](https://github.com/mrjlist/tz-postgres/blob/main/Тестовое%20задание.pdf)*
