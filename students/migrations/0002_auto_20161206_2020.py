# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Biblioteka',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, verbose_name='\u0406\u043c\u2019\u044f')),
                ('text', models.TextField(verbose_name='\u0442\u0435\u043a\u0441\u0442 \u043f\u043e\u0434\u0456\u0457')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Istoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, verbose_name='\u0406\u043c\u2019\u044f')),
                ('text', models.TextField(verbose_name='\u0442\u0435\u043a\u0441\u0442 \u043f\u043e\u0434\u0456\u0457')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Kolek',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, verbose_name='\u0406\u043c\u2019\u044f')),
                ('text', models.TextField(verbose_name='\u0442\u0435\u043a\u0441\u0442 \u043f\u043e\u0434\u0456\u0457')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Muzey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, verbose_name='\u0406\u043c\u2019\u044f')),
                ('text', models.TextField(verbose_name='\u0442\u0435\u043a\u0441\u0442 \u043f\u043e\u0434\u0456\u0457')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Psuholoh',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, verbose_name='\u0406\u043c\u2019\u044f')),
                ('text', models.TextField(verbose_name='\u0442\u0435\u043a\u0441\u0442 \u043f\u043e\u0434\u0456\u0457')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rozklad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, verbose_name='\u0406\u043c\u2019\u044f')),
                ('text', models.TextField(verbose_name='\u0442\u0435\u043a\u0441\u0442 \u043f\u043e\u0434\u0456\u0457')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vyhovna',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, verbose_name='\u0406\u043c\u2019\u044f')),
                ('text', models.TextField(verbose_name='\u0442\u0435\u043a\u0441\u0442 \u043f\u043e\u0434\u0456\u0457')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Zno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, verbose_name='\u0406\u043c\u2019\u044f')),
                ('text', models.TextField(verbose_name='\u0442\u0435\u043a\u0441\u0442 \u043f\u043e\u0434\u0456\u0457')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='podii',
            name='text',
            field=models.TextField(verbose_name='\u0442\u0435\u043a\u0441\u0442 \u043f\u043e\u0434\u0456\u0457'),
            preserve_default=True,
        ),
    ]
