# -*- coding: utf-8 -*-
import random
import time
import unittest
from selenium import webdriver
from PubliCode.onlineClass import *


class MassReply(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        ClasMenu.menu_full_text(self, "移动端配置", "微信企业号", "群发管理")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000738")

    """移动端配置-微信企业号-企业回复管理添加"""
    def test_1907_01_Keyword(self):
        """移动端配置-微信企业号-关键字回复添加"""
        driver = self.driver
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
        time.sleep(3)
        driver.switch_to_frame("winEdit_IFrame")
        v_list_user = driver.find_elements_by_class_name("x-tree-node")
        v_list_user[1].click()
        v_list_user[2].click()
        v_list_user[3].click()
        v_list_user[4].click()
        v_list_user[5].click()
        v_list_user[6].click()
        v_list_user[7].click()
        v_list_user[8].click()
        v_list_user[9].click()
        # n = 2
        # while n < 10:
        #     v_list_user[n].click()
        #     print(v_list_user[n].text)
        # n += 1
        # 内容
        driver.find_element_by_xpath("//*[@id='x-form-el-tfContent']/div/span").click()
        time.sleep(2)
        v_l_content = driver.find_elements_by_class_name("x-grid3-row")
        v_l_content[random.randint(0, len(v_l_content)-1)].click()
        driver.find_element_by_id("Button2").click()
        time.sleep(2)
        driver.find_element_by_id("btnAdd").click()
        time.sleep(2)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功" in i.text:
                print(i.text)
            elif "部分发送失败" in i.text:
                print(i.text)
            else:
                print(i.text)
                unittest.expectedFailure("test_1907_01_Keyword")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(MassReply("test_1907_02_Concern"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)