# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emailApp', '0004_auto_20150405_1641'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='rules',
        ),
        migrations.AddField(
            model_name='rule',
            name='ruleType',
            field=models.CharField(default=b'', max_length=20, choices=[(b'', b''), (b'category', b'Category'), (b'sender', b'Sender')]),
            preserve_default=True,
        ),
    ]
