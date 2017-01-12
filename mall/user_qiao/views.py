#coding=utf-8
from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponseRedirect,HttpResponse

from models import *
from django.core.paginator import Paginator
from cart_kun.models import *
from goods_qi.models import *

def g_base(request):
     return render(request,'base/g_base.html')

def g_base_top(request):
    return render(request,'base/g_base_top.html')

def g_base_top_rightsearch(request):
    return  render(request,'base/g_base_top_rightsearch.html')

def user_center_info(request):
    return render(request,'./user_center_info.html')


def userinfo(request):
    # 创建一个商品列表 用于存储最近浏览的商品
    shoplist = []
    latest_goods_list_id = request.session.get('latest_goods_list')[:5]
    latest_goods_list = []
    for goods_id in latest_goods_list_id:
        goods = GoodsInfo.objects.get(id=goods_id)
        latest_goods_list.append(goods)
    context={'list':latest_goods_list }



    return render(request,'user/userinfo.html',context)

def userorder(request,pIndex):
    list1 = [1, 3, 3, 3, 3, 35,5,5,2,5,5,5,5,5,25,5,5,5,10,5,5,5,2,5,2]
    print(list1)
    p = Paginator(list1, 4)
    if pIndex == '':
        pIndex = '1'
    pIndex = int(pIndex)
    list2 = p.page(pIndex)
    plist = p.page_range
    # 根据登陆用户id查处他的订单
    orders = OrderInfo.objects.filter(user_id=1)

    # user_orders = orders.order_by(orders[1].ordernum)
    # print (orders.total)
    # 根据订单号查询订单详情

    # orderdet = OrderDetailInfo.objects.filter(order_id=orders.id)
    orderdet = OrderDtailInfo.objects.filter(order__id__in=[1,2,3,4])
    # print(len(orderdet))
    # print (orderdet.ordernum)
    # 根据订单详情查出对应商品
    # goods = OrderDetailInfo.objects.filter(goods__id__in=[0, 1, 2, 3, 4])

    # context = {'orders': orders, 'orderdet': orderdet, 'goods': goods}
    context = {'orders': orders, 'orderdet': orderdet,'list': list2, 'plist': plist, 'pIndex': pIndex}
    print list2
    return render(request,'user/userorder.html',context)

def usersite(request):
    return render(request,'user/usersite.html')


#用户收货地址
def postTest(request):
    # print ('aaaa')
    # 获取用户数据
    phone=request.POST['phone']
    # print("-------------------")
    recipients=request.POST['recipients']
    address=request.POST['address']
    # print (phone,recipients,address)
    # user=UserInfo.objects.get(pk=1)
    user = UserInfo()
    user.recipients=recipients
    user.address=address
    user.phone=phone
    user.save()
    # print(UserInfo.objects.all())

    return HttpResponseRedirect('/usersite/')


#用户全部订单
def userCenterOrder(request):
    # 根据登陆用户id查处他的订单
    orders = OrderInfo.objects.filter(user_id=1)
    print orders

    # user_orders = orders.order_by(orders[1].ordernum)
    # print (orders.total)

    # 根据订单号查询订单详情
    # orderdet = OrderDetailInfo.objects.filter(order__id__in=[1,2,3,4])
    orderdet = OrderDtailInfo.objects.filter(order__id=orders.id)[:4]
    # print(len(orderdet))
    # print (orderdet.ordernum)

    # 根据订单详情查出对应商品
    goods = OrderDtailInfo.objects.filter(goods__id__in=[0,1,2,3,4])
    # print(goods.goods.title)
    context = {'orders':orders,'orderdet':orderdet,'goods':goods}
    return  render(request,'userCenter/user_center_order.html',context)



