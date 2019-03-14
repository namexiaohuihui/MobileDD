# -*- coding: utf-8 -*-

# @author:  ln_company
# @license: (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
# @software: PyCharm
# @file:  server_command.py
# @time: 2019/3/5 12:03
# @Software: PyCharm
# @Site    : 
# @desc:

import os
import time

import threading

from utiltools.base_doc_cmd import BaseDosCmd
from utiltools.server_post import ServerPost
from utiltools.operation_yaml import OperationYaml


class ServerCommand:
    def __init__(self, command):
        self.doc = BaseDosCmd()
        self.op_yaml = OperationYaml("../configs/userconfig.yaml")
        self.devices_list = self.get_devices(command)
        # self.devices_list = [1,2,3,4,56,7,8,96,4,6,0]

    def get_devices(self, command):
        """
        获取设备信息
        :param command: adb devices
        :return:
        """
        devices_list = []
        result_list = self.doc.excute_cmd_result(command)
        result_len = len(result_list)
        if result_len > 1:
            for i in range(1, result_len):
                devices_info = result_list[i].split('\t')
                if devices_info[-1] == 'device':
                    devices_list.append(devices_info[0])
        else:
            devices_list = None
        return devices_list

    def creatr_post_list(self, start_post):
        """
        创建可用端口
        :param start_post:
        :return:
        """
        port = ServerPost()
        port_list = port.create_port_list(start_post, self.devices_list)
        return port_list

    def create_command_list(self, i, appium_start_post, bp_start_port):
        """
        appium -p 4700 -bp 4709 - U xxxx
        :return:
        """
        # # 存储命令
        # command_list = []

        # 开始端口
        appium_port_list = self.creatr_post_list(appium_start_post)

        # 结束端口
        bootstrap_port_list = self.creatr_post_list(bp_start_port)

        log_path = os.path.join(os.path.abspath(os.path.dirname(os.getcwd())), 'logs')
        if not os.path.exists(log_path): os.mkdir(log_path)
        log_path = os.path.join(log_path, '%s.log' % (time.strftime('%Y_%m_%d')))

        command = "appium -p %s -bp %s -U %s --no-reset --session-override --log %s" % \
                  (appium_port_list[i], bootstrap_port_list[i], self.devices_list[i], log_path)
        # command_list.append(command)
        self.op_yaml.write_data(i, self.devices_list[i], bootstrap_port_list[i], appium_port_list[i])

        return command

    def start_server(self, i, appium_start_post, bp_start_port):
        start_list = self.create_command_list(i, appium_start_post, bp_start_port)
        print("需要执行的指令为:%s" % start_list)
        self.doc.excute_cmd(start_list)
        # self.doc.excute_cmd('adb devices')
        pass

    def kill_server(self):
        server_list = self.doc.excute_cmd_result('tasklist | find "node.exe"')
        if len(server_list) > 0:
            self.doc.excute_cmd('taskkill -F -PID node.exe')

    def main_start(self, appium_start_post: int = 4723, bp_start_port: int = 4790):
        self.kill_server()
        self.op_yaml.clear_data()
        for i in range(len(self.devices_list)):
            appium_start = threading.Thread(target=self.start_server, args=(i, appium_start_post, bp_start_port,))
            appium_start.start()
        time.sleep(20)


if __name__ == '__main__':
    devices_list = ServerCommand('adb devices').main_start(4723, 4790)
    print(devices_list)
