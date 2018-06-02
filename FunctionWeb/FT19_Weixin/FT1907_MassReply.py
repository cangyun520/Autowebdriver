# -*- coding: utf-8 -*-
from PubliCode.webClass import *


class MassReply(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.PhantomJS()
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        ClasMenu.menu_full_text(self, "移动端配置", "微信企业号", "群发管理")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000738")

    """移动端配置-微信企业号-企业回复管理添加"""
    def test_1907_01_Keyword(self):
        """移动端配置-微信企业号-关键字回复添加"""
        driver = self.driver
        driver.find_element_by_id("cbQyApp").click()
        time.sleep(1)
        v_prj = driver.find_elements_by_class_name("x-combo-list-item")
        v_prj[random.randint(0, len(v_prj) - 1)].click()
        driver.find_element_by_id("btnSelect").click()
        driver.find_element_by_id("btnAdd").click()
        time.sleep(2)

        # 添加页面
        driver.switch_to.frame("winEdit_IFrame")
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
        # 内容
        driver.find_element_by_xpath("//*[@id='x-form-el-tfContent']/div/span").click()
        time.sleep(2)
        v_text = driver.find_elements_by_class_name("x-grid3-row")
        for i in v_text:
            print(i.text)
        v_text[0].click()
        driver.find_element_by_id("Button2").click()
        time.sleep(1)
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
    unittest.main()
