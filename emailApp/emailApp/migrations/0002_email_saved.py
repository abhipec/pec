# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emailApp', '0001_squashed_0009_dashboard'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='saved',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
