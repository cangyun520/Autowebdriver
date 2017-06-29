# -*- coding: utf-8 -*-
from PubliCode.onlineClass import *


class CustomEvent(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        # self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        ClasMenu.menu_full_text(self, "移动端配置", "微信企业号", "自定义事件",)
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000595")

    """移动端配置-微信企业号-自定义事件添加"""
    def test_1904_add(self):
        """移动端配置-微信企业号-自定义事件添加"""
        driver = self.driver
        driver.find_element_by_id("btnAdd").click()
        time.sleep(3)
        driver.switch_to.frame("winDetail_IFrame")
        v_tim = time.strftime("%y%m%d%H%M")
        # 事件名称
        driver.find_element_by_id("txtTitle").send_keys("自定义事件_" + v_tim)
        # 事件key
        driver.find_element_by_id("txtEventKey").send_keys(v_tim)
        driver.find_element_by_xpath("//*[@id='txtContent_Container']/div/span").click()
        time.sleep(3)
        v_list = driver.find_elements_by_class_name("x-grid3-row")
        if len(v_list) > 0:
            v_list[0].click()
            driver.find_element_by_id("Button1").click()
            time.sleep(1)
            driver.find_element_by_id("btnSave").click()
            time.sleep(2)
            v_tip = driver.find_elements_by_class_name("ext-mb-text")
            for i in v_tip:
                if "成功" in i.text:
                    print(i.text)
                else:
                    print(i.text)
                    unittest.expectedFailure("test_1904_add")
        else:
            print("回复内容为空")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(CustomEvent("test_DB07_05_MenuRelease"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)