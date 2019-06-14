# -*- coding: utf-8 -*-

# @author:  ln_company
# @license: (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
# @software: PyCharm
# @file:  start_appium.py
# @time: 2019/3/3 15:02
# @Software: PyCharm
# @Site    : 
# @desc:

import time
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))

from utiltools.directional_motion import DirectionalMotion
from business.start_server import StartServer
from case.account_to_login import AccountToLogin

# appWaitActivity: 切换到指定的activity
# appActivity: 启动默认的activity
desired_caps = {
    "platformName": "Android",
    "automationName": "Uiautomator2",
    "platformVersion": "7.1.1",
    # "deviceName": "64535188",
    "deviceName": "192.168.1.3:5555",
    "noReset": True,
    "appPackage": "cn.com.open.mooc",
    "appActivity": "com.imooc.component.imoocmain.splash.MCSplashActivity"
}

start = StartServer(desired_caps)


try:
    account = AccountToLogin(start.driver)

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
    print('点击的完毕\n')
    account.click_login_button('登录密码错误')
    print('点击完毕')

except Exception as e:
    print(e)
    pass

finally:
    time.sleep(2)
    start.driver.quit()
