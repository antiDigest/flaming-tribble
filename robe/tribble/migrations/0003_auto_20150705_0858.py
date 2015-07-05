# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tribble', '0002_auto_20150705_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='words_india',
            name='sentiment',
            field=models.IntegerField(default=2, verbose_name=[0, 2]),
        ),
    ]
