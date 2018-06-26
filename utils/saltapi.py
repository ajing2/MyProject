#!/usr/bin/env python
# encoding: utf-8

"""
@author: lingxiangxinag 
@file: saltapi.py
@time: 2018/6/22 下午2:36

"""
import json

import requests


class SaltHttp(object):
    def __init__(self):
        self.session = requests.session()
        self.token = self.getToken()

    def getToken(self):
        url = "http://118.25.138.208:8888/login"
        headers = {
            "Accept": "application/json",
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'
        }
        data = {"username": "saltapi", "password": "saltapi", "eauth": "pam"}
        res = self.session.post(url=url, data=data, headers=headers)
        token = json.loads(res.text().get("return")[0].get("token"))
        return token

    def execlModules(self, **kwargs):
        headers = {
            "Accept": "application/json",
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',
            'X-Auth-Token':self.token,
        }
        url = "http://118.25.138.208:8888"
        res = self.session.post(url=url, headers=headers, data=kwargs)
        html = json.loads(res.text.get("return"))
        if html.get("return"):
            return html.get("return")
        else:
            return "error"



