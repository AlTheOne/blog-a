Собираем миграции:<br>
`python manage.py makemigrations adviceApp boardApp feedbackApp galleryApp mbaseApp nbaseApp creationApp mainApp`

Выполняем миграции:<br>
`python manage.py migrate`

Создаём суперпользователя:<br>
`python manage.py createsuperuser`

Пуск dev сервера:<br>
`python manage.py runserver`

В модуле "Статические страницы" необходимо создать:

- Страницу со слагом **main** (для главной страницы)
- Страницу со слагом **portfolio** (для страницы портфолио)
