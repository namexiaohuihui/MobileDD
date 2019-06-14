# -*- coding: utf-8 -*-

# @author:  dingdong
# @license: (C) Copyright 2016-2019, Ding dong online.
# @software: PyCharm
# @file:  demo_test1.py
# @time: 2019/4/28 10:30
# @Software: PyCharm
# @Site    : 
# @desc:
import requests
import time
import json
import base64

# # 接口的url
# url = "https://hospcardcenter.healthan.net/api"
#
# # 接口的参数
#
#
#
# s = json.dumps(params)
# encodestr = base64.b64encode(s.encode('utf-8'))
# print(encodestr)
# ss = "eyJtZXRob2QiOiJDYXJkQmluZCIsImhvc3BfaWQiOiI1IiwiZGF0YSI6eyJtaW5pX29wZW5pZCI6Im9jYVNwNVFVX0Q1aTNYb2lqWlFlWmV6MjQ1TE0iLCJtb2JpbGUiOiLlup/ni5ciLCJuYW1lIjoi546L5a+TIiwiaWRjYXJkIjoiIiwicGF0aWVudElkIjoiMDAwMDIwMzgzOTAwIiwic21zY29kZSI6IuaWueazlSJ9LCJkYXRldGltZSI6MTU1NjQzNTEzMSwic2lnbiI6IjU3Y2ViYTFjZDRiYjU4MDUzNmYzMTk5ZDEwYjM2NjcyIn0="
# r = requests.request("post", url, headers=headers, params=encodestr)
# # 打印返回结果
# params_text = r.text
# print(params_text)

params_text = "eyJjb2RlIjoxLCJtc2ciOiLmj5DkuqTph5Hpop3plJnor68iLCJlcnJvcl9jb2RlIjowLCJlcnJvcl9tc2ciOiIiLCJkYXRhIjoiIiwicmV0dXJuX3RpbWUiOjE1NTY1Mjg1ODkzMDY5Ljc0OH0="
params_text = json.loads(base64.b64decode(params_text))
# params_text['data']['fee'] = '1'
import pprint
pprint.pprint(params_text)

params_text = json.dumps(params_text)
encodestr = base64.b64encode(params_text.encode('utf-8'))
print(encodestr)

