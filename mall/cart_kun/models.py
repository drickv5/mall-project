#encoding=utf-8
from django.db import models
from goods_qi.models import GoodsInfo
from user_qiao.models import UserInfo
from datetime import datetime
from random import randint

# Create your models here.
class CartInfo(models.Model):
    user = models.ForeignKey(UserInfo)#引入用户外键
    goods = models.ForeignKey(GoodsInfo)#引入商品外键
    count = models.IntegerField()#商品数量
    ischeck = models.BooleanField(default=0)  #选中状态默认为1（选中）

class OrderInfo(models.Model):
    #订单编号
    id = models.CharField('订单编号', max_length=31, primary_key=True, null=False)
    #引入用户外键
    user = models.ForeignKey(UserInfo)
    #订单总价格
    ototal = models.DecimalField(max_digits=7,decimal_places=2)
    # 订单生成时间
    createdTime = models.DateTimeField('创建时间',auto_now_add=True)
    #状态默认‘未支付’
    state = models.BooleanField(default=0)

    def save(self):
        if not self.id:
            now = datetime.now()
            # 自动生成订单编号
            self.id = '{0}{1:0>2}{2:0>2}{3:0>2}{4:0>2}{5:0>2}{6:0>6}'.format(
                now.year,now.month,now.day,now.hour,now.minute,now.second,randint(0,999999))
            super(OrderInfo, self).save()    # 最后调用父类save方法

class OrderDtailInfo(models.Model):
    order = models.ForeignKey(OrderInfo)#引入order外键
    goods = models.ForeignKey(GoodsInfo)#引用商品列表
    count = models.IntegerField()#商品数量
    price = models.DecimalField(max_digits=7,decimal_places=2)#商品单价
