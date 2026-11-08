# Teaching Project

Django-проект, развёрнутый в Docker. Приложение работает в контейнере `web`,
база данных PostgreSQL — в контейнере `db`, они общаются внутри сети Docker Compose.

## Описание:

"Teaching Project" - это платформа для онлайн-обучения.
LMS-система, в которой каждый желающий может размещать свои полезные материалы/лекции или курсы.
В эом приложении можно использовать учет платежей.

## Стек технологий

- Python 3.x, Django
- PostgreSQL
- Docker и Docker Compose
- PyCharm (IDE)

## Структура проекта

```
project/
├── teaching/
├── users/
├── Dockerfile
├── docker-compose.yml
├── .env
├── .env.sample
├── .dockerignore
├── .gitignore
├── requirements.txt
└── README.md
```

## Быстрый старт

1. Склонируйте репозиторий и перейдите в папку проекта.
2. Создайте файл `.env` по образцу `.env.example`.
3. Соберите и запустите контейнеры:

    ```bash
    docker compose up -d --build
    ```
4. примините миграции:
   ```
    docker compose exec web python manage.py migrate
   ```
5. создайте суперпользователя: 
   ``` 
   docker compose exec web python manage.py createsuperuser
   ```
6. Откройте в браузере:

- сайт: http://localhost:8000
- админка: http://localhost:8000/admin/


## Переменные окружения

```
SECRET_KEY	- Секретный ключ Django	
DEBUG	- Режим отладки (True / False)	
POSTGRES_DB- Имя базы данных (в нижнем регистре)	
POSTGRES_USER	- Пользователь БД	(в нижнем регистре)
POSTGRES_PASSWORD- Пароль пользователя БД	
DATABASE_HOST -	Хост БД внутри сети Docker — имя сервиса	-
DATABASE_PORT -	Порт БД	
```
 
## Использование:

1. Откройте приложение в вашем веб-браузере.
2. Создайте новый проект и начните наполнять базу данных курасами и лекциями, если есть пользователи, 
ими тоже. 


## Лицензия:

Проект распространяется под [лицензией MIT](LICENSE).