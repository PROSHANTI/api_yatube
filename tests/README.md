# Проект API для Yatube

### Описание:

Финальный проект блока API.

Курс "Python-Разработчик" от Яндекс.Практикум

Yatube — это платформа для блогов, чем-то похожая на Блогикум. Все блоги чем-то похожи друг на друга: любой блог-сервис предполагает возможность зарегистрироваться, создать, отредактировать или удалить собственный пост, прокомментировать пост другого автора и подписаться на него.

Данный проект позволяет осуществлять работу с приложением Yatube по средством API на базе Django + Django REST Framework.

### Технологии:

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:
```bash
git clone https://github.com/PROSHANTI/api_final_yatube.git
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:
```bash
WINDOWS:

python -m venv venv
source venv/scripts/activate

MACOS:

python3 -m venv venv
```
Установить зависимости из файла requirements.txt:
```bash
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

Выполнить миграции:
```bash
cd yatube_api
python3 manage.py migrate
```

Запустить проект:
```bash
python3 manage.py runserver
```

### Примеры работы API:

После запуска проекта, документация с примерами доступна по адресу: 
```
http://127.0.0.1:8000/redoc/
```

### Автор проекта

Максим Субботин - [GitHub](<https://github.com/PROSHANTI>)