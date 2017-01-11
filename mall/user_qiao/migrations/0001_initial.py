# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods_qi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num', models.IntegerField()),
                ('goods_info', models.ForeignKey(to='goods_qi.GoodsInfo')),
            ],
            options={
                'db_table': 'cart',
            },
        ),
        migrations.CreateModel(
            name='OrderDetailInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('goods_price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('count', models.DecimalField(max_digits=5, decimal_places=2)),
                ('goods', models.ForeignKey(to='goods_qi.GoodsInfo')),
            ],
            options={
                'db_table': 'OrderDetailInfo',
            },
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.BooleanField()),
                ('total', models.DecimalField(max_digits=5, decimal_places=2)),
                ('ordernum', models.CharField(max_length=20)),
                ('bpub_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'OrderInfo',
            },
        ),
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
        migrations.AddField(
            model_name='orderinfo',
            name='user',
            field=models.ForeignKey(to='user_qiao.UserInfo'),
        ),
        migrations.AddField(
            model_name='orderdetailinfo',
            name='order',
            field=models.ForeignKey(to='user_qiao.OrderInfo'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(to='user_qiao.UserInfo'),
        ),
    ]
