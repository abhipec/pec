# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emailApp', '0005_auto_20150329_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='category',
            field=models.CharField(default=b'', max_length=15, choices=[(b'', b''), (b'promotional', b'Promotional'), (b'spam', b'Spam'), (b'human', b'Human'), (b'notification', b'Notification'), (b'others', b'Others')]),
            preserve_default=True,
        ),
    ]
