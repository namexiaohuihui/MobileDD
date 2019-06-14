# -*- coding: utf-8 -*-

# @author:  ln_company
# @license: (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
# @software: PyCharm
# @file:  test_thre.py
# @time: 2019/3/4 17:55
# @Software: PyCharm
# @Site    : 
# @desc:

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))

import threading
import multiprocessing
import unittest
import HTMLTestRunner

from case.login_case import LoginCase
from utiltools.server_command import ServerCommand
from utiltools.operation_yaml import OperationYaml

# 获取当前文件所在目录
CUR_PATH ='../report/'

# 设置时间格式
day_now = time.strftime("%Y-%m-%d")
time_now = time.strftime("%H-%M-%S")

def get_suite(i):
    suite = unittest.TestSuite()
    suite.addTest(LoginCase("test_01", parame=i))
    suite.addTest(LoginCase("test_02", parame=i))
    report_path = os.path.join(CUR_PATH, day_now)
    if not os.path.exists(report_path): os.mkdir(report_path)

    filename = "%s-%s.html" % (time_now, 'report_%s'%i)
    report_abspath = os.path.join(report_path, filename)

    fp = open(report_abspath, "wb")
    HTMLTestRunner.HTMLTestRunner(fp).run(suite)


def threading_start(count):
    """
    多线程启动
    :param count:
    :return:
    """
    threads = []

    for i in range(count):
        t = threading.Thread(target=get_suite, args=(i,))
        t.start()
        threads.append(t)
        pass
    for j in threads:
        j.join()
        pass


def multiprocessing_start(count):
    """
    多线程启动
    :param count:
    :return:
    """
    mult_list = []
    for i in range(count):
        t = multiprocessing.Process(target=get_suite, args=(i,))
        t.start()
        mult_list.append(t)
        pass


if __name__ == '__main__':
    server = ServerCommand('adb devices')
    server.main_start()

    count = OperationYaml("../configs/userconfig.yaml").get_file_lines()
    print("链接设备有:%s" % count)

    multiprocessing_start(count)
