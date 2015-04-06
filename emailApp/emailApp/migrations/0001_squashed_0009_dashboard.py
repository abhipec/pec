# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    replaces = [(b'emailApp', '0001_initial'), (b'emailApp', '0002_email_textcleaned'), (b'emailApp', '0003_email_removedcontent'), (b'emailApp', '0004_auto_20150329_0757'), (b'emailApp', '0005_auto_20150329_1216'), (b'emailApp', '0006_auto_20150329_1251'), (b'emailApp', '0007_auto_20150329_1252'), (b'emailApp', '0008_auto_20150403_1346'), (b'emailApp', '0009_dashboard')]

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
                ('textPlain', models.TextField(null=True, blank=True)),
                ('textHtml', models.TextField(null=True, blank=True)),
                ('removedContentHtml', models.TextField(null=True, blank=True)),
                ('removedContentPlain', models.TextField(null=True, blank=True)),
                ('textCleanHtml', models.TextField(null=True, blank=True)),
                ('textCleanPlain', models.TextField(null=True, blank=True)),
                ('category', models.CharField(default=b'', max_length=15, choices=[(b'NULL', b'Not categorized'), (b'promotional', b'Promotional'), (b'spam', b'Spam'), (b'human', b'Human'), (b'notification', b'Notification'), (b'others', b'Others')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Dashboard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.TextField(null=True, blank=True)),
                ('timeStamp', models.DateTimeField()),
                ('validTill', models.DateTimeField()),
                ('source', models.OneToOneField(to='emailApp.Email')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
