from django.contrib import admin
from models import *
from goods_qi.models import *


class User_admin(admin.ModelAdmin):
    list_display = ['id','uname']



admin.site.register(UserInfo,User_admin)
admin.site.register(OrderInfo)
admin.site.register(OrderDetailInfo)
admin.site.register(cart)
admin.site.register(GoodsInfo)
admin.site.register(TypeInfo)