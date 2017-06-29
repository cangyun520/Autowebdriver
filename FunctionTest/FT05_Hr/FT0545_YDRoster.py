
from PubliCode.onlineClass import *
'''
    *   Arvin
    *   2017-05-13
'''


class YDRoster(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "人事管理", "员工异动", "员工花名册")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM001008")

    '''人事管理-员工异动-员工花名册'''
    def test_0545_01_Look(self):
        """人事管理-员工异动-员工花名册"""
        driver = self.driver
        v_check = driver.find_element_by_id("btnQuery")
        if v_check.is_displayed():
            pass
        else:
            driver.get_screenshot_as_file(root_path() + "TestPicture/oa/test_0545_01_Look.jpg")
            unittest.expectedFailure("test_0545_01_Look")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    unittest.main()
