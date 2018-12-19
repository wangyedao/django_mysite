# -*- coding: utf-8 -*-

from django.urls import path
from .import views
app_name='polls'
urlpatterns = [
    # 首页http://ip:port/polls/
    path('',views.index, name='index'),
    # 首页问题列表/polls/index/
    path('index',views.index,name='index'),
    # 问题详细页ex:/polls/1/
    path('<int:question_id>/',views.detail,name='detail'),
    # 投票结果页/polls/2/results/
    path('<int:question_id>/results/',views.results,name='results'),
    # 去投票，选项技术+1 /polls/5/vote/
    path('<int:question_id>/vote/',views.vote,name='vote'),
    #通用视图示例
    path('simple/',views.SimpleView.as_view(),name='simple')
]
#先引入视图函数
# path（）函数定义的路由最终都会在启东时加载
# # path（路由规则)
# 1.xx版本的路由写法是正则风格
# from django.conf.urls import url
# urlpatterns=[
#     url(r'^$',views.index,name='index'),
#     url(r'^index$',views.index),
# ]