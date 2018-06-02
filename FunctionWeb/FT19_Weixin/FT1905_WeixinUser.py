
from PubliCode.webClass import *


class WeixinUser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        # self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        ClasMenu.menu_full_text(self, "移动端配置", "微信企业号", "微信用户管理",)
        # 移动到页面顶部，防止对象遮挡
        time.sleep(2)
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000615")

    """移动端配置-微信企业号-微信用户管理【编辑】"""
    def test_1905_01_edit(self):
        """移动端配置-微信企业号-微信用户管理【编辑】"""
        driver = self.driver
        driver.find_element_by_id("btnEdit").click()
        time.sleep(2)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "选择需要" in i.text:
                print(i.text)
                ClasForm.form_button_yes(self, "确定")
            else:
                print(i.text)
                unittest.expectedFailure("test_1905_01_edit")
        v_list = driver.find_elements_by_class_name("x-grid3-row")
        v_list[2].click()
        driver.find_element_by_id("btnEdit").click()
        time.sleep(2)
        driver.find_element_by_id("btnSave").click()
        time.sleep(2)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功" in i.text:
                print(i.text)
            else:
                print(i.text)
                unittest.expectedFailure("test_1905_01_edit")

    """移动端配置-微信企业号-微信用户管理【删除】"""
    def test_1905_02_delete(self):
        """移动端配置-微信企业号-微信用户管理【删除】"""
        driver = self.driver
        driver.find_element_by_id("BtnDelUser").click()
        time.sleep(2)
        v_title = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_title:
            if "请选择需要删除" in i.text:
                print(i.text)
                break
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/weixin/test_1905_02_delete.jpg")
                print(i.text)
                unittest.expectedFailure("test_1905_02_delete")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    unittest.main()