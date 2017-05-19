
from PubliCode.onlineClass import *
from PubliCode.randData import *
'''
    *   Arvin
    *   2017-05-13
'''


class DataRelated(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        # self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, u"系统管理", u"警报设置", u"数据相关")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000181")

    '''系统管理-警报设置-数据相关查询'''
    def test_1614_01_Look(self):
        """系统管理-警报设置-数据相关查询"""
        driver = self.driver
        v_check = driver.find_element_by_id("btnSelect")
        if v_check.is_displayed():
            v_check.click()
        else:
            driver.get_screenshot_as_file(root_path() + "TestPicture/Sys/test_1614_01_Look.jpg")
            unittest.expectedFailure("test_1614_01_Look")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    unittest.main()
