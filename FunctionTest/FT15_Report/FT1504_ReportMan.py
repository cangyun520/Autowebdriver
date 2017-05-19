
from PubliCode.onlineClass import *
from PubliCode.randData import *
'''
    *   Arvin
    *   2017-01-13
'''


class ReportMan(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "报表平台", "报表管理")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000016")

    '''报表平台-报表管理查询'''
    def test_1504_01_Look(self):
        """报表平台-报表管理查询功能"""
        driver = self.driver
        v_check = driver.find_element_by_id("btnSearch")
        if v_check.is_displayed():
            v_check.click()
        else:
            driver.get_screenshot_as_file(root_path() + "TestPicture/Report/test_0211_01_check.jpg")
            unittest.expectedFailure("test_0211_01_check")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    unittest.main()
