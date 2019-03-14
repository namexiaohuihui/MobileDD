# -*- coding: utf-8 -*-

# @author:  ln_company
# @license: (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
# @software: PyCharm
# @file:  get_by_local.py
# @time: 2019/3/4 16:21
# @Software: PyCharm
# @Site    : 
# @desc:
from selenium.webdriver.common.by import By

from utiltools.readModel import ReadModel


class GetByLocal(object):

    def __init__(self, file_name):
        self.file_name = file_name

    def get_element(self, section, key):
        read_ini = ReadModel(self.file_name)
        local = read_ini.get_value(section, key)
        if local:
            local = local.split('>')
            way = local[0]
            local = local[1]

            if 'class' == way or 'Class' == way:
                ele_by = (By.CLASS_NAME, local)
                pass
            elif 'id' == way or 'Id' == way:
                ele_by = (By.ID, local)
                pass
            elif 'xpath' == way or 'Xpath' == way:
                ele_by = (By.XPATH, local)
                pass
            elif 'text' == way or 'text' == way:
                ele_by = (By.LINK_TEXT, local)
                pass
            else:
                raise Exception("get_element:你写的ini有误")
        else:
            ele_by = None
        return ele_by
        pass
