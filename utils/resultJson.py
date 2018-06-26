#!/usr/bin/env python
# encoding: utf-8

"""
@author: lingxiangxinag 
@file: resultJson.py
@time: 2018/6/16 下午2:55

"""

from django.http import JsonResponse


class ResultBean(object):
    def  __init__(self):
        self.code = int()
        self.message = str()
        self.data = None

        self.jsonResult = {
            "code": self.code,
            "message": self.message,
            "data": self.data
        }

    def setCode(self, code):
        self.jsonResult.update({"code": code})

    def setMessage(self, message):
        self.jsonResult.update({"message": message})

    def setData(self, data):
        self.jsonResult.update({"data": data})