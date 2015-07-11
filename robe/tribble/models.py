from django.db import models
import time

# Create your models here.
class Words_India(models.Model):
    word_name = models.CharField(max_length=200)
    frequency = models.IntegerField(default=1)
    trend = models.IntegerField(range(1,3), default=3)
    sentiment = models.IntegerField(range(0,4,2),default=2)
    senti_flag = models.BooleanField(default=0)
    word_from = models.CharField(default='', max_length=500)
    date_time = models.DateTimeField(default=time.strftime('%Y-%m-%m %H:%M:%S'))
    url = models.CharField(max_length=500, default=None)

class Words_Global(models.Model):
    word_name = models.CharField(max_length=200)
    frequency = models.IntegerField(default=1)
    trend = models.IntegerField(range(1,3), default=3)
    senti_flag = models.BooleanField(default=0)
    sentiment = models.IntegerField(range(0,4,2),default=2)
    word_from = models.CharField(default='', max_length=500)
    date_time = models.DateTimeField(default=time.strftime('%Y-%m-%m %H:%M:%S'))
    url = models.CharField(max_length=500, default=None)

class ytstats(models.Model):
    num_videos = models.IntegerField(default=0)
    subscribers = models.IntegerField(default=0)
    video_views = models.IntegerField(default=0)
    video_likes = models.IntegerField(default=0)
    date_time = models.DateTimeField(default=time.strftime('%Y-%m-%m %H:%M:%S'))

class fbstats(models.Model):
    num_posts = models.IntegerField(default=0)
    page_likes = models.IntegerField(default=0)
    post_views = models.IntegerField(default=0)
    total_likes = models.IntegerField(default=0)
    date_time = models.DateTimeField(default=time.strftime('%Y-%m-%m %H:%M:%S'))

class tstats(models.Model):
    num_videos = models.IntegerField(default=0)
    followers = models.IntegerField(default=0)
    retweets = models.IntegerField(default=0)
    total_favourites = models.IntegerField(default=0)
    date_time = models.DateTimeField(default=time.strftime('%Y-%m-%m %H:%M:%S'))

class wordlist(models.Model):
    word = models.CharField(max_length=100)