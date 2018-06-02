
from PubliCode.webClass import *


class Enterprise(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        # self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        ClasMenu.menu_full_text(self, "移动端配置", "微信企业号", "企业号设置",)
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000598")

    """系统管理-微信企业号-企业号设置-【添加】检查"""
    def test_1901_add(self):
        """系统管理-微信企业号-企业号设置-【添加】检查"""
        driver = self.driver
        driver.find_element_by_id("btnAdd").click()
        time.sleep(2)
        v_title = driver.find_elements_by_class_name("x-window-header-text")
        for i in v_title:
            if "企业号设置" in i.text:
                print(i.text)
                break
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/weixin/test_1901_add.jpg")
                print(i.text)
                unittest.expectedFailure("test_1901_add")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(Enterprise("test_1214_Positioning"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)