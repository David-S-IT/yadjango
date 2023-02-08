# yadjango

## Запуск проекта в dev-режиме
#### Скачайте Python версии 3.7.16
- Linux:
```sudo apt install python==3.7.16``` 
- Windows (3.7.9):
- - 64-битная версия:
https://www.python.org/ftp/python/3.7.9/python-3.7.9-amd64.exe
- - 32-битная версия:
https://www.python.org/ftp/python/3.7.9/python-3.7.9.exe
#### Создайте виртуальное окружение в папке с проектом(лучше, через CMD, а не PowerShell)
```python -m venv venv```
#### Активируйте виртуальное окружение
- Linux:
```source venv/bin/activate```
- Windows (3.7.9):
```.\venv\Scripts\activate.bat```
#### Установите зависимости из файла requirements.txt
```pip install -r requirements.txt```
#### Запустите сервер (в папке ya, с файлом manage.py)
```python manage.py runserver```