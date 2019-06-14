# -*- coding: utf-8 -*-

# @author:  ln_company
# @license: (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
# @software: PyCharm
# @file:  login_handles.py
# @time: 2019/3/4 16:50
# @Software: PyCharm
# @Site    : 
# @desc:


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage


class LoginHandles():
    def __init__(self, driver, login_ini):
        self.driver = driver
        self.login_page = LoginPage(login_ini,self.driver)
        pass

    def verify_element_exist(self, edit):
        """
        判断元素是否找到
        :param edit:
        :return:
        """
        try:
            edit = WebDriverWait(self.driver, 5, 1).until(
                EC.presence_of_element_located(edit))
        except Exception as e:
            edit = None
            print(e)
            pass
        return edit

    def find_and_verify(self, section, key):
        """
        根据指定的key找到元素并校验是否存在
        :param section:
        :param key:
        :return:
        """
        edit = self.login_page.get_page_element(section, key)
        edit = self.verify_element_exist(edit)
        return edit

    def element_input(self, section, key, msg):
        """
        执行输入操作
        :param section:
        :param key:
        :param msg:
        :return:
        """
        edit = self.find_and_verify(section, key)
        edit.click()
        edit.clear()
        edit.send_keys(msg)

    def element_click(self, section, key):
        """
        执行点击操作
        :param section:
        :param key:
        :return:
        """
        edit = self.find_and_verify(section, key)
        edit.click()
