# -*- coding: utf-8 -*-
import random
import time
import unittest
from selenium import webdriver
from PubliCode.onlineClass import *


class EnterpriseReply(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        ClasMenu.menu_full_text(self, "移动端配置", "微信企业号", "企业回复管理")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000653")

    """移动端配置-微信企业号-企业回复管理添加"""
    def test_1904_01_Keyword(self):
        """移动端配置-微信企业号-关键字回复添加"""
        driver = self.driver
        driver.switch_to.frame("pText_IFrame")
        driver.find_element_by_id("cbQyApp").click()
        time.sleep(1)
        v_list = driver.find_elements_by_class_name("x-combo-list-item")
        v_total = []
        for i in v_list:
            v_total.append(i.text)
        v_number = random.randint(0, len(v_list)-0)
        v_list[v_number].click()
        driver.find_element_by_id("btnAdd").click()
        v_tim = time.strftime("%m%d%H")
        # 关键字
        driver.find_element_by_id("txtKeyword").send_keys(v_tim)
        # 标题
        driver.find_element_by_id("txtTitle").send_keys(v_total[v_number] + "_" + v_tim)
        # 回复内容
        driver.find_element_by_xpath("//*[@id='tfContent_Container']/div/span").click()
        time.sleep(2)
        v_l_content = driver.find_elements_by_class_name("x-grid3-row")
        v_l_content[random.randint(0, len(v_l_content)-1)].click()
        driver.find_element_by_id("Button1").click()
        time.sleep(2)
        driver.find_element_by_id("btnSave").click()
        time.sleep(2)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功" in i.text:
                print(i.text)
            elif "已存在" in i.text:
                print(i.text)
            else:
                print(i.text)
                unittest.expectedFailure("test_1904_01_Keyword")

    """移动端配置-微信企业号-关注时回复添加"""
    def test_1904_02_Concern(self):
        """移动端配置-微信企业号-关注时回复添加"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "关注时回复")
        driver.switch_to.frame("pFocus_IFrame")
        # 回复内容
        driver.find_element_by_xpath("//*[@id='x-form-el-tfContent']/div/span").click()
        time.sleep(2)
        v_l_content = driver.find_elements_by_class_name("x-grid3-row")
        v_l_content[random.randint(0, len(v_l_content)-1)].click()
        driver.find_element_by_id("Button3").click()
        time.sleep(2)
        driver.find_element_by_id("btnSave").click()
        time.sleep(2)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功" in i.text:
                print(i.text)
            else:
                print(i.text)
                unittest.expectedFailure("test_1904_02_Concern")

    def test_1904_03_Exception(self):
        """移动端配置-微信企业号-关注时回复添加"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "异常回复")
        driver.switch_to.frame("pException_IFrame")
        # 回复内容
        driver.find_element_by_xpath("//*[@id='x-form-el-tfContent']/div/span").click()
        time.sleep(2)
        v_l_content = driver.find_elements_by_class_name("x-grid3-row")
        v_l_content[random.randint(0, len(v_l_content)-1)].click()
        driver.find_element_by_id("Button3").click()
        time.sleep(2)
        driver.find_element_by_id("btnSave").click()
        time.sleep(2)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功" in i.text:
                print(i.text)
            else:
                print(i.text)
                unittest.expectedFailure("test_1904_03_Exception")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(EnterpriseReply("test_1904_02_Concern"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)