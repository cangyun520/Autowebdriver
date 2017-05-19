
from PubliCode.onlineClass import *
from PubliCode.randData import *
'''
    *   Arvin
    *   2017-05-13
'''


class MenuPermission(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        # self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, u"系统管理", u"权限配置", u"数据权限")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000384")

    '''系统管理-权限配置-数据权限查询'''
    def test_1612_01_Look(self):
        """系统管理-权限配置-数据权限查询"""
        driver = self.driver
        driver.find_elements_by_class_name("x-tree-node")[1].click()
        time.sleep(1)
        v_check = driver.find_element_by_id("btnSearch")
        if v_check.is_displayed():
            v_check.click()
        else:
            driver.get_screenshot_as_file(root_path() + "TestPicture/Sys/test_1612_01_Look.jpg")
            unittest.expectedFailure("test_1612_01_Look")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    unittest.main()
