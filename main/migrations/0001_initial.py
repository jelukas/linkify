# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('short_url', models.CharField(max_length=10)),
                ('url', models.CharField(max_length=255)),
                ('title', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
