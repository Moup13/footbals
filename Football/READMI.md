
<p align="center">
    <a target="_blank" rel="noopener noreferrer">
    "Football"   
    </a>
</p>
Данный проект написан на фрэймворке Django.

Состоит из рабочих разделов:Футбол(все доступные стадионы для футбола),Минифутбол(все доступные стадионы для минифутбола),остальные разделы не нужны заказчику.


# Установка

### 1) Создать виртуальное окружение
    python3 -m venv venv

    source venv/bin/activate

### 2) Установить зависимости

    pip install -r requirements.txt

### 3) Выполнить миграции

    python manage.py migrate    

### 4) Создать суперпользователя

    python manage.py createsuperuser

# Старт

    python manage.py runserver