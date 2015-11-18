# -*- coding: utf-8 -*-
# Generated by Django 1.9c1 on 2015-11-17 09:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminders_calls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='state',
            field=models.IntegerField(choices=[(0, b'failed'), (10, b'dialing'), (20, b'answered'), (30, b'busy'), (40, b'no_answer'), (50, b'unknown')], default=10),
        ),
        migrations.AlterField(
            model_name='call',
            name='twilio_sid',
            field=models.CharField(default=None, max_length=34, null=True, unique=True),
        ),
    ]