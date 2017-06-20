# -*- coding: utf-8 -*-
from PubliCode.config import *
from PubliCode.onlineClass import *


class OvertimeApply(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "人事管理", "考勤管理", "考勤制度", "工作日历")
        driver.switch_to.frame("frame_tab_PM000908")

    """人事管理-考勤管理-考勤制度-工作日历"""
    def test_0531_01(self):
        """人事管理-考勤管理-考勤制度-工作日历"""
        driver = self.driver
        v_button = driver.find_elements_by_tag_name("button")
        for i in v_button:
            if "查询" in i.text:
                print("员工考勤档案页面显示正常")
                break
            else:
                unittest.expectedFailure("test_0531_01")
                driver.get_screenshot_as_file(root_path() + 'TestPicture/hr/test_0531_01.jpg')

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    unittest.main()
