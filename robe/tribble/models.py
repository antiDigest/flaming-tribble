from django.db import models
import time

# Create your models here.
class Words_India(models.Model):
    word_name = models.CharField(max_length=200)
    frequency = models.IntegerField(default=1)
    senti_pos = models.IntegerField(default=0)
    senti_neg = models.IntegerField(default=0)
    senti_neut = models.IntegerField(default=0)
    senti_flag = models.BooleanField(default=0)
    word_from = models.CharField(default='', max_length=500)
    onlydate = models.DateTimeField(default=time.strftime('%Y-%m-%d'))
    date_time = models.DateTimeField(default=time.strftime('%Y-%m-%d %H:%M:%S'))

    def __unicode__(self):
        return self.word_name

class Words_Global(models.Model):
    word_name = models.CharField(max_length=200)
    frequency = models.IntegerField(default=1)
    senti_flag = models.BooleanField(default=0)
    senti_pos = models.IntegerField(default=0)
    senti_neg = models.IntegerField(default=0)
    senti_neut = models.IntegerField(default=0)
    word_from = models.CharField(default='', max_length=500)
    onlydate = models.DateTimeField(default=time.strftime('%Y-%m-%d'))
    date_time = models.DateTimeField(default=time.strftime('%Y-%m-%d %H:%M:%S'))

    def __unicode__(self):
        return self.word_name

class ytstats(models.Model):
    num_videos = models.IntegerField(default=0)
    subscribers = models.IntegerField(default=0)
    video_views = models.IntegerField(default=0)
    video_likes = models.IntegerField(default=0)
    onlydate = models.DateTimeField(default=time.strftime('%Y-%m-%d'))
    date_time = models.DateTimeField(default=time.strftime('%Y-%m-%d %H:%M:%S'))

    def __unicode__(self):
        return self.num_videos

class fbstats(models.Model):
    num_posts = models.IntegerField(default=0)
    page_likes = models.IntegerField(default=0)
    post_views = models.IntegerField(default=0)
    total_likes = models.IntegerField(default=0)
    onlydate = models.DateTimeField(default=time.strftime('%Y-%m-%d'))
    date_time = models.DateTimeField(default=time.strftime('%Y-%m-%d %H:%M:%S'))

    def __unicode__(self):
        return self.page_likes

class tstats(models.Model):
    num_videos = models.IntegerField(default=0)
    followers = models.IntegerField(default=0)
    retweets = models.IntegerField(default=0)
    total_favourites = models.IntegerField(default=0)
    onlydate = models.DateTimeField(default=time.strftime('%Y-%m-%d'))
    date_time = models.DateTimeField(default=time.strftime('%Y-%m-%d %H:%M:%S'))

    def __unicode__(self):
        return self.total_favourites

class wordlist(models.Model):
    word = models.CharField(max_length=100)

    def __unicode__(self):
        return self.word