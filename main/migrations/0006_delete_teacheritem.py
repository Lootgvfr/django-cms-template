# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-07 13:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_quickphotoitem_teacheritem'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TeacherItem',
        ),
    ]
