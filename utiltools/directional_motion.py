# -*- coding: utf-8 -*-

# @author:  ln_company
# @license: (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
# @software: PyCharm
# @file:  directional_motion.py.py
# @time: 2019/3/3 16:01
# @Software: PyCharm
# @Site    : 
# @desc:

import time


class DirectionalMotion(object):

    def __init__(self, driver, time_motion):
        """
        模拟上下左右滑动屏幕
        :param driver:   appium驱动对象
        :param time_motion:   手指滑动时间,毫秒为单位
        """
        self.driver = driver
        self.time_motion = time_motion
        pass

    def swipe_on(self, direction: str):
        time.sleep(2)
        direction = "swipe_" + direction
        function = getattr(self, direction)
        function()

    def get_size(self):
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        return width, height

    def swipe_left(self):
        # 向左滑动
        width, height = self.get_size()
        x1 = width / 10 * 9
        y1 = height / 2
        x2 = width / 10
        self.driver.swipe(x1, y1, x2, y1, self.time_motion)

    def swipe_right(self):
        # 向右滑动
        width, height = self.get_size()
        x1 = width / 10 * 9
        y1 = height / 2
        x2 = width / 10
        self.driver.swipe(x2, y1, x1, y1, self.time_motion)

    def swipe_up(self):
        # 向上滑动
        width, height = self.get_size()
        x1 = width / 2
        y1 = height / 10 * 9
        y2 = height / 10 * 2
        self.driver.swipe(x1, y1, x1, y2, self.time_motion)

    def swipe_down(self):
        # 向下滑动
        width, height = self.get_size()
        x1 = width / 2
        y1 = height / 10 * 2
        y2 = height / 10 * 9
        self.driver.swipe(x1, y1, x1, y2, self.time_motion)
