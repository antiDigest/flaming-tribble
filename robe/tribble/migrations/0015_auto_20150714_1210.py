# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tribble', '0014_auto_20150714_0835'),
    ]

    operations = [
        migrations.AddField(
            model_name='words_global',
            name='chart',
            field=models.CharField(default=None, max_length=1000),
        ),
        migrations.AddField(
            model_name='words_india',
            name='chart',
            field=models.CharField(default=None, max_length=1000),
        ),
        migrations.AlterField(
            model_name='fbstats',
            name='date_time',
            field=models.DateTimeField(default=b'2015-07-14 12:10:32'),
        ),
        migrations.AlterField(
            model_name='tstats',
            name='date_time',
            field=models.DateTimeField(default=b'2015-07-14 12:10:32'),
        ),
        migrations.AlterField(
            model_name='words_global',
            name='date_time',
            field=models.DateTimeField(default=b'2015-07-14 12:10:32'),
        ),
        migrations.AlterField(
            model_name='words_india',
            name='date_time',
            field=models.DateTimeField(default=b'2015-07-14 12:10:32'),
        ),
        migrations.AlterField(
            model_name='ytstats',
            name='date_time',
            field=models.DateTimeField(default=b'2015-07-14 12:10:32'),
        ),
    ]
