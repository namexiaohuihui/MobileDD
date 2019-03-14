# -*- coding: utf-8 -*-

# @author:  ln_company
# @license: (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
# @software: PyCharm
# @file:  login_business.py
# @time: 2019/3/4 17:02
# @Software: PyCharm
# @Site    : 
# @desc:

from handles.login_handles import LoginHandles


class LoginBusiness(object):
    def __init__(self, driver, login_ini, section):
        self.section = section
        self.login_handle = LoginHandles(driver, login_ini)
        pass

    def login_input_exist(self, key, account):
        self.login_handle.element_input(self.section, key, account)
        pass

    def login_click_exist(self, key):
        self.login_handle.element_click(self.section, key)
        pass
