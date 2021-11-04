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
from django.urls import path
from app01 import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login),
    path('logout/', views.logout),
    path('index/', views.index),
    # path('layout/', views.layout),

    path('user/', views.user),
    path('add_user/', views.add_user),
    path('edit_user/<int:nid>/', views.edit_user),
    path('del_user/', views.del_user),

    path('fun1_project/', views.fun1_project),
    path('fun1_addproject/', views.fun1_addproject),
    path('fun1_editproject/<str:project_id>/', views.fun1_editproject),
    path('fun1_delproject/', views.fun1_delproject),

    path('fun2_samplehandover/', views.fun2_samplehandover),
    path('fun2_addsamplehandover/', views.fun2_addsamplehandover),
    path('fun2_editsamplehandover/<str:sample_ids>/', views.fun2_editsamplehandover),
    path('fun2_delsamplehandover/<str:sample_ids>/', views.fun2_delsamplehandover),

    path('fun2_sample/', views.fun2_sample),
    path('fun2_addsample/', views.fun2_addsample),
    path('fun2_editsample/<str:sample_id>/', views.fun2_editsample),
    path('fun2_delsample/<str:sample_id>/', views.fun2_delsample),

    path('fun21_sampletype/', views.fun21_sampletype),
    path('fun21_addsampletype/', views.fun21_addsampletype),
    path('fun21_editsampletype/<int:nid>/', views.fun21_editsampletype),
    path('fun21_delsampletype/', views.fun21_delsampletype),

    # path('fun3_result/', views.fun3_result),
    # path('fun3_addresult/', views.fun3_addresult),
    # path('fun3_editresult/<str:project_id>/', views.fun3_editresult),
    # path('fun3_delresult/', views.fun3_delresult),
]
