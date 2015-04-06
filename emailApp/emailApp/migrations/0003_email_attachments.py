# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emailApp', '0002_email_saved'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='attachments',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
