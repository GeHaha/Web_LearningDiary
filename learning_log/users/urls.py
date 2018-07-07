# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 14:59:02 2018

@author: Administrator
"""

"""为应用程序users定义URL模式"""

from django.conf.urls import url
from django.contrib.auth.views import login
from . import views

urlpatterns = [
        #登陆页面
        url(r'^login/$', login, {'template_name': 'users/login.html'},
            name='login'),
            ]