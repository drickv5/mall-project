#coding=utf-8

from django.shortcuts import redirect
def IsLogin(fun):
    def isLogin(request,*args,**kwargs):
        print('islogin')
        context={}
        if request.session.has_key('username'):
            context['uname']=request.session['username']
        return fun(request,context,*args,**kwargs)
    return isLogin

def RequireLogin(fun):
    def requireLogin(request,*args,**kwargs):
        print('requireLogin')
        if not request.session.has_key('username'):
            return redirect('login')
        else:
            return fun(request,*args,**kwargs)
    return requireLogin

