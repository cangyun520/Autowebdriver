# -*- coding: utf-8 -*-
from PubliCode.onlineClass import *


class IntWeixin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)

    '''系统管理-移动端配置-应用菜单'''
    def test_Int03_01_MenuRelease(self):
        """移动端配置-微信企业号-应用菜单发布功能检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "订货管理", "移动端配置", "钉钉号", "微信企业号", "应用菜单")
        driver.switch_to.frame("frame_tab_PM000597")
        driver.find_element_by_id("cbQyApp").click()
        # 选择应用
        v_applications = driver.find_elements_by_class_name("x-combo-list-item")
        v_applications[0].click()
        v_initial = 1
        while v_initial < len(v_applications):
            driver.find_element_by_id("cbQyApp").click()
            v_applications[v_initial].click()
            time.sleep(1)
            driver.find_element_by_id("btnSave").click()
            time.sleep(1)
            for i in driver.find_elements_by_class_name("x-btn-text"):
                if i.text == "是":
                    i.click()
                    time.sleep(3)
                    break
            v_tip = driver.find_elements_by_class_name("ext-mb-text")
            for ii in v_tip:
                if "发布成功" in ii.text:
                    for i3 in driver.find_elements_by_class_name("x-btn-text"):
                        if i3.text == "确定":
                            i3.click()
                            time.sleep(2)
                            print("移动端配置-应用菜单-应用菜单发布OK -" + str(v_initial))
                            break
                else:
                    print("BUG 移动端配置-应用菜单-应用菜单发布失败")
                    unittest.expectedFailure("test_Int03_01_MenuRelease")
            v_initial += 1

    def test_Int03_02_UsersSync(self):
        """移动端配置-微信企业号-微信用户管理同步功能检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "订货管理", "移动端配置", "钉钉号", "微信企业号", "微信用户管理")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000615")
        driver.find_element_by_id("s_txtName").send_keys("arvin")
        time.sleep(1)
        driver.find_element_by_id("btnSearch").click()
        time.sleep(2)
        for i in driver.find_elements_by_class_name("x-grid3-row-table"):
            i.click()
        time.sleep(1)
        driver.find_element_by_id("BtnSynQyUserSelected").click()
        time.sleep(2)
        for i in driver.find_elements_by_class_name("x-btn-mc"):
            if i.text == "是":
                i.click()
                break
        time.sleep(5)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "已成功同步" in i.text:
                print(i.text)
            else:
                print("BUG 移动端配置-微信企业号-微信用户管理同步失败")
                unittest.expectedFailure("test_Int03_02_UsersSync")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
