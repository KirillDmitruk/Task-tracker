# Task Tracker

## Описание
Task Tracker - это веб-приложение для эффективного управления задачами, назначенные сотрудникам, а так же обеспечивает прозрачность процессов выполнения задач. Такое приложение помогает командам и организациям эффективно управлять задачами, следить за их выполнением и обеспечивать продуктивность.

1. Клонируйте репозиторий:

   ```bash
   git clone <URL вашего репозитория>
   cd <Имя вашего репозитория>
   
## Запуск проекта

1. Постройте и запустите контейнеры Docker:

   ```bash
   docker-compose up -d --build

2. Выполните миграции базы данных:

   ```bash
   docker-compose exec habit python manage.py migrate

3. Создайте суперпользователя (если необходимо):

   ```bash
   docker-compose exec habit python manage.py createsuperuser

4. Откройте браузер и перейдите по адресу http://localhost:8000/library/ для доступа к приложению.

## Команды Docker

Запуск контейнеров в фоновом режиме:

    ```bash
    docker-compose up -d

Остановка контейнеров:

    ```bash
    docker-compose down

Перестройка контейнеров и перезапуск:

    ```bash
    docker-compose up -d --build

Просмотр логов контейнеров:

    ```bash
    docker-compose logs

Запуск оболочки в контейнере habit:

    ```bash
    docker-compose exec habit bash

Остановка всех контейнеров:

    ```bash
    docker-compose stop

## Завершение работы

**Для остановки и удаления всех контейнеров, сетей и томов:**

    ```bash
    docker-compose down -v
