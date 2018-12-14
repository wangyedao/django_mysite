# -*- coding: utf-8 -*-
# @Time    : 2018/12/13 14:40
# @Author  : 赵利涵
# @Email   : zhaolihan168@163.com
# @File    : urls.py.py
from django.urls import path
from .import views
urlpatterns = [
    path('',views.index, name='index'),
    path('index',views.index,name='index')
]
#先引入视图函数
# path（）函数定义的路由最终都会在启东时加载
# path（路由规则)