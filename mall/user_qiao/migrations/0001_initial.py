# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uname', models.CharField(max_length=40)),
                ('upwd', models.CharField(max_length=50)),
                ('isDelete', models.BooleanField(default=False)),
                ('recipients', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=60)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
    ]
