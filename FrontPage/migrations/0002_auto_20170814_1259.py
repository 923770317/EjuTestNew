# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-14 04:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FrontPage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='releaseversion',
            name='remark',
            field=models.CharField(max_length=200, null=True, verbose_name='\u5907\u6ce8'),
        ),
    ]
