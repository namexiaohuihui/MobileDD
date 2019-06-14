# -*- coding: utf-8 -*-

# @author:  hz_company
# @license: (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
# @software: PyCharm
# @file:  test_h5.py
# @time: 2019/3/31 20:25
# @Software: PyCharm
# @Site    : 
# @desc:

import unittest
import os
from uiautomator import Device
from time import sleep


class wechatPublicTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        pass

    # 微信原生界面流程测试,用uiautomator框架
    def setUp(self):
        # 使用adb命令调起微信
        cmd = 'adb shell am start com.tencent.mm/com.tencent.mm.ui.LauncherUI'
        os.system(cmd)
        # 对应设备的deviceName
        self.driver = Device('64535188')
        print(self.driver.info)
        # self.driver = androidDriver
        # 休眠一下，等待微信主页面加载完毕
        sleep(5)
        pass

    # def test_public_native(self):
    #     # 找到微信主页面的“通讯录” 并点击
    #     self.driver(text='通讯录').click()
    #     # 点击公众号
    #     self.driver(text='公众号').click()
    #     # 上下滑动去找连你订水
    #     print("开始找")
    #     self.driver(scrollable=True).scroll.to(text="连你订水")
    #     print("找到了")
    #     self.driver(text='连你订水').click()
    #     self.driver(text='用户').click()
    #     self.driver(text='个人中心').click()
    #     sleep(5)
    #     pass

    def test_public_xiaochengxu(self):
        # 找到微信主页面的“发现” 并点击
        self.driver(text='发现').click()
        # 点击公众号
        self.driver(text='小程序').click()

        # 上下滑动去找连你订水商城
        print("开始找小程序")
        self.driver(scrollable=True).scroll.to(text="连你订水商场")
        print("找到了小程序")
        self.driver(text='连你订水商城').click()
        pass

    def tearDown(self):
        # 测试用例运行结束关闭应用
        cmd = 'adb shell am force-stop com.tencent.mm'
        os.system(cmd)
        pass

    @classmethod
    def tearDownClass(self):
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
