# -*- coding: utf-8 -*-
import random
import time
import unittest
from selenium import webdriver
from PubliCode.onlineClass import *


class Int05_HRTaking(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_part_text(self, "人事管理", "员工异动", "入职")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000892")

    '''人事管理-员工异动-入职'''

    def test_Int05_01_Import(self):
        driver = self.driver
        driver.find_element_by_id("ExcelImport").click()
        time.sleep(3)
        driver.switch_to.frame("winExcel_IFrame")

        driver.find_element_by_id("UploadFile-file").send_keys(root_path() + "PubliData/excel/HR员工入职.xlsx")
        time.sleep(1)
        driver.find_element_by_id("BtnSaveForm").click()
        time.sleep(4)

        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "导入成功" in i.text:
                print(i.text)
            elif "档案中已存在" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/test_Int05_01_Import.jpg")
                unittest.expectedFailure("test_Int05_01_Import")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    unittest.main()
