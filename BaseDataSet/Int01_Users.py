# -*- coding: utf-8 -*-
import time
import unittest
from selenium import webdriver
from PubliCode.onlineClass import *


class IntUsers(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)

    '''系统管理-系统初始化'''
    def test_Int01_01(self):
        driver = self.driver
        ClasMenu.menu_full_text(self, "系统管理", "用户管理", "组管理")
        time.sleep(4)
        driver.switch_to.frame("frame_tab_PM000123")
        v_list = driver.find_elements_by_class_name("x-grid3-row")
        if len(v_list) < 2:
            driver.find_element_by_id("ExcelAdd").click()
            time.sleep(3)
            driver.switch_to.frame("winExcel_IFrame")
            driver.find_element_by_id("UploadFile-file").send_keys(root_path() + "PubliData/excel/group.xlsx")
            driver.find_element_by_id("BtnSaveForm").click()
            time.sleep(4)
            v_tip = driver.find_elements_by_class_name("ext-mb-text")
            for i in v_tip:
                if "成功" in i.text:
                    print(i.text)
                else:
                    print(i.text)
                    unittest.expectedFailure("test_Int01_01")
        else:
            print("已经导入，无需再导")

    def test_Int01_02(self):
        driver = self.driver
        ClasMenu.menu_full_text(self, "系统管理", "用户管理", "岗位管理")
        time.sleep(3)
        driver.switch_to.frame("frame_tab_PM000005")
        v_list = driver.find_elements_by_class_name("x-grid3-row")
        if len(v_list) < 2:
            driver.find_element_by_id("ExcelAdd").click()
            time.sleep(3)
            driver.switch_to.frame("winExcel_IFrame")
            driver.find_element_by_id("UploadFile-file").send_keys(root_path() + "PubliData/excel/job.xlsx")
            driver.find_element_by_id("BtnSaveForm").click()
            time.sleep(4)
            v_tip = driver.find_elements_by_class_name("ext-mb-text")
            for i in v_tip:
                if "成功" in i.text:
                    print(i.text)
                else:
                    print(i.text)
                    unittest.expectedFailure("test_Int01_01")
        else:
            print("已经导入，无需再导")

    def test_Int01_03(self):
        driver = self.driver
        ClasMenu.menu_full_text(self, "系统管理", "用户管理", "部门管理")
        time.sleep(3)
        driver.switch_to.frame("frame_tab_PM000006")
        v_list = driver.find_elements_by_class_name("x-grid3-row")
        if len(v_list) < 2:
            driver.find_element_by_id("ExcelAdd").click()
            time.sleep(3)
            driver.switch_to.frame("winExcel_IFrame")
            driver.find_element_by_id("UploadFile-file").send_keys(root_path() + "PubliData/excel/Department.xlsx")
            driver.find_element_by_id("BtnSaveForm").click()
            time.sleep(3)
            v_tip = driver.find_elements_by_class_name("ext-mb-text")
            for i in v_tip:
                if "成功" in i.text:
                    print(i.text)
                else:
                    print(i.text)
                    unittest.expectedFailure("test_Int01_01")
        else:
            print("已经导入，无需再导")

    def test_Int01_04(self):
        driver = self.driver
        ClasMenu.menu_full_text(self, "系统管理", "用户管理", "角色管理")
        time.sleep(3)
        driver.switch_to.frame("frame_tab_PM000004")
        v_list = driver.find_elements_by_class_name("x-grid3-row")
        if len(v_list) < 3:
            driver.find_element_by_id("ExcelAdd").click()
            time.sleep(3)
            driver.switch_to.frame("winExcel_IFrame")
            driver.find_element_by_id("UploadFile-file").send_keys(root_path() + "PubliData/excel/onrole.xlsx")
            driver.find_element_by_id("BtnSaveForm").click()
            time.sleep(3)
            v_tip = driver.find_elements_by_class_name("ext-mb-text")
            for i in v_tip:
                if "成功" in i.text:
                    print(i.text)
                else:
                    print(i.text)
                    unittest.expectedFailure("test_Int01_01")
        else:
            print("已经导入，无需再导")

    def test_Int01_05(self):
        driver = self.driver
        ClasMenu.menu_full_text(self, "系统管理", "用户")
        time.sleep(3)
        driver.switch_to.frame("frame_tab_PM000003")
        v_list = driver.find_elements_by_class_name("x-grid3-row")
        if len(v_list) < 2:
            driver.find_element_by_id("ExcelAdd").click()
            time.sleep(3)
            driver.switch_to.frame("winExcel_IFrame")
            driver.find_element_by_id("UploadFile-file").send_keys(root_path() + "PubliData/excel/onuser.xlsx")
            driver.find_element_by_id("BtnSaveForm").click()
            time.sleep(3)
            v_tip = driver.find_elements_by_class_name("ext-mb-text")
            for i in v_tip:
                if "成功" in i.text:
                    print(i.text)
                else:
                    print(i.text)
                    unittest.expectedFailure("test_Int01_01")
        else:
            print("已经导入，无需再导")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()

    testsuit.addTest(IntUsers("test_Int01_05"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)