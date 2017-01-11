from django.conf.urls import include, url
from django.contrib import admin
import views
urlpatterns = [
    url(r'^g_base/$', views.g_base),
    url(r'^g_base_top/$', views.g_base_top),
    # url(r'^g_base_top_centersearch', views.g_base_top_centersearch),
    url(r'^g_base_top_rightsearch/$', views.g_base_top_rightsearch),
    # url(r'^g_base_top_rightsearch_usercenter', views.g_base_top_rightsearch_usercenter),
    url(r'^user_center_info/$',views.user_center_info),
    # url(r'^user_center_order',views.user_center_oreder),
    # url(r'^user_center_site',views.user_center_site),
    url(r'^userinfo/',views.userinfo),
    url(r'^userorder/(\d*)',views.userorder),
    url(r'^usersite/',views.usersite),
    url(r'^postTest/', views.postTest),
    # url(r'^(\d*)/',views.pagTest),
]