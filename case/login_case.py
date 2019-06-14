# -*- coding: utf-8 -*-

# @author:  ln_company
# @license: (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
# @software: PyCharm
# @file:  login_case.py
# @time: 2019/3/4 17:24
# @Software: PyCharm
# @Site    : 
# @desc:


import sys
import os
import time

sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))

import unittest

from business.start_server import StartServer
from case.account_to_login import AccountToLogin


class ParameTestCase(unittest.TestCase):
    """
    执行case用例时可接收传入参数的写法
    """

    def __init__(self, methodName='runTest', parame=None):
        super(ParameTestCase, self).__init__(methodName)
        global parames
        parames = parame


class LoginCase(ParameTestCase):

    @classmethod
    def setUpClass(cls):
        print("读取配置信息:%s\n" % parames)

    def setUp(cls):
        print("执行前置动作:%s\n" % parames)
        cls.start = StartServer(parames)
        pass

    def hahahaha(self):
        try:
            account = AccountToLogin(self.start.driver)

            # 切换到账号
            print('start zhagnhao\n')
            account.enter_account()
            print('stop zhanghao\n')

            # 点击去登录
            print('chilk login\n')
            account.click_login()
            print('stop login\n')

            # 输入账号
            print('输入账号\n')
            account.account_edit('18778036030')
            print('账号输入完毕\n')

            # 输入密码
            print('输入密码\n')
            account.password_edit('123456')
            print('密码输入完毕\n')

            # 点击登录按钮
            print('点击的呢牢固\n')
            account.click_login_button('登录1密码错误')
            print('点击完毕')

        except Exception as e:
            print(e)
            pass

    def test_01(self):
        """用例场景=:="""
        print("执行用例:%s\n" % parames)
        self.hahahaha()
        self.start.driver.save_screenshot(r'E:\test_01.png')
        pass

    @unittest.skip('qweqw')
    def test_02(self):
        print("this is test_02")
        self.hahahaha()
        self.start.driver.save_screenshot(r'E:\test_02.png')
        pass

    def tearDown(self):
        print("执行后置动作\n")
        time.sleep(2)
        self.start.driver.quit()
        pass

    @classmethod
    def tearDownClass(cls):
        print("执行结尾操作\n")


if __name__ == '__main__':
    unittest.main(verbosity=2)
