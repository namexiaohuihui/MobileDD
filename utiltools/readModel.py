# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: readModel.py
@time: 2017/12/20 23:30
@项目名称:operating
"""
import configparser
import os


class ReadModel(object):
    def __init__(self, file_name, file_path=None):

        if file_path:
            self.file_path = file_path
        else:
            cur_path = os.path.abspath(os.path.dirname(os.getcwd()))
            self.file_path = os.path.join(cur_path, 'configs')

        if '.ini' in file_name:
            self.file_name = file_name
        else:
            self.file_name = file_name + ".ini"

        configPath = os.path.join(self.file_path, self.file_name)
        self.read_ini(configPath)
        pass

    def read_ini(self, configPath):
        """
        将ini文件内的数据转成dict
        :param configPath:  需要读取的ini文件
        :return:
        """
        self.conf = configparser.ConfigParser()
        self.conf.read(configPath)
        pass

    def get_value(self, section, key):
        """
        通过key值获取相应的数据信息
        :param section:
        :param key:
        :return:
        """
        try:
            value = self.conf.get(section, key)
        except:
            value = None
        return value


if __name__ == '__main__':
    conf = ReadModel('LoginElement')
    password = conf.get_value('login', 'password')
    print()
