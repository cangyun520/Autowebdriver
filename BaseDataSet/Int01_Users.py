# -*- coding: utf-8 -*-
from PubliCode.onlineClass import *


class IntUsers(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)

    '''系统管理-系统初始化-组管理导入'''
    def test_Int01_01(self):
        driver = self.driver
        ClasMenu.menu_full_text(self, "订货管理", "系统管理", "用户设置", "组管理")
        time.sleep(4)
        driver.switch_to.frame("frame_tab_PM000123")
        v_list = driver.find_elements_by_class_name("x-grid3-row")
        if len(v_list) < 2:
            driver.find_element_by_id("ExcelAdd").click()
            time.sleep(3)
            driver.switch_to.frame("winExcel_IFrame")
            driver.find_element_by_id("UploadFile-file").send_keys(root_path() + "PubliData/excel/组.xlsx")
            time.sleep(1)
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

    '''系统管理-系统初始化-岗位管理导入'''
    def test_Int01_02(self):
        driver = self.driver
        ClasMenu.menu_full_text(self, "订货管理", "系统管理", "用户设置", "岗位管理")
        time.sleep(3)
        driver.switch_to.frame("frame_tab_PM000005")
        v_list = driver.find_elements_by_class_name("x-grid3-row")
        if len(v_list) < 2:
            driver.find_element_by_id("ExcelAdd").click()
            time.sleep(2)
            driver.switch_to.frame("winExcel_IFrame")
            driver.find_element_by_id("UploadFile-file").send_keys(root_path() + "PubliData/excel/岗位.xlsx")
            time.sleep(1)
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

    '''系统管理-系统初始化-部门管理导入'''
    def test_Int01_03(self):
        driver = self.driver
        ClasMenu.menu_full_text(self, "订货管理", "系统管理", "用户设置", "部门管理")
        time.sleep(3)
        driver.switch_to.frame("frame_tab_PM000006")
        v_list = driver.find_elements_by_class_name("x-grid3-row")
        if len(v_list) < 2:
            driver.find_element_by_id("ExcelAdd").click()
            time.sleep(2)
            driver.switch_to.frame("winExcel_IFrame")
            driver.find_element_by_id("UploadFile-file").send_keys(root_path() + "PubliData/excel/部门.xlsx")
            time.sleep(1)
            driver.find_element_by_id("BtnSaveForm").click()
            time.sleep(3)
            v_tip = driver.find_elements_by_class_name("ext-mb-text")
            for i in v_tip:
                if "部门成功" in i.text:
                    print(i.text)
                else:
                    print(i.text)
                    unittest.expectedFailure("test_Int01_01")
        else:
            print("已经导入，无需再导")

    '''系统管理-系统初始化-角色管理导入'''
    def test_Int01_04(self):
        driver = self.driver
        ClasMenu.menu_full_text(self, "订货管理", "系统管理", "用户设置", "角色管理")
        time.sleep(3)
        driver.switch_to.frame("frame_tab_PM000004")
        v_list = driver.find_elements_by_class_name("x-grid3-row")
        if len(v_list) < 3:
            driver.find_element_by_id("ExcelAdd").click()
            time.sleep(2)
            driver.switch_to.frame("winExcel_IFrame")
            driver.find_element_by_id("UploadFile-file").send_keys(root_path() + "PubliData/excel/角色.xlsx")
            time.sleep(1)
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

    '''系统管理-系统初始化-用户设置导入'''
    def test_Int01_05(self):
        driver = self.driver
        ClasMenu.menu_full_text(self, "订货管理", "系统管理", "用户设置", "用户管理")
        time.sleep(3)
        driver.switch_to.frame("frame_tab_PM000003")
        v_list = driver.find_elements_by_class_name("x-grid3-row")
        if len(v_list) < 2:
            driver.find_element_by_id("ExcelAdd").click()
            time.sleep(2)
            driver.switch_to.frame("winExcel_IFrame")
            driver.find_element_by_id("UploadFile-file").send_keys(root_path() + "PubliData/excel/用户.xlsx")
            time.sleep(1)
            driver.find_element_by_id("BtnSaveForm").click()
            time.sleep(3)
            v_tip = driver.find_elements_by_class_name("ext-mb-text")
            for i in v_tip:
                if "成功" in i.text:
                    print(i.text)
                else:
                    print(i.text)
                    unittest.expectedFailure("test_Int01_05")
        else:
            print("已经导入，无需再导")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    unittest.main()
