from django.conf.urls import include, url
import views

urlpatterns=[
        url(r'^login$',views.login),
        url(r'^$',views.index),
        url(r'^index$',views.index),
        url(r'^register$',views.register),
        url(r'^login_handle/$',views.login_handle),

  ]
