# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_qiao', '0001_initial'),
        ('goods_qi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.IntegerField()),
                ('goods', models.ForeignKey(to='goods_qi.GoodsInfo')),
                ('user', models.ForeignKey(to='user_qiao.UserInfo')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDtailInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.IntegerField()),
                ('price', models.DecimalField(max_digits=7, decimal_places=2)),
                ('goods', models.ForeignKey(to='goods_qi.GoodsInfo')),
            ],
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ototal', models.DecimalField(max_digits=7, decimal_places=2)),
                ('state', models.BooleanField(default=0)),
                ('user', models.ForeignKey(to='user_qiao.UserInfo')),
            ],
        ),
        migrations.AddField(
            model_name='orderdtailinfo',
            name='order',
            field=models.ForeignKey(to='cart_kun.OrderInfo'),
        ),
    ]
