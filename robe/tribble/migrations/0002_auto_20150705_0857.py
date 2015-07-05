# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tribble', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='words_global',
            name='sentiment',
            field=models.IntegerField(default=2, verbose_name=[0, 2]),
        ),
    ]
