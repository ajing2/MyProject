#!/usr/bin/env python
# encoding: utf-8

"""
@author: lingxiangxinag 
@file: serializers.py
@time: 2018/6/16 下午2:24

"""
from rest_framework import serializers

from saltstack.models import App


class AppSerializer(serializers.ModelSerializer):

    class Meta:
        model = App
        fields = "__all__"
