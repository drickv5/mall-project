from django.conf.urls import url
import views

urlpatterns=[
	#url(r'^index/$',views.index),
	url(r'^list/$',views.list),
	url(r'^detail/$',views.detail),
	url(r'^addCart/$',views.addCart),
]