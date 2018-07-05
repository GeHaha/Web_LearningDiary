# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 16:20:12 2018

@author: Administrator
"""

"""定义learning_logs的url模式"""
from django.conf.urls import url
from . import views
urlpatterns = [
        #主页
        url(r'^$',views.index, name='index'),
        #显示所有的主题
        url(r'^topics/$', views.topics, name='topics'),

        ]