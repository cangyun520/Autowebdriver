# -*- coding: utf-8 -*-
import random
import time
import unittest
from selenium import webdriver
from PubliCode.onlineClass import *


class DB08_Department(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)

    '''系统初始化-用户管理-部门管理'''
    def test_0801_Department(self):
        driver = self.driver
        ClasMenu.menu_full_text(self, "系统管理", "用户设置", "部门管理")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000006")
        v_depart = driver.find_elements_by_class_name("x-treegrid-col")
        v_total = 0
        while v_total <= 4:
            v_depart[v_total].click()
            v_total += 1
        driver.find_element_by_id("btnSelect").click()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    unittest.main()
