import os  
from celery.schedules import crontab  

# Добавьте ваше приложение в INSTALLED_APPS  
INSTALLED_APPS = [  
    ...  
    'news',  
    'django_celery_beat',  # для периодических задач  
]  

# Настройки для Celery  
CELERY_BROKER_URL = 'redis://localhost:6379/0'  
CELERY_ACCEPT_CONTENT = ['json']  
CELERY_TASK_SERIALIZER = 'json'  

# Настройка еженедельной задачи  
CELERY_BEAT_SCHEDULE = {  
    'send_weekly_newsletter': {  
        'task': 'news.tasks.send_weekly_newsletter',  
        'schedule': crontab(hour=8, minute=0, day_of_week='mon'),  # Каждую понедельник в 8:00  
    },  
}  

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  
EMAIL_HOST = 'smtp.example.com'  
EMAIL_PORT = 587  
EMAIL_HOST_USER = 'email@example.com'  
EMAIL_HOST_PASSWORD = 'email_password'  
DEFAULT_FROM_EMAIL = 'webmaster@example.com'  