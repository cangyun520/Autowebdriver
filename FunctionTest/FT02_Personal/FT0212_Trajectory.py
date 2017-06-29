
from PubliCode.onlineClass import *


class Trajectory(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        # self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_part_text(self, "事务处理", "外勤管理", "外勤轨迹")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000825")

    """事务处理-外勤管理-外勤轨迹面检查"""
    def test_0212_01_check(self):
        """事务处理-外勤管理-外勤轨迹面检查"""
        driver = self.driver
        v_check = driver.find_element_by_id("btnQueryList")
        if v_check.is_displayed():
            v_check.click()
            time.sleep(3)
            for i in driver.find_elements_by_tag_name("button"):
                if "地图查询" in i.text:
                    pass
                    break
        else:
            driver.get_screenshot_as_file(root_path() + "TestPicture/oa/test_0212_01_check.jpg")
            unittest.expectedFailure("test_0212_01_check")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    unittest.main()