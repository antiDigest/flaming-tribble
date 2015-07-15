# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tribble', '0015_auto_20150714_1210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='words_global',
            name='chart',
        ),
        migrations.RemoveField(
            model_name='words_india',
            name='chart',
        ),
        migrations.AlterField(
            model_name='fbstats',
            name='date_time',
            field=models.DateTimeField(default=b'2015-07-14 18:06:21'),
        ),
        migrations.AlterField(
            model_name='tstats',
            name='date_time',
            field=models.DateTimeField(default=b'2015-07-14 18:06:21'),
        ),
        migrations.AlterField(
            model_name='words_global',
            name='date_time',
            field=models.DateTimeField(default=b'2015-07-14 18:06:21'),
        ),
        migrations.AlterField(
            model_name='words_india',
            name='date_time',
            field=models.DateTimeField(default=b'2015-07-14 18:06:21'),
        ),
        migrations.AlterField(
            model_name='ytstats',
            name='date_time',
            field=models.DateTimeField(default=b'2015-07-14 18:06:21'),
        ),
    ]
