#coding=utf-8
from django.shortcuts import render,redirect
from models import *
from django.http import HttpResponse,JsonResponse

# Create your views here.

def cartList(request):
    list = CartInfo.objects.filter(user_id=1)
    context = {"list":list}
    return render(request,'cart.html',context)

def updateCount(request):
    print 'llll'
    cart_id = request.GET.get('cid')
    gcount = request.GET.get('gnum')
    print cart_id
    print gcount

    cartobj = CartInfo.objects.filter(id = cart_id)[0]
    cartobj.count = gcount
    cartobj.save()
    return HttpResponse(cartobj.count)

    # goodObj = GoodsInfo.objects.filter(goods_id = goodsid)[0]
    # goodscount = request.get['gcount']
    # user = UserInfo.objects.filter(pk=1)[0]
    # cartInfoObj =  CartInfo.objects.filter(user=user, gods=goodObj)
    # cartInfoObj.count = goodscount
    # cartInfoObj.save()

    # cartInfoObj =  CartInfo.objects.filter(user=user_id, gods=goodObj)
    # from django.http import JsonResponse
    #
    # return JsonResponse({'count': cartInfoObj.count})

def delUpdate(request):
    cart_id = request.GET.get('cid')
    cartobj = CartInfo.objects.filter(id = cart_id)[0]
    cartobj.delete()
    return  HttpResponse()

def isCheck(resquest):
    cart_id = resquest.GET.get('cid')
    ischeckobj = int(resquest.GET.get('checkobj'))
    cartobj = CartInfo.objects.filter(id = cart_id)[0]
    if ischeckobj==1:
        ischeck=True
        print (ischeck)
    else:
        ischeck=False
        print (ischeck)
    cartobj.ischeck = ischeck
    cartobj.save()
    return HttpResponse()


# -----------------------------
def place_order1(request):                           #立即购买跳转过来的
    user = request.session.get('uid',default='')     #session保持状态的key
    if user=='':
        return redirect('login.html')
    else:
        receInfo=UserInfo.objects.filter(id=user)

    a=request.GET['a']      #商品ID
    b=request.GET['b']		#商品数量

    #因为模板要保持一致，两个对象不一样，所以要先把这个商品对象存入购物车数据库然后引用
    cart=CartInfo()
    cart.user_id=user
    cart.goods_id=int(a)
    cart.count=int(b)
    cart.ischeck=True
    cart.save()


    #然后调用购物车里面的这个对象
    goodsInfo=CartInfo.objects.filter(goods_id=a).filter(check=True)

    totalnum=0
    totalprice=0
    for n in goodsInfo:
        totalprice=totalprice+(n.goods.gprice)*(n.count) #总金额结算
        totalnum=totalnum+(n.count)                      #商品总个数
    total_pay=10+totalprice                              #总金额（包含了邮费）
    context={"receInfo":list(receInfo),
             "goodsInfo":goodsInfo,
             "totalprice":totalprice,
             "totalnum":totalnum,
             "total_pay":total_pay,
             }
    return render(request,'place_order.html',context)


def place_order2(request):         #购物车跳转过来的页面
    user = request.session.get('uid',default='')  #session保持状态的key
    if user=='':
        return redirect('login.html')
    else:
    receInfo=UserInfo.objects.filter(id=user)
    goodsInfo=CartInfo.objects.filter(user_id=user).filter(ischeck=True)

    totalnum=0
    totalprice=0
    for n in goodsInfo:
        totalprice=totalprice+(n.goods.gprice)*(n.count) #总金额结算
        totalnum=totalnum+(n.count)                      #商品总个数
    total_pay=10+totalprice                              #总金额（包含了邮费）
    context={"receInfo":list(receInfo),
             "goodsInfo":goodsInfo,
             "totalprice":totalprice,
             "totalnum":totalnum,
             "total_pay":total_pay,
             }
    return render(request,'place_order.html',context)



def submit(request):
    user = request.session.get('uid',default='')
    receInfo=UserInfo.objects.filter(id=user)

#登录用户选中的购物车商品信息
    goodsInfo=CartInfo.objects.filter(user_id=user).filter(ischeck=True)

    totalnum=0
    totalprice=0
    for n in goodsInfo:
        totalprice=totalprice+(n.goods.gprice)*(n.count) #总金额结算
        totalnum=totalnum+(n.count)                      #商品总个数
    total_pay=10+totalprice                              #总金额（包含了邮费）

    #OrderInfo
    order=OrderInfo()
    order.user_id=user
    order.ototal=total_pay
    order.state=True
    order.save()


    #OrderDtailInfo
    for n in goodsInfo:
        detail_order=OrderDtailInfo()
        detail_order.order= order
        detail_order.goods= n.goods
        detail_order.count = n.count
        detail_order.price = n.goods.gprice
        detail_order.save()
        n.delete()                #提交保存订单信息后，删除购物车信息

    data = {'result': True}
    return JsonResponse(data)