# -*- coding: utf-8 -*-

# @author:  dingdong
# @license: (C) Copyright 2016-2019, Ding dong online.
# @software: PyCharm
# @file:  __init__.py.py
# @time: 2019/4/28 10:29
# @Software: PyCharm
# @Site    : 
# @desc:
#- * - coding: utf - 8 -
import requests
import base64
import json
params = {
    "method":"CardBind",
    "hosp_id":"5",
    "data":
        {
            "mini_openid":"ocaSp5QU_D5i3XoijZQeZez245LM",
            "mobile":"记得记得计算机",
            "name":"王寓",
            "idcard":"",
            "patientId":"000020383900",
            "smscode":"你的内心那些那你"
        },
    "datetime":1556419247,
    "sign":"f408af7bd3252d9d27041fb9e0b3cdb4"
}
s = json.dumps(params)
print(type(s))


#json串转换成base64（转码）
encodestr = base64.b64encode(s.encode('utf-8'))
print(encodestr)
print(str(encodestr,'utf-8'))
#base64转换成json（解码）
ww=base64.b64decode(encodestr)
print(str(ww,'utf-8'))