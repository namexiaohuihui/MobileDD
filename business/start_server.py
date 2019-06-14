# -*- coding: utf-8 -*-

# @author:  ln_company
# @license: (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
# @software: PyCharm
# @file:  start_server.py
# @time: 2019/3/3 16:22
# @Software: PyCharm
# @Site    : 
# @desc:


import os
from appium import webdriver
from utiltools.operation_yaml import OperationYaml


class StartServer(object):

    def __init__(self, i, desired_caps=None):
        """
        :param i:  启动端口及url的标识符
        :param desired_caps: 设备的信息
        """
        yaml_path = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'configs/userconfig.yaml')
        op_yaml = OperationYaml(yaml_path)

        deviceName = op_yaml.get_value('user_info_%s' % i, 'deviceName')
        port = op_yaml.get_value('user_info_%s' % i, 'port')

        if desired_caps:
            self.desired_caps = desired_caps
        else:
            self.desired_caps = {
                "platformName": "Android",
                "automationName": "Uiautomator2",
                "platformVersion": "7.1.1",
                # "deviceName": "64535188",
                "deviceName": deviceName,
                "noReset": True,
                "appPackage": "cn.com.open.mooc",
                "appActivity": "com.imooc.component.imoocmain.splash.MCSplashActivity"
            }
        self.start_app(port=port)
        pass

    def start_app(self, port):
        """
        端口及url的设置
        :param port:
        :return:
        """
        self.driver = webdriver.Remote("http://127.0.0.1:%s/wd/hub" % port, self.desired_caps)
        self.driver.implicitly_wait(5)
        pass
