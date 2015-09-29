# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='booker',
            field=models.CharField(default='aaaa', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='schedule',
            unique_together=set([('tutor', 'time')]),
        ),
    ]
