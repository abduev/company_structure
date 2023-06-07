# Проект Company structure


Требования:
 - Python 3.8+
 - Git
 - Docker
 - Docker compose

Установка и запуск:

Клонируем проект:
git clone https://github.com/abduev/company_structure.git

Переходим в корневой каталог проекта.
Запускаем сборку проекта:
```sh
docker-compose up -d
```
Создаем суперпользователя:
 ```sh
docker-compose exec web python manage.py createsuperuser
```

Админка: http://127.0.0.1/admin/

API документация: http://127.0.0.1:8000/api/swagger/

Для остановки проекта выполните команду:
```sh
docker-compose down
```