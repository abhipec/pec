# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emailApp', '0003_email_removedcontent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='removedContent',
        ),
        migrations.RemoveField(
            model_name='email',
            name='textCleaned',
        ),
        migrations.AddField(
            model_name='email',
            name='removedContentHtml',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='email',
            name='removedContentPlain',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='email',
            name='textCleanHtml',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='email',
            name='textCleanPlain',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
    ]
