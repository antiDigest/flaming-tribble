# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tribble', '0012_auto_20150712_0503'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='words_global',
            name='sentiment',
        ),
        migrations.RemoveField(
            model_name='words_global',
            name='url',
        ),
        migrations.RemoveField(
            model_name='words_india',
            name='sentiment',
        ),
        migrations.RemoveField(
            model_name='words_india',
            name='url',
        ),
        migrations.AddField(
            model_name='words_global',
            name='senti_neg',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='words_global',
            name='senti_neut',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='words_global',
            name='senti_pos',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='words_india',
            name='senti_neg',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='words_india',
            name='senti_neut',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='words_india',
            name='senti_pos',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='fbstats',
            name='date_time',
            field=models.DateTimeField(default=b'2015-07-14 08:32:19'),
        ),
        migrations.AlterField(
            model_name='fbstats',
            name='onlydate',
            field=models.DateTimeField(default=b'2015-07-14'),
        ),
        migrations.AlterField(
            model_name='tstats',
            name='date_time',
            field=models.DateTimeField(default=b'2015-07-14 08:32:19'),
        ),
        migrations.AlterField(
            model_name='tstats',
            name='onlydate',
            field=models.DateTimeField(default=b'2015-07-14'),
        ),
        migrations.AlterField(
            model_name='words_global',
            name='date_time',
            field=models.DateTimeField(default=b'2015-07-14 08:32:19'),
        ),
        migrations.AlterField(
            model_name='words_global',
            name='onlydate',
            field=models.DateTimeField(default=b'2015-07-14'),
        ),
        migrations.AlterField(
            model_name='words_india',
            name='date_time',
            field=models.DateTimeField(default=b'2015-07-14 08:32:19'),
        ),
        migrations.AlterField(
            model_name='words_india',
            name='onlydate',
            field=models.DateTimeField(default=b'2015-07-14'),
        ),
        migrations.AlterField(
            model_name='ytstats',
            name='date_time',
            field=models.DateTimeField(default=b'2015-07-14 08:32:19'),
        ),
        migrations.AlterField(
            model_name='ytstats',
            name='onlydate',
            field=models.DateTimeField(default=b'2015-07-14'),
        ),
    ]
