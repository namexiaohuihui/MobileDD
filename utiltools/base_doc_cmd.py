# -*- coding: utf-8 -*-

# @author:  ln_company
# @license: (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
# @software: PyCharm
# @file:  base_driver.py
# @time: 2019/3/5 11:17
# @Software: PyCharm
# @Site    : 
# @desc: driver定义处

import os, subprocess


class BaseDosCmd:
    def excute_cmd_result(self, command):
        """
        执行命令并返回结果集
        :param command:
        :return:
        """
        result_list = []
        result = os.popen(command)
        for i in result:
            if i == '\n':
                continue
            else:
                result_list.append(i.strip('\n'))
        return result_list

    def excute_cmd(self, command):
        """
        不需要返回结果集
        只执行命令
        :param command:
        :return:
        """
        os.system(command)
        pass

    def rewrite_popen(self, command):
        """
        重写popen方法
        :param command:
        :return:
        """
        try:
            popen = subprocess.Popen(command, stdout=subprocess.PIPE)
            popen.wait()
            lines = popen.stdout.readlines()
            return [line.decode('gbk') for line in lines]
        except BaseException as e:
            return -1


if __name__ == '__main__':
    command = 'adb devices'
    print(BaseDosCmd().excute_cmd(command))
