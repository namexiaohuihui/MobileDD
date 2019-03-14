# -*- coding: utf-8 -*-

# @author:  ln_company
# @license: (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
# @software: PyCharm
# @file:  server_post.py
# @time: 2019/3/5 12:18
# @Software: PyCharm
# @Site    : 
# @desc:

from utiltools.base_doc_cmd import BaseDosCmd


class ServerPost():
    def post_is_used(self, post_num):
        """
        判断端口是否被占用
        :param post:
        :return:
        """
        self.doc = BaseDosCmd()
        result = self.doc.excute_cmd_result('netstat -ano | findstr %s' % post_num)
        if len(result) > 0:
            flag = True
        else:
            flag = False
        return flag

    def create_port_list(self, start_post, device_list):
        """
        生成可用端口
        :param start_post: 端口号
        :param device_list: 可用的设备
        :return:
        """
        port_list = []
        # 判断是否有可用的设备
        if device_list:
            # 当可用接口数量小于设备数量,开始获取可用端口
            while len(port_list) < len(device_list):
                # 判断端口是否可用
                if not self.post_is_used(start_post):
                    port_list.append(start_post)
                # 端口数+1
                start_post = start_post + 1
        else:
            port_list = None
            print('Failed to generate port, available device is zero...')

        return port_list


if __name__ == '__main__':
    li = [1,2,3,4,5,6]
    print(ServerPost().create_port_list(4722,li))
