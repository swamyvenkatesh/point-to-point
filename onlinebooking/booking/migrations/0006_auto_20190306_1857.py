# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-06 18:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_auto_20190218_1832'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartproducts',
            name='fare_reference',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='cartproducts',
            name='journey_index',
            field=models.IntegerField(default=0),
        ),
    ]
