# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Podii',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, verbose_name='\u0406\u043c\u2019\u044f')),
                ('text', models.TextField(max_length=256, verbose_name='\u0442\u0435\u043a\u0441\u0442 \u043f\u043e\u0434\u0456\u0457')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
