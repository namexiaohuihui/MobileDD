# -*- coding: utf-8 -*-
__author__ = 'Administrator'
"""
@file: app_buyer_sign.py
@time: 2018/1/15 17:35
"""

import time
import unittest
from business.start_server import StartServer
from utiltools.directional_motion import DirectionalMotion
from utiltools.get_by_local import GetByLocal


class TestBuyerSign(unittest.TestCase):
    app_package = "com.tencent.mm"

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(cls):
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "7.1.1",
            "deviceName": "64535188",
            "appPackage": cls.app_package,
            "appActivity": ".ui.LauncherUI",
            "noReset": True,
            'chromeOptions': {'androidProcess': 'com.tencent.mm:appbrand0'}
        }
        cls.start = StartServer(0, desired_caps)
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def click_element_data(self, data: str):
        data = 'new UiSelector().text("%s")' % data
        data = self.start.driver.find_element_by_android_uiautomator(data)
        data.click()

    def test_01(self):
        """用例场景=:="""
        self.start.driver.wait_activity(".ui.LauncherUI", 3)

        self.dm = DirectionalMotion(self.start.driver, 500)
        self.dm.swipe_on('down')
        get_by = GetByLocal("1", self.start.driver)
        id_yp = get_by.is_visible_all_driver("com.tencent.mm:id/yp",'id')
        get_by.is_visible_click(id_yp[7])

        time.sleep(15)

        get_by.click_element_prompt("个人中心")
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
