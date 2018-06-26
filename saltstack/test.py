#!/usr/bin/env python
# encoding: utf-8

"""
@author: lingxiangxinag 
@file: test.py
@time: 2018/6/22 上午11:32

"""
import json
import urllib2
from io import StringIO
import requests

# url = "http://118.25.138.208:8888/login"
# session = requests.session()
#
# headers = {"Accept": "application/json", 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',}
# data = {"username": "saltapi", "password": "saltapi",  "eauth": "pam"}
# r = session.post(url=url, data=data, headers=headers, verify=False)
# # r = session.post(url=url, data=data, headers=headers, cert=('localhost.crt', 'localhost_nopass.key'))
#
# print(r.status_code )
# print(r.text)
# print(json.loads(r.text).get("return")[0].get("token"))
# import urllib3
#
#
def excelModules(**kwargs):

    session = requests.session()
    headers = {
            "Accept": "application/json",
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',
            'X-Auth-Token': 'c8a164e86d6242a5c253f7a5230f9e8fc50d2c87',
        }
    header = {"Content-Type": "application/json", "Accept": "application/json",
              "X-Auth-Token": "c8a164e86d6242a5c253f7a5230f9e8fc50d2c87"}
    data = kwargs
    url = "http://118.25.138.208:8888"
    res = session.post(url=url, headers=headers, data=data)
    html = res.text
    print(json.loads(html))
    print(json.loads(html).get("return"))


if __name__ == '__main__':
    result = excelModules(client='local', tgt="*", fun="hello.hello", arg=['ajing', 15])



