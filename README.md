# Simple PasteBin v1.1.0

## Description [ENG]

**Simple PasteBin** is a minimalistic web application, for downloading any texts to share with users via a short link.

## Description [RUS]

**Simple PasteBin** - это минималистичное веб приложение, для загрузки любых текстов, чтобы поделиться с пользователями по короткой ссылке.

---

## How to deploy [ENG]

1. To get started, you need: *MySQL, Redis*, and *S3 storage*. You can rent a specialized server, or install on your server yourself.
2. Download the source code, and unpack it on the server.
3. Edit the *config.py* file so that all items are changed.
4. [Deploy the application](https://flask.palletsprojects.com/en/3.0.x/deploying/).
5. Add a task to crontab that opens a */cron* page every hour to clean up overdue posts.

## How to deploy [RUS]

1. Для начала вам нужно: *MySQL, Redis*, и *S3 хранилище*. Вы можете арендовать специализированный сервер, или установить на свой сервер самому.
2. Скачайте исходный код, и распакуйте на сервере.
3. Отредактируйте файл *config.py*, чтобы все пункты были изменены.
4. [Разверните приложение](https://flask.palletsprojects.com/en/3.0.x/deploying/).
5. Добавьте в crontab задачу, которая открывает каждый час страницу */cron*, для очистки просроченных постов.

---

## TODO [ENG]
* Unit tests.
