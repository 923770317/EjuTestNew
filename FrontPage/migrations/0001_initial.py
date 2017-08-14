# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-14 04:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReleaseVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(max_length=20, verbose_name='\u6240\u5c5e\u9879\u76ee')),
                ('mod', models.CharField(max_length=20, verbose_name='\u6a21\u5757')),
                ('version', models.CharField(max_length=20, verbose_name='\u7248\u672c\u53f7')),
                ('lastOnLineDate', models.DateField()),
                ('remark', models.CharField(max_length=200, verbose_name='\u5907\u6ce8')),
            ],
        ),
    ]
