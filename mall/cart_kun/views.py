from django.shortcuts import render
from models import *

# Create your views here.

def cartList(request):
    list = CartInfo.objects.filter(user_id=1)
    context = {"list":list}
    return render(request,'cart.html',context)