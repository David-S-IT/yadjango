# yadjango

[![flake8 Lint](https://github.com/David-S-IT/yadjango/actions/workflows/py-actions-flake8.yml/badge.svg)](https://github.com/David-S-IT/yadjango/actions/workflows/py-actions-flake8.yml)
[![black Lint](https://github.com/David-S-IT/yadjango/actions/workflows/black.yml/badge.svg)](https://github.com/David-S-IT/yadjango/actions/workflows/black.yml)
[![django tests](https://github.com/David-S-IT/yadjango/actions/workflows/django_tests.yml/badge.svg)](https://github.com/David-S-IT/yadjango/actions/workflows/django_tests.yml)
![](https://img.shields.io/badge/django-3.2.18-green)
![](https://img.shields.io/badge/python-3.9-brightgreen)

## Запуск проекта в dev-режиме
#### 1. Скачать Python версии 3.9
- Linux: 
- - ```sudo apt install python==3.9```
- - ```sudo apt install python3.9-venv```
- Windows (python 3.9.16 просто так скачать не получится, но python 3.9.13 тоже подходит):
- - 64-битная версия:
https://www.python.org/ftp/python/3.9.13/python-3.9.13-amd64.exe
- - 32-битная версия:
https://www.python.org/ftp/python/3.9.13/python-3.9.13.exe
#### 2. Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/David-S-IT/yadjango.git
cd yadjango
```
Если у вас появляется ошибка, что нет команды ```git```, то вам нужно установить Git Bash: https://gitforwindows.org/
#### 3. Cоздать виртуальное окружение в папке с проектом
- Linux: ```python3.9 -m venv venv```
- Windows: ```python -m venv venv```
#### 4. Активировать виртуальное окружение
- Linux:
```source venv/bin/activate```
- Windows:
```.\venv\Scripts\activate.bat```
#### 5. Установить зависимости
Обновить pip: ```venv/bin/python -m pip install --upgrade pip```  
Перейти в папку requirements: ```cd requirements```
- Основной - для запуска сервера: ```pip install -r requirements_prod.txt```
- Дополнительный - для тестов: ```pip install -r requirements_test.txt```
- Дополнительный - для разработки: ```pip install -r requirements_dev.txt```
Выйти из папки requirements: ```cd ..```  

#### 6. Создать и применить миграции
```
python manage.py makemigrations
```
```
python manage.py migrate
```

#### 7. Для генерации SECRET_KEY:
Открыть Python:  
- Linux: ```python3.9```
- Windows: ```python```

Выполнить:  
```
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```
Вставить значение ключа в example.env SECRET_KEY="..."  
Для закрытия Python выполнить: ```quit()```
#### 8. Запуск сервера
Перейти в папку ya с файлом manage.py: ```cd ya```
- Linux: ```python3.9 manage.py runserver```
- Windows: ```python manage.py runserver```
#### 9. Сайт доступен по адресу: http://127.0.0.1:8000/

## Фикстуры для наполнения базы
Используйте фикстуры для тестов в папке ya, где manage.py
Чтобы загрузить фикстуры выполнить:

```
python manage.py loaddata fixtures.json
```
Пользователь: admin  
Пароль: adminadmin

## Чтобы создать своего суперпользователя с правами админа
Выполнить и исполнить предложенные инструкции в консоли
```
python manage.py createsuperuser
```


