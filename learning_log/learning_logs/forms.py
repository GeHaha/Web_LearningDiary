# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 22:05:39 2018

@author: Administrator
"""

from django import forms
from .models import Topic

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text':''}