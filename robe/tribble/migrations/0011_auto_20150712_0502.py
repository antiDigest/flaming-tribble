# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tribble', '0010_auto_20150712_0451'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fbstats',
            name='onlydate',
        ),
        migrations.RemoveField(
            model_name='tstats',
            name='onlydate',
        ),
        migrations.RemoveField(
            model_name='words_global',
            name='onlydate',
        ),
        migrations.RemoveField(
            model_name='words_india',
            name='onlydate',
        ),
        migrations.RemoveField(
            model_name='ytstats',
            name='onlydate',
        ),
    ]
