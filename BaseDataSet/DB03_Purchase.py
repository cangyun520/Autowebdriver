# -*- coding: utf-8 -*-
import random
import time
import unittest
from selenium import webdriver
from PubliCode.onlineClass import *


class DB03_Purchase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)

    # 采购设置-采购合同条款-数据添加
    def test_DB03_01_ContractAdd(self):
        """采购设置-采购合同条款-数据添加"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "系统管理", "业务设置", "采购设置", "采购合同条款")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000729")
        v_save = driver.find_element_by_id("btnSave")
        v_tim = time.strftime("%y%m%d%H%M")
        if v_save.is_displayed():
            v_write_file = open(root_path() + 'PubliData/character5K.txt', 'r')
            v_lines = v_write_file.read()
            driver.find_element_by_id("descrption").clear()
            driver.find_element_by_id("descrption").send_keys(v_tim + v_lines[10:1000])
            time.sleep(2)
            v_save.click()
            time.sleep(3)
            print("业务设置-采购设置-采购合同条款数据添OK")
        else:
            print("BUG 业务设置-采购设置-采购合同条款数据添加错误")
            unittest.expectedFailure("test_DB03_01_ContractAdd")

    # 采购设置-付款阶段设置-付款阶段设置
    def test_DB03_02_PhaseAdd(self):
        """采购设置-付款阶段设置-付款阶段设置"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "系统管理", "业务设置", "采购设置", "付款阶段设置")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000727")
        v_add = driver.find_element_by_id("btnAdd")
        v_tim = time.strftime("%y%m%d%H%M")
        if  v_add.is_displayed():
            v_add.click()
            time.sleep(2)
            driver.find_element_by_id("txtName").send_keys("付款名称Auto" + v_tim)
            driver.find_element_by_id("txtWarningDays").send_keys(random.randint(1,100))
            driver.find_element_by_id("BtnSaveForm").click()
            time.sleep(3)
            print("业务设置-采购设置-付款阶段设置添加报警天数正常")
        else:
            print("BUG 业务设置-采购设置-付款阶段设置添加报警天数正常错误")
            unittest.expectedFailure("test_DB03_02_PhaseAdd")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(DB03_Purchase("test_DB03_01_ContractAdd"))
    testsuit.addTest(DB03_Purchase("test_DB03_02_PhaseAdd"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)