# -*- coding: utf-8 -*-
from PubliCode.onlineClass import *


class HTRemove(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "人事管理", "员工合同", "合同变更")
        driver.switch_to.frame("frame_tab_PM000944")

    """人事管理-员工合同-合同变更"""
    def test_0521_01(self):
        """人事管理-员工合同-合同变更"""
        driver = self.driver
        v_button = driver.find_elements_by_tag_name("button")
        for i in v_button:
            if "查询" in i.text:
                print("页面显示正常")
                break
            else:
                unittest.expectedFailure("test_0521_01")
                driver.get_screenshot_as_file(root_path() + 'TestPicture/hr/test_0521_01.jpg')

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    unittest.main()
