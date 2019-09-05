# Как запустить:
Создать virtualenv:  
```
virtualenv -p python3 env 
```
Активировать virtualenv:  
```
source env/bin/activate
```
Перейти в simple_chat и установить requirements.txt:
```
pip install -r requirements.txt
```
Заполнить chat_project/chat_project/settings.py в соответствии с настройками БД:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_name',
        'USER': 'db_name',
        'PASSWORD': 'db_password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```
Выполнить:
```
python manage.py migrate
```
Запустить проект командой:
```
python manage.py runserver
```
