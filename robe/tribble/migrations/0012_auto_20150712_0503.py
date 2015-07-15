# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tribble', '0011_auto_20150712_0502'),
    ]

    operations = [
        migrations.AddField(
            model_name='fbstats',
            name='onlydate',
            field=models.DateTimeField(default=b'2015-07-12'),
        ),
        migrations.AddField(
            model_name='tstats',
            name='onlydate',
            field=models.DateTimeField(default=b'2015-07-12'),
        ),
        migrations.AddField(
            model_name='words_global',
            name='onlydate',
            field=models.DateTimeField(default=b'2015-07-12'),
        ),
        migrations.AddField(
            model_name='words_india',
            name='onlydate',
            field=models.DateTimeField(default=b'2015-07-12'),
        ),
        migrations.AddField(
            model_name='ytstats',
            name='onlydate',
            field=models.DateTimeField(default=b'2015-07-12'),
        ),
        migrations.AddField(
            model_name='fbstats',
            name='date_time',
            field=models.DateTimeField(default=b'2015-07-12 05:03:18'),
        ),
        migrations.AddField(
            model_name='tstats',
            name='date_time',
            field=models.DateTimeField(default=b'2015-07-12 05:03:18'),
        ),
        migrations.AddField(
            model_name='words_global',
            name='date_time',
            field=models.DateTimeField(default=b'2015-07-12 05:03:18'),
        ),
        migrations.AddField(
            model_name='words_india',
            name='date_time',
            field=models.DateTimeField(default=b'2015-07-12 05:03:18'),
        ),
        migrations.AddField(
            model_name='ytstats',
            name='date_time',
            field=models.DateTimeField(default=b'2015-07-12 05:03:18'),
        ),
    ]
