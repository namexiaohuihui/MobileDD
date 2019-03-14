# -*- coding: utf-8 -*-

# @author:  ln_company
# @license: (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
# @software: PyCharm
# @file:  account_to_login.py
# @time: 2019/3/4 15:17
# @Software: PyCharm
# @Site    : 
# @desc:

import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from handles.login_handles import LoginHandles
from business.login_business import LoginBusiness


class AccountToLogin(object):
    """从账号点击去登录按钮"""

    def __init__(self, driver):
        self.driver = driver
        self.login_ini = 'LoginElement'
        self.section = 'login'
        self.login_business = LoginBusiness(self.driver, self.login_ini, self.section)
        pass

    def enter_account(self):
        """
        切换到账号:Viewgroup
        :return:
        """
        # 方式一:通过相同id的元素，不同text来区分
        # dowm_text = self.driver.find_elements_by_id("android:id/text1")
        # for dowm in dowm_text:
        #     print(dowm.text)
        #     if '账号' == dowm.text:
        #         dowm.click()
        #         break

        # 方式二:通过同一组class,然后点击序号不同的对象
        # dowm_text = self.driver.find_elements_by_class_name("android.support.v7.app.ActionBar$Tab")
        # dowm_text[3].click()

        # 方式三:通过谷歌提供的UiSelector接口来找
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("账号")').click()
        pass

    def click_login(self):
        """
        点击去登录
        :return:
        """
        header_line = self.driver.find_element_by_id("cn.com.open.mooc:id/header_line")
        line_text = header_line.find_element_by_class_name("android.widget.TextView")
        line_text.click()
        pass

    def account_edit(self, account):
        # 输入账号
        self.login_business.login_input_exist('account', account)
        pass

    def password_edit(self, password):
        # 输入密码
        self.login_business.login_input_exist('password', password)
        pass

    def click_login_button(self, msg=None):
        # 点击登录按钮
        self.login_business.login_click_exist('login_button')

        if msg:
            self.prompt_information(msg)
        pass

    def prompt_information(self, msg):
        """
        点击登录之后,如果登录失败接口返回提示语:判断提示语是否出现
        :param msg:  提示语
        :return:
        """
        try:
            tost_ele = ("xpath", "//*[contains(@text,'%s')]" % msg)
            tost_ele = WebDriverWait(self.driver, 10, 0.1).until(
                EC.presence_of_element_located(tost_ele))
            print("点击登录找到提示:%s" % tost_ele.text)
            return tost_ele.text
        except:
            return False
