#coding=utf-8
from django.shortcuts import render
from django.core.paginator import  *
from models import *

#typeId :商品类别的id，
#pindex :页码
#sort:排序方式，默认为default，

def list(request):
	#使用GET属性，调取所需参数
	typeId = int(request.GET['typeId'])
	pindex = request.GET['pindex']
	sort = request.GET['sort']

	#判断typeId参数，如过为0则获取未删除的所有类别商品；判断sort参数，以确定商品展示顺序
	if typeId == 0:
		maxGoods = GoodsInfo.objects.filter(isDelete=False)
		if sort == 'default' or sort == '':
			goodsList = GoodsInfo.objects.filter(isDelete=False)
		elif sort == 'price':
			goodsList = GoodsInfo.objects.order_by('gprice').filter(isDelete=False)			
		elif sort == 'buycount':
			goodsList = GoodsInfo.objects.order_by('gbuycount').filter(isDelete=False)
	else:
		maxGoods = GoodsInfo.objects.filter(gtype_id=typeId,isDelete=False)
		if sort == 'default' or sort == '':			
			goodsList = GoodsInfo.objects.filter(gtype_id=typeId,isDelete=False)			
		elif sort == 'price':
			goodsList = GoodsInfo.objects.order_by('gprice').filter(gtype_id=typeId,isDelete=False)			
		elif sort == 'buycount':
			goodsList = GoodsInfo.objects.order_by('gbuycount').filter(gtype_id=typeId,isDelete=False)
			

	#商品列表	
	paginator = Paginator(goodsList,15)
	page = paginator.page(int(pindex))


	#新品推荐，查询id值最大的两个商品，以保证其为本品类最新的两个商品	
	count = maxGoods.count()
	maxGoodsList = maxGoods[(count-2):]
	maxGoods_1 = maxGoodsList[0]
	maxGoods_2 = maxGoodsList[1]

	context = {
		'page':page,
		'typeId':typeId,
		'pindex':pindex,
		'maxGoods_1':maxGoods_1,
		'maxGoods_2':maxGoods_2,
		'sort':sort,
	}
	return render(request,'goods_qi/list.html',context)





def detail(request):
	gid = request.GET['goodsId']
	sort = request.GET['sort']
	goods = GoodsInfo.objects.get(id=gid)
	print goods
	typeId = goods.gtype_id


	#userqiao
	if request.session.has_key('latest_goods_list'):
		latest_goods_list = request.session.get('latest_goods_list')
		latest_goods_list.insert(0, gid)
		request.session['latest_goods_list'] = latest_goods_list
	else:
		latest_goods_list = []
		latest_goods_list.insert(0,gid )
		request.session['latest_goods_list'] = latest_goods_list


	#新品推荐
	if typeId == '0':
		maxGoods = GoodsInfo.objects.filter(isDelete=False)
	else:
		maxGoods = GoodsInfo.objects.filter(gtype_id=typeId,isDelete=False)
	count = maxGoods.count()
	maxGoodsList = maxGoods[(count-2):]
	maxGoods_1 = maxGoodsList[0]
	maxGoods_2 = maxGoodsList[1]		
	


	context = {
		'goods':goods,
		'typeId':typeId,
		'sort':sort,
		'maxGoods_1':maxGoods_1,
		'maxGoods_2':maxGoods_2,

	}



	return render(request,'goods_qi/detail.html',context)

# def addCart(request):
# 	goodsId = request.GET['goodsId']
# 	count = request.GET['count']
	
