
from PubliCode.onlineClass import *

'''
    *   Arvin
    *   2017-05-13
'''


class IDRemind(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "人事管理", "人员管理", "证照提醒")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000889")

    '''人事管理-人员管理-证照提醒'''
    def test_0504_01_Look(self):
        """人事管理-人员管理-证照提醒"""
        driver = self.driver
        v_check = driver.find_element_by_id("btnSearch")
        if v_check.is_displayed():
            pass
        else:
            driver.get_screenshot_as_file(root_path() + "TestPicture/oa/test_0504_01_Look.jpg")
            unittest.expectedFailure("test_0504_01_Look")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    unittest.main()
    """# 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(IDRemind("test_0504_01_Look"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)
    """