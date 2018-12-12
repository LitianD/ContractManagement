"""ContractManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from ContractMis import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.login),
    url(r'^login$', views.login),
    url(r'^gaihetong/$', views.gaihetong),
    url(r'^gaihetong/submit$', views.gaihetong),
    url(r'^xiehetong/$', views.xiehetong),
    url(r'^.*/service/pricing$', views.pricing_view),
    url(r'^.*/service/agreement$', views.agreement_view),
    url(r'^hetongfanben/$', views.home),
    url(r'^zhuanlijishuxukehetong/$', views.zhuanlijishuxukehetong),
    url(r'^home/$', views.home),
    url(r'^logout/$', views.logout),
    url(r'^my/$', views.my),
    url(r'^.*.html$', views.home)
]