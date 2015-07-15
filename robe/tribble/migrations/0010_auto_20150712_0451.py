# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tribble', '0009_auto_20150711_1707'),
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
    ]
