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

    '''系统管理-常规设置-行格式自定义'''

    def test_0801_Department(self):
        driver = self.driver
        ClasMenu.menu_full_text(self, "系统管理", "常规设置", "行格式自定义")
        driver.switch_to.frame("frame_tab_PM000255")

        driver.find_element_by_id("comboBoxXmlName").click()



    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
