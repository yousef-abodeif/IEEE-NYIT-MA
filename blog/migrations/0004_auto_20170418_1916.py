# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-18 19:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170327_1539'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=3000)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]