# -*- coding: utf-8 -*-
import random
import time
import unittest
from selenium import webdriver
from PubliCode.onlineClass import *


class Int06_PersonalAdd(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_part_text(self, "事务处理", "通讯录", "个人通讯录")
        driver.switch_to.frame("frame_tab_PM001018")

    '''事务处理-通讯录-个人通讯录'''

    def test_Int06_Import(self):
        driver = self.driver
        driver.find_element_by_xpath("/html/body/div/div[1]/div/div[1]/div[2]/div/a[3]").click()
        driver.find_element_by_id("btnImport").click()
        time.sleep(2)

        driver.find_element_by_id("UploadFile-file").send_keys(root_path() + "PubliData/excel/个人通信录.xlsx")
        time.sleep(1)
        driver.find_element_by_id("BtnSaveForm").click()
        time.sleep(4)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "导入成功" in i.text:
                print(i.text)
            elif "已存在" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/test_Int06_Import.jpg")
                unittest.expectedFailure("test_Int06_Import")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(Int06_PersonalAdd("test_Int06_Import"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)