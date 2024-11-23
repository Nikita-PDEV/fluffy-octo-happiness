from django.db import models  
from django.db.models.signals import post_save  
from django.dispatch import receiver  
from .tasks import notify_subscribers  

class News(models.Model):  
    title = models.CharField(max_length=200)  
    content = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True)  

@receiver(post_save, sender=News)  
def news_created(sender, instance, created, **kwargs):  
    if created:  
        notify_subscribers.delay(instance.id)  
        from flask_sqlalchemy import SQLAlchemy  

db = SQLAlchemy()  

class User(db.Model):  
    id = db.Column(db.Integer, primary_key=True)  
    email = db.Column(db.String(120), unique=True, nullable=False)  
    subscriptions = db.relationship('Subscription', backref='subscriber', lazy=True)  

class Article(db.Model):  
    id = db.Column(db.Integer, primary_key=True)  
    title = db.Column(db.String(200), nullable=False)  
    content = db.Column(db.Text, nullable=False)  
    category = db.Column(db.String(50), nullable=False)  
    timestamp = db.Column(db.DateTime, index=True, default=db.func.current_timestamp)  

class Subscription(db.Model):  
    id = db.Column(db.Integer, primary_key=True)  
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  
    category = db.Column(db.String(50), nullable=False)