# -*- coding: utf-8 -*-
import time
import unittest
from selenium import webdriver
from PubliCode.onlineClass import *


class Int01_Users(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)

    # 系统管理------系统初始化
    def test_Int01_00(self):
        driver = self.driver
        ClasMenu.menu_full_text(self, "系统管理", "用户管理", "组管理")

    def test_Int01_01(self):
        driver = self.driver
        ClasMenu.menu_full_text(self, "系统管理", "用户管理", "组管理")
        time.sleep(3)
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000123")
        driver.find_element_by_id("ExcelAdd").click()
        time.sleep(3)
        driver.switch_to_frame("winExcel_IFrame")
        driver.find_element_by_id("UploadFile-file").send_keys(root_path() + "PubliData/excel/group.xlsx")
        driver.find_element_by_id("BtnSaveForm").click()
        time.sleep(4)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功" in i.text:
                print("系统管理-系统初始化-组数据导入OK")
            elif "导入组失败" in i.text:
                print("BUG 系统初始化-组管理数据导入失败")
            else:
                print("BUG 系统初始化-组管理数据导入失败")
                unittest.expectedFailure("test_Int01_01")

    def test_Int01_02(self):
        driver = self.driver
        ClasMenu.menu_full_text(self, "系统管理", "用户管理", "岗位管理")
        # 移动到页面顶部，防止对象遮挡
        time.sleep(3)
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000005")
        v_excelAdd = driver.find_element_by_id("ExcelAdd")
        if v_excelAdd.is_displayed():
            print("系统管理-系统初始化-岗位管理数据导入OK")
            v_excelAdd.click()
            time.sleep(1)
            driver.switch_to_frame("winExcel_IFrame")
            driver.find_element_by_id("UploadFile-file").send_keys(root_path() + "PubliData/excel/job.xlsx")
            driver.find_element_by_id("BtnSaveForm").click()
            time.sleep(4)
        else:
            print("BUG 系统初始化-岗位数据导入失败")

    def test_Int01_03(self):
        driver = self.driver
        ClasMenu.menu_full_text(self, "系统管理", "用户管理", "部门管理")
        time.sleep(3)
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000006")
        v_excelAdd = driver.find_element_by_id("ExcelAdd")
        if  v_excelAdd.is_displayed():
            print("系统管理-系统初始化-部门数据导入OK")
            v_excelAdd.click()
            time.sleep(1)
            driver.switch_to_frame("winExcel_IFrame")
            driver.find_element_by_id("UploadFile-file").send_keys(root_path() + "PubliData/excel/Department.xlsx")
            driver.find_element_by_id("BtnSaveForm").click()
            time.sleep(4)
        else:
            print("BUG 系统初始化-部门管理数据导入失败")

    def test_Int01_04(self):
        driver = self.driver
        ClasMenu.menu_full_text(self, "系统管理", "用户管理", "角色管理")
        time.sleep(3)
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000004")
        v_excelAdd = driver.find_element_by_id("ExcelAdd")
        if  v_excelAdd.is_displayed():
            print("系统管理-系统初始化-角色数据导入OK")
            v_excelAdd.click()
            time.sleep(1)
            driver.switch_to_frame("winExcel_IFrame")
            driver.find_element_by_id("UploadFile-file").send_keys(root_path() + "PubliData/excel/onrole.xlsx")
            driver.find_element_by_id("BtnSaveForm").click()
            time.sleep(4)
        else:
            print("BUG 系统初始化-角色管理-数据导入失败")

    def test_Int01_05(self):
        driver = self.driver
        ClasMenu.menu_full_text(self, "系统管理", "用户")
        time.sleep(3)
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000003")
        driver.find_element_by_id("ExcelAdd").click()
        time.sleep(2)
        driver.switch_to_frame("winExcel_IFrame")
        driver.find_element_by_id("UploadFile-file").send_keys(root_path() + "PubliData/excel/onuser.xlsx")
        driver.find_element_by_id("BtnSaveForm").click()
        time.sleep(4)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "导入成功" in i.text:
                print(i.text)
            else:
                print(i.text)
                unittest.expectedFailure("test_Int01_05")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()

    testsuit.addTest(Int01_Users("test_Int01_05"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)