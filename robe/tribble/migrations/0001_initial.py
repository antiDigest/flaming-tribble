# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fbstats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num_posts', models.IntegerField(default=0)),
                ('page_likes', models.IntegerField(default=0)),
                ('post_views', models.IntegerField(default=0)),
                ('total_likes', models.IntegerField(default=0)),
                ('date_time', models.DateField(default=b'2015-07-05')),
            ],
        ),
        migrations.CreateModel(
            name='tstats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num_videos', models.IntegerField(default=0)),
                ('followers', models.IntegerField(default=0)),
                ('retweets', models.IntegerField(default=0)),
                ('total_favourites', models.IntegerField(default=0)),
                ('date_time', models.DateField(default=b'2015-07-05')),
            ],
        ),
        migrations.CreateModel(
            name='Words_Global',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('word_name', models.CharField(max_length=200)),
                ('frequency', models.IntegerField(default=1)),
                ('trend', models.IntegerField(default=3, verbose_name=[1, 2])),
                ('sentiment', models.IntegerField(default=1, verbose_name=[0, 1])),
                ('word_from', models.CharField(default=b'', max_length=500)),
                ('date_time', models.DateField(default=b'2015-07-05')),
            ],
        ),
        migrations.CreateModel(
            name='Words_India',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('word_name', models.CharField(max_length=200)),
                ('frequency', models.IntegerField(default=1)),
                ('trend', models.IntegerField(default=3, verbose_name=[1, 2])),
                ('sentiment', models.IntegerField(default=1, verbose_name=[0, 1])),
                ('word_from', models.CharField(default=b'', max_length=500)),
                ('date_time', models.DateField(default=b'2015-07-05')),
            ],
        ),
        migrations.CreateModel(
            name='ytstats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num_videos', models.IntegerField(default=0)),
                ('subscribers', models.IntegerField(default=0)),
                ('video_views', models.IntegerField(default=0)),
                ('video_likes', models.IntegerField(default=0)),
                ('date_time', models.DateField(default=b'2015-07-05')),
            ],
        ),
    ]
