"""hptest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
# from django.urls import path
from app01 import views
from django.conf.urls import url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', views.login),
    url(r'^logout/', views.logout),
    url(r'^index/', views.index),
    # url(r'^layout/', views.layout),

    url(r'^user/', views.user),
    url(r'^add_user/', views.add_user),
    url(r'^edit_user/(\d+)/', views.edit_user),
    url(r'^del_user/', views.del_user),

    url(r'^fun1_project/', views.fun1_project),
    url(r'^fun1_addproject/', views.fun1_addproject),
    url(r'^fun1_editproject/(\d+)/', views.fun1_editproject),
    url(r'^fun1_delproject/', views.fun1_delproject),

    # url(r'^fun2_sample/', views.fun2_sample),
    # url(r'^fun2_addsample/', views.fun2_addsample),
    # url(r'^fun2_editsample/(\d+)/', views.fun2_editsample),
    # url(r'^fun2_delsample/', views.fun2_delsample),
    #
    # url(r'^fun21_sampletype/', views.fun21_sampletype),
    # url(r'^fun21_addsampletype/', views.fun21_addsampletype),
    # url(r'^fun21_editsampletype/(\d+)/', views.fun21_editsampletype),
    # url(r'^fun21_delsampletype/', views.fun21_delsampletype),
    #
    # url(r'^fun3_result/', views.fun3_result),
    # url(r'^fun3_addresult/', views.fun3_addresult),
    # url(r'^fun3_editresult/(\d+)/', views.fun3_editresult),
    # url(r'^fun3_delresult/', views.fun3_delresult),
]