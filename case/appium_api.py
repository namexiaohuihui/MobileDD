# -*- coding: utf-8 -*-

# @author:  ln_company
# @license: (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
# @software: PyCharm
# @file:  appium_api.py
# @time: 2019/3/3 15:32
# @Software: PyCharm
# @Site    : 
# @desc:

class AppiumApi():
    def __init__(self,driver):
        self.driver = driver

    def huadong(self):
        # 左右滑动界面,传入时间为毫秒
        self.driver.swipe(900, 1300, 100, 1300, 1000)