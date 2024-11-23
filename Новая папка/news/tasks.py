from celery import shared_task  
from .models import News  
from django.core.mail import send_mail  
from django.contrib.auth.models import User  

@shared_task  
def notify_subscribers(news_id):  
    news = News.objects.get(id=news_id)  
    subscribers = User.objects.filter(is_subscribed=True) 
    email_list = [user.email for user in subscribers]  

    subject = f'Новая новость: {news.title}'  
    message = f'{news.content} \n\n Ссылка на новость: http://example.com/news/{news_id}/'  
    send_mail(subject, message, 'from@example.com', email_list)  

@shared_task  
def send_weekly_newsletter():  
    last_week_news = News.objects.filter(created_at__gte=datetime.now() - timedelta(days=7))  
    subscribers = User.objects.filter(is_subscribed=True)  
    email_list = [user.email for user in subscribers]  

    subject = 'Еженедельная рассылка новостей'  
    message = 'Вот последние новости за неделю:\n\n'  

    for news in last_week_news:  
        message += f'{news.title}: http://example.com/news/{news.id}/\n'  

    send_mail(subject, message, 'from@example.com', email_list)  