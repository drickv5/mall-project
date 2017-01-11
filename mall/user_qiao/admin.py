from django.contrib import admin
from models import *
from goods_qi.models import *


class User_admin(admin.ModelAdmin):
    list_display = ['id','uname']


admin.site.register(UserInfo,User_admin)

