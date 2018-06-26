#!/usr/bin/env python
# encoding: utf-8

"""
@author: lingxiangxinag 
@file: forms.py
@time: 2018/6/16 下午2:39

"""
from django import forms

class AddAppForm(forms.Form):
    ip = forms.CharField(max_length=20)
    app = forms.CharField(max_length=50)

class CheckAppForm(forms.Form):
    ip = forms.CharField(max_length=20)
    app = forms.CharField(max_length=50)
    tool = forms.CharField(max_length=2)