from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$',views.cartList),
    url(r'^2/$',views.updateCount),
    url(r'^del/$',views.delUpdate),
    url(r'^ischeck/$',views.isCheck),
    url(r'^place_order1/',views.place_order1),
	url(r'^place_order2/',views.place_order2),
	url(r'^submit/',views.submit),
]