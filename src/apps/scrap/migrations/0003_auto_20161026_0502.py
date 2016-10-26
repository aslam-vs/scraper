# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrap', '0002_auto_20161026_0459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='og_title',
            field=models.CharField(max_length=255, null=True, verbose_name='Og Title', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(max_length=255, null=True, verbose_name='Title', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='twitter_title',
            field=models.CharField(max_length=255, null=True, verbose_name='Twitter Title', blank=True),
            preserve_default=True,
        ),
    ]
