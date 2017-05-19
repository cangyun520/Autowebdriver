
from PubliCode.onlineClass import *
from PubliCode.randData import *
'''
    *   Arvin
    *   2017-01-13
'''


class MyReport(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "报表平台", "我的收藏报表")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000014")

    '''报表平台-我的收藏报表查询'''
    def test_1505_01_Look(self):
        """报表平台-我的收藏报表查询功能"""
        driver = self.driver
        v_check = driver.find_element_by_id("btnSearch")
        if v_check.is_displayed():
            v_check.click()
        else:
            driver.get_screenshot_as_file(root_path() + "TestPicture/Report/test_1505_01_Look.jpg")
            unittest.expectedFailure("test_1505_01_Look")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    unittest.main()
