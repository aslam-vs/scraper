# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrap', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='height',
            field=models.CharField(default=1, max_length=11, verbose_name='Height'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='images',
            name='page',
            field=models.ForeignKey(default=1, to='scrap.Page'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='images',
            name='width',
            field=models.CharField(default=1, max_length=11, verbose_name='Width'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='page',
            name='link_url',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
