# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('messageId', models.SlugField(unique=True, max_length=100)),
                ('sender', models.EmailField(max_length=254)),
                ('timeStamp', models.DateTimeField()),
                ('subject', models.CharField(max_length=998, null=True)),
                ('textPlain', models.TextField()),
                ('textHtml', models.TextField()),
                ('isPromotional', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
