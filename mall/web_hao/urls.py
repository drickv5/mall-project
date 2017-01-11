from django.conf.urls import include,url

urlpatterns = [
    url(r'^cart/',include('cart_kun.urls')),

]