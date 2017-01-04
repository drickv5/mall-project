#coding=utf-8
from django.db import models

# Create your models here.


class TypeInfo(models.Model):
	ttitle = models.CharField(max_length=20)                 #商品类别
	isDelete = models.BooleanField(default=False)            #isDelete



class GoodsInfo(models.Model):
	gtitle = models.CharField(max_length=20)                 #商品名称
	gresume = models.CharField(max_length=300)               #商品摘要
	gdesc = models.CharField(max_length=500)                 #商品详情描述
	gimg = models.CharField(max_length=100)                  #商品图片路径
	gunit = models.CharField(max_length=20)                  #商品规格
	gprice = models.DecimalField(max_digits=6,decimal_places=2)#商品价格
	gbuycount = models.IntegerField()                        #商品人气（购买次数）
	gtype = models.ForeignKey('TypeInfo')                    #商品类别（外键）
	isDelete = models.BooleanField(default=False)            #isDelete


