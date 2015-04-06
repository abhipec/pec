# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emailApp', '0006_auto_20150329_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='removedContentHtml',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='email',
            name='removedContentPlain',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='email',
            name='textCleanHtml',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='email',
            name='textCleanPlain',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='email',
            name='textHtml',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='email',
            name='textPlain',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
