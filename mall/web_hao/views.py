#coding=utf-8
from django.shortcuts import render,redirect
from django.http import  HttpResponse, HttpResponseRedirect
from hashlib import sha1
from goods_qi.models import  GoodsInfo
from web_hao.Decorator import  *
from user_qiao.models import UserInfo

#主页
@IsLogin
def index(request,context):
    b1=GoodsInfo.objects.filter(isDelete = False,gtype = 1)
    num = b1.count()
    list1 =b1[num-4:]

    b2 = GoodsInfo.objects.filter(isDelete=False, gtype=2)
    num = b2.count()
    list2 = b2[num-4:]

    b3 = GoodsInfo.objects.filter(isDelete=False, gtype=3)
    num = b3.count()
    list3 = b3[num-4:]

    b4 = GoodsInfo.objects.filter(isDelete=False, gtype=4)
    num = b4.count()
    list4 = b4[num-4:]

    b5 = GoodsInfo.objects.filter(isDelete=False, gtype=5)
    num = b5.count()
    list5 = b5[num-4:]

    b6 = GoodsInfo.objects.filter(isDelete=False, gtype=6)
    num = b6.count()
    list6 = b6[num-4:]
    context['list1']=list1
    context['list2'] = list2
    context['list3'] = list3
    context['list4'] = list4
    context['list5'] = list5
    context['list6'] = list1

    return render(request, 'index.html', context)

#登陆页面
def login(request):
    return render(request, 'login.html')

#登陆加密转向功能
def login_handle(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        suname = request.POST['username']
        supwd = request.POST['pwd']
        s1 = sha1()
        s1.update(supwd)
        sspwdSha1 = s1.hexdigest()
        usd = UserInfo.objects.filter(uname=suname)
        if usd:
            if usd[0].upwd == sspwdSha1:
                request.session['username'] = suname
                request.session.set_expiry(0)
                return redirect('/mall/index')
            else:
                return HttpResponse('输入的密码有误')
        else:
            return render(request, 'login.html')

#注销页面
def logout(request):
    request.session.flush()
    return redirect('/mall/index')



#注册页面
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        uname = request.POST['user_name']
        upwd = request.POST['pwd']
        sname = UserInfo.objects.filter(uname=uname)
        if sname:
            return HttpResponse('你输入的用户名已经存在')
        else:
            s1 = sha1()
            s1.update(upwd)
            spwdSha1 = s1.hexdigest()
            user=UserInfo.objects.create(uname=uname,upwd=spwdSha1)
            user.save()
            return HttpResponse('注册成功')










