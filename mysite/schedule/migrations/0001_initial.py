# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(verbose_name=b'time')),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('time_available', models.ManyToManyField(to='schedule.TimeTable', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='schedule',
            name='time',
            field=models.ForeignKey(to='schedule.TimeTable', null=True),
        ),
        migrations.AddField(
            model_name='schedule',
            name='tutor',
            field=models.ForeignKey(to='schedule.Tutor', null=True),
        ),
    ]
