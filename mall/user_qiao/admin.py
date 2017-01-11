from django.contrib import admin
from models import *
from goods_qi.models import *


class User_admin(admin.ModelAdmin):
    list_display = ['id','uname']



<<<<<<< HEAD
admin.site.register(UserInfo,User_admin)
=======
admin.site.register(UserInfo,User_admin)
>>>>>>> d9e08dcd3beb2f2ea099bd8ca17d79f6a76d4d5d
