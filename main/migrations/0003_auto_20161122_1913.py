# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-22 19:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20161122_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacante',
            name='aplicantes',
            field=models.ManyToManyField(blank=True, null=True, related_name='vacantes', to=settings.AUTH_USER_MODEL),
        ),
    ]
