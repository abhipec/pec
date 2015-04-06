# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emailApp', '0005_auto_20150406_1708'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='removedContentHtml',
        ),
        migrations.RemoveField(
            model_name='email',
            name='removedContentPlain',
        ),
        migrations.RemoveField(
            model_name='email',
            name='saved',
        ),
    ]
