# -*- coding: utf-8 -*-

# @author:  ln_company
# @license: (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
# @software: PyCharm
# @file:  ream_yaml.py
# @time: 2019/3/5 14:04
# @Software: PyCharm
# @Site    : 
# @desc:

import yaml


class OperationYaml:
    def __init__(self, yaml_path):
        self.yaml_path = yaml_path

    def read_data(self):
        '''
        加载数据
        :return:
        '''
        with open(self.yaml_path) as fr:
            data = yaml.load(fr)
        return data

    def get_value(self, key, port):
        data = self.read_data()
        value = data[key][port]
        return value

    def write_data(self, i, device, dp, port):
        """
        写入数据
        :param data:
        :return:
        """
        data = self.joji_data(i, device, dp, port)
        with open(self.yaml_path, "a") as fr:
            yaml.dump(data, fr)

    def joji_data(self, i, device, dp, port):
        data = {
            "user_info_%s" % i: {
                'deviceName': device,
                'dp': dp,
                'port': port
            }
        }
        return data

    def clear_data(self):
        with open(self.yaml_path, "w") as fr:
            fr.truncate()

    def get_file_lines(self):
        data = self.read_data()
        return len(data)

if __name__ == '__main__':
    yaml_path = "../configs/userconfig.yaml"
    op_yaml = OperationYaml(yaml_path)
    data_value = op_yaml.get_value('user_info_0', 'port')
    print(data_value)
