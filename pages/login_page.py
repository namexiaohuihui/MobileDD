# -*- coding: utf-8 -*-

# @author:  ln_company
# @license: (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
# @software: PyCharm
# @file:  login_page.py
# @time: 2019/3/4 16:40
# @Software: PyCharm
# @Site    : 
# @desc:

from utiltools.get_by_local import GetByLocal

class LoginPage(object):
    def __init__(self, login_ini,driver):
        self.driver = driver
        self.login_ini = login_ini
        self.get_by = GetByLocal(self.login_ini,self.driver)
        pass

    def get_page_element(self, section, key):
        """
        获取指定页面的元素路径信息
        :param section:
        :param key:
        :return:
        """
        page_ele = self.get_by.get_element(section, key)
        return page_ele

