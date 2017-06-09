from PubliCode.config import *
from PubliCode.onlineClass import *
'''
    *   Arvin
    *   2017-01-13
'''


class VoteLook(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        # self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "行政办公", "投票管理", "投票")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000481")

    '''行政办公-投票-单选投票添加'''
    def test_0413_01_add(self):
        """行政办公-投票-单选投票添加功能"""
        driver = self.driver
        v_check = driver.find_element_by_id("btnQuery")
        if v_check.is_displayed():
            pass
        else:
            driver.get_screenshot_as_file(root_path() + "TestPicture/oa/test_0211_01_check.jpg")
            unittest.expectedFailure("test_0211_01_check")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    unittest.main()
    """# 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(VoteLook("test_0413_01_add"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)
    """