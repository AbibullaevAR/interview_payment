# Interview_payment




## Name
Interview_payment

## Description
Данный сервис можно проверить по ссылке https://ftt-dream-team.ru/interviewPayment/items/

Для входа в панель администратора прейти по ссылке https://ftt-dream-team.ru/admin и использовать:

Логин: `Admin_test`

Пароль: `admin`

## Installation
Так же можно запустить локально. Для этого требуется склонировать репозиторий и настроить переменные окружения в файлах .env.db и .env.prod

В файле .env.db:
- `POSTGRES_USER` имя пользователя БД
- `POSTGRES_PASSWORD` пароль пользователя БД
- `POSTGRES_DB` имя базы данных

В файле .env.prod:
- `DEBUG` включает и отключает режим тестирования. 1 для включения 0 для выключения. 
- `SECRET_KEY` устанавливает секретный ключ
- `DJANGO_ALLOWED_HOSTS` устанавливает ALLOWED_HOSTS параметр для локальной разработки установить значение `localhost 127.0.0.1 [::1]`
- `DATABASES_NAME` должно совпадать со значением в .env.db `POSTGRES_DB`
- `DATABASES_USER` должно совпадать со значением в .env.db `POSTGRES_USER`
- `DATABASES_PASSWORD` должно совпадать со значением в .env.db `POSTGRES_PASSWORD`
- `DATABASES_HOST` установить значение `db`
- `DATABASES_PORT` установить зачение `5432`
- `STRIPE_API_KEY` установить значение секретного ключа stripe. Например `sk_test_51M7bAyEP3f4ccZtMUm6PPxkH7JPzKSnYVmZv6qq3yWRdZ6ejlHDCGm2SixRBzteZXnveaznBGlZOHPBnQ7PYW1kw00r77SyvCy`

После установки переменных окружения запустить команду `docker-compose up -d --build` в директории проекта. Сервис будет доступен по адресу `http://localhost:8000/interviewPayment/items/`.

