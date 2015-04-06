# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emailApp', '0004_auto_20150329_0757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='isPromotional',
        ),
        migrations.AddField(
            model_name='email',
            name='category',
            field=models.CharField(default=b'', max_length=15, choices=[(b'', b''), (b'promotional', b'Promotional'), (b'spam', b'Spam'), (b'human', b'Human'), (b'others', b'Others')]),
            preserve_default=True,
        ),
    ]
