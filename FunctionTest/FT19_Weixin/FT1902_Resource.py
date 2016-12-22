
from PubliCode.onlineClass import *
from PubliCode.randData import *


class Resource(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        ClasMenu.menu_full_text(self, "移动端配置", "微信企业号", "资源管理",)
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000393")

    """微信营销-资源管理-文本素材添加功能"""
    def test_1902_01_add(self):
        """微信营销-资源管理-文本素材添加功能"""
        driver = self.driver
        driver.switch_to.frame("pText_IFrame")
        driver.find_element_by_id("Button11").click()
        v_tim = time.strftime("%y%m%d%H%M")
        time.sleep(3)
        # 素材名称
        driver.find_element_by_id("txfTextMeterialName").send_keys("文本素材_" + v_tim)
        driver.find_element_by_id("txaTextMeterialContent").send_keys(fun_data_character(50, 500))
        driver.find_element_by_id("btnSaveText").click()
        time.sleep(3)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "添加成功" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/oa/test_1902_01_add.jpg")
                print(i.text)
                unittest.expectedFailure("test_1902_01_add")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(Resource("FT1902_01_add"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)