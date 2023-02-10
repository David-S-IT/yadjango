# yadjango

[![flake8 Lint](https://github.com/David-S-IT/yadjango/actions/workflows/%20py-actions.yml/badge.svg)](https://github.com/David-S-IT/yadjango/actions/workflows/%20py-actions.yml)
![](https://img.shields.io/badge/django-3.2-green)
![](https://img.shields.io/badge/python-3.7-brightgreen)

## Запуск проекта в dev-режиме
#### 1. Скачать Python версии 3.7.16
- Linux: ```sudo apt install python==3.7.16``` 
- Windows (python 3.7.16 просто так скачать не получится, но python 3.7.9 тоже подходит):
- - 64-битная версия:
https://www.python.org/ftp/python/3.7.9/python-3.7.9-amd64.exe
- - 32-битная версия:
https://www.python.org/ftp/python/3.7.9/python-3.7.9.exe
#### 2. Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/David-S-IT/yadjango.git
cd yadjango
```
Если у вас появляется ошибка, что нет команды ```git```, то вам нужно установить Git Bash.
#### 3. Cоздать виртуальное окружение в папке с проектом
- Linux: ```python3.7 -m venv venv```
- Windows: ```python -m venv venv```
#### 4. Активировать виртуальное окружение
- Linux:
```source venv/bin/activate```
- Windows:
```.\venv\Scripts\activate.bat```
#### 5. Установить зависимости
Перейти в папку requirements: ```cd requirements```
- Для запуска сервера: ```pip install -r requirements_prod.txt```
- Для разработки: ```pip install -r requirements_dev.txt```
- Для тестов: ```pip install -r requirements_tests.txt```
#### 6. Для генерации SECRET_KEY выполнить:
```
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```
Вставить значение ключа в settings.py  SECRET_KEY="..."
#### 7. Запуск сервера
Выйти из папки requirements: ```cd ..```  
Перейти в папку ya с файлом manage.py: ```cd ya```
- Linux: ```python3.7 manage.py runserver```
- Windows: ```python manage.py runserver```