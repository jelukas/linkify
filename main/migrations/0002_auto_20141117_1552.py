# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetaUrl',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(verbose_name=b'New Title')),
                ('description', models.TextField(verbose_name=b'New Description')),
                ('image', models.URLField(verbose_name=b'Social Image')),
                ('url', models.OneToOneField(related_name='meta_url', to='main.Url')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='url',
            name='title',
        ),
    ]
