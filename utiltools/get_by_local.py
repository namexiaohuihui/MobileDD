# -*- coding: utf-8 -*-

# @author:  ln_company
# @license: (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
# @software: PyCharm
# @file:  get_by_local.py
# @time: 2019/3/4 16:21
# @Software: PyCharm
# @Site    : 
# @desc:
import inspect
from time import sleep

import selenium.webdriver.support.ui as ui
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By

from utiltools.readModel import ReadModel


class GetByLocal(object):
    """
    获取指定路径yaml下面存储的元素然后判断其是否存在
    """

    def __init__(self, file_name, driver):
        self.driver = driver
        self.file_name = file_name

    def get_element(self, section, key):
        read_ini = ReadModel(self.file_name)
        local = read_ini.get_value(section, key)
        if local:
            local = local.split('>')
            ele_by = self.is_visible_driver(local[1], local[0])
        else:
            ele_by = None
        return ele_by

    def is_visible_driver(self, local: str, way: str):
        """
        根据类型定义相应的by元素对象
        :param local:     元素路径
        :param way:     元素类路径类型
        :return:
        """
        by_ele = {"Css": 'CSS_SELECTOR', "Id": 'ID', "Xpath": 'XPATH', "Name": 'NAME'}
        # capitalize不区分大小写
        if way.capitalize() in by_ele.keys():
            ele_by = by_ele.get(way.capitalize())
            ele_by = getattr(By, ele_by)
            ele_by = (ele_by, local)
        else:
            ele_by = None
        del by_ele
        return ele_by

    def differentiate_all_exist(self, ele_by, timeout=5):
        """
        根据某个元素路径,返回符合该路径的全部元素
        :param ele_by: 在is_visible_driver中返回的元素by属性
        :param timeout: 元素查找时间,默认为5s
        :return:
        """
        try:
            ele = ui.WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located(ele_by))
            return ele
        except Exception as e:
            fun_name = inspect.stack()[0][3]
            print("%s发生错误%s,元素对象为%s" % (fun_name, e, ele_by))
            return False

    def differentiate_single_exist(self, ele_by, timeout=5):
        """
        根据某个元素路径,第一个符合该路径的元素
        :param ele_by: 在is_visible_driver中返回的元素by属性
        :param timeout: 元素查找时间,默认为5s
        :return:
        """
        try:
            ele = ui.WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(ele_by))
            return ele
        except Exception as e:
            fun_name = inspect.stack()[0][3]
            print("%s发生错误%s,元素对象为%s" % (fun_name, e, ele_by))
            return False

    def differentiate_not_exist(self, ele_by, timeout=5):
        """
        识别某个元素是否从界面上消失
        :param ele_by:在is_visible_driver中返回的元素by属性
        :param timeout:
        :return:
        """
        try:
            ui.WebDriverWait(self.driver, timeout).until_not(EC.element_to_be_clickable(ele_by))
            return True
        except Exception as e:
            fun_name = inspect.stack()[0][3]
            print("%s发生错误%s,元素对象为%s" % (fun_name, e, ele_by))
            return False

    def is_visible_single_driver(self, locator, way, timeout=5):
        """
        识别某个元素是否加载完毕
        :param locator:
        :param way:
        :param timeout:
        :return:
        """
        ele_by = self.is_visible_driver(locator, way)
        return self.differentiate_single_exist(ele_by, timeout)

    def is_visible_all_driver(self, locator: str, way: str, timeout: int = 5):
        """
        识别元素路径相同的全部元素
        :param locator:
        :param way:
        :param timeout:
        :return:
        """
        ele_by = self.is_visible_driver(locator, way)
        return self.differentiate_all_exist(ele_by, timeout)

    def is_visible_not_driver(self, locator, way, timeout=5):
        """
        判断某个元素是否消失
        :param locator:
        :param way:
        :param timeout:
        :return:
        """

        ele_by = self.is_visible_driver(locator, way)
        return self.differentiate_not_exist(ele_by, timeout)

    def click_element_prompt(self, prompt: str):
        prompt = 'new UiSelector().text("%s")' % prompt
        prompt = self.driver.find_element_by_android_uiautomator(prompt)
        self.is_visible_click(prompt)

    def is_click_single(self, locator, way):
        prompt = self.is_visible_driver(locator, way)
        prompt = self.differentiate_single_exist(prompt)
        self.is_visible_click(prompt)

    def is_visible_click(self, prompt):
        """
        执行点击操作
        :param prompt:
        :return:
        """
        prompt.click()
        sleep(1)

    def is_visible_input(self, attribute, parameter):
        """
        统一封装元素输入操作
        :param attribute: 元素对象
        :param parameter: 输入内容
        :return:
        """
        attribute.clear()
        attribute.send_keys(parameter)
        sleep(1)
