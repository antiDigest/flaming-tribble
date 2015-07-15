# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tribble', '0005_auto_20150709_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='words_global',
            name='url',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AddField(
            model_name='words_india',
            name='url',
            field=models.CharField(default=None, max_length=500),
        ),
    ]
