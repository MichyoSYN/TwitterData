# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Twitter',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('text_content', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('event', models.CharField(default=b'test', max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
