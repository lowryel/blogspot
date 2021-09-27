# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-09-24 10:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blogModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=200)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='img')),
            ],
        ),
    ]
