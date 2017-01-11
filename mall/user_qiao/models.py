#encoding=utf-8
from django.db import models
#encoding=utf-8
from django.db import models
from goods_qi.models import GoodsInfo




class UserInfo(models.Model):
    id = models.AutoField
    uname=models.CharField(max_length=40)#用户名
    upwd=models.CharField(max_length=50)#密码
    isDelete=models.BooleanField(default=False)#逻辑删除
    recipients=models.CharField(max_length=40)#收件人
    address=models.CharField(max_length=60)#收货地址
    phone=models.CharField(max_length=20)#联系电话

class cart(models.Model):
    num = models.IntegerField()
    user = models.ForeignKey(UserInfo)#引入用户外键
    goods_info = models.ForeignKey(GoodsInfo)#引入商品外键
    class Meta:
        db_table = 'cart'


class OrderInfo(models.Model):
    user = models.ForeignKey(UserInfo)#引入用户外键
    state = models.BooleanField()#状态默认‘未支付’
    total = models.DecimalField(max_digits=5,decimal_places=2)#订单总价
    ordernum = models.CharField(max_length=20)#订单编号
    bpub_date = models.DateTimeField()#订单日期
    class Meta:
        db_table = 'OrderInfo'
    #目的是把价格转为字符串不出现中文
    def __str__(self):
        return str(self.total).encode('utf-8')

class OrderDetailInfo(models.Model):
    order = models.ForeignKey(OrderInfo)#用表单外键做订单号
    goods = models.ForeignKey(GoodsInfo)#引用商品列表
    goods_price = models.DecimalField(max_digits=5,decimal_places=2)#商品单价
    count = models.DecimalField(max_digits=5,decimal_places=2)#商品数量
    class Meta:
        db_table = 'OrderDetailInfo'



