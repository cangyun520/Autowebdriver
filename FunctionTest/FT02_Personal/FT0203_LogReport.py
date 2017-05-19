
from PubliCode.onlineClass import *
import traceback


class LogReport(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        # self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_part_text(self, "事务处理", "工作日志", "日志报表")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000489")

    """事务处理-工作日志-日志报表页面检查"""
    def test_0203_01_check(self):
        """事务处理-工作日志-日志报表页面检查"""
        driver = self.driver
        v_check = driver.find_element_by_id("submitQuery")
        if v_check.is_displayed():
            pass
        else:
            driver.get_screenshot_as_file(root_path() + "TestPicture/oa/test_0203_01_check.jpg")
            unittest.expectedFailure("test_0203_01_check")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    unittest.main()