# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_auto_20150929_0331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='booker',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
