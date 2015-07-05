# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tribble', '0003_auto_20150705_0858'),
    ]

    operations = [
        migrations.CreateModel(
            name='wordlist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('word', models.CharField(max_length=100)),
            ],
        ),
    ]
