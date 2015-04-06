# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emailApp', '0002_email_textcleaned'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='removedContent',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
    ]
