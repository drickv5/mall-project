from django.db import models

# Create your models here.
class CartInfo(models.Model):
    user = models.ForeignKey('UserInfo')#引入用户外键
    goods = models.ForeignKey('GoodsInfo')#引入商品外键
    count = models.IntegerField()#商品数量

class OrderInfo(models.Model):
    user = models.ForeignKey('UserInfo')#引入用户外键
    ototal = models.DecimalField(max_digits=7,decimal_places=2)#订单总价格
    state = models.BooleanField(default=0)#状态默认‘未支付’

class OrderDtailInfo(models.Model):
    order = models.ForeignKey('OrderInfo')#用表单外键做订单号
    goods = models.ForeignKey('GoodsInfo')#引用商品列表
    count = models.IntegerField()#商品数量
    price = models.DecimalField(max_digits=7,decimal_places=2)#商品单价

