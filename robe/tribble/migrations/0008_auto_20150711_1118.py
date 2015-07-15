# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tribble', '0007_auto_20150711_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fbstats',
            name='date_time',
            field=models.DateTimeField(default=b'2015-07-07 11:18:25'),
        ),
        migrations.AlterField(
            model_name='tstats',
            name='date_time',
            field=models.DateTimeField(default=b'2015-07-07 11:18:25'),
        ),
        migrations.AlterField(
            model_name='words_global',
            name='date_time',
            field=models.DateTimeField(default=b'2015-07-07 11:18:25'),
        ),
        migrations.AlterField(
            model_name='words_india',
            name='date_time',
            field=models.DateTimeField(default=b'2015-07-07 11:18:25'),
        ),
        migrations.AlterField(
            model_name='ytstats',
            name='date_time',
            field=models.DateTimeField(default=b'2015-07-07 11:18:25'),
        ),
    ]
