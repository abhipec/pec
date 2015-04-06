# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emailApp', '0008_auto_20150403_1346'),
    ]

    operations = [
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
