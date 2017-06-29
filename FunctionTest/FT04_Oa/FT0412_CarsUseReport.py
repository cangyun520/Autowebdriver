# -*- coding: utf-8 -*-

from PubliCode.onlineClass import *
'''
    *   Arvin
    *   2017-05-13
'''


class CarsUseReport(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "行政办公", "车辆管理", "车辆预约情况")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000805")

    '''行政办公-车辆管理-车辆预约情况'''
    def test_0412_01_Look(self):
        """行政办公-车辆管理-车辆预约情况"""
        driver = self.driver
        v_span = driver.find_elements_by_tag_name("span")
        for i in v_span:
            if "图例说明" in i.text:
                pass
                break
        else:
            driver.get_screenshot_as_file(root_path() + "TestPicture/oa/test_0412_01_Look.jpg")
            unittest.expectedFailure("test_0412_01_Look")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(CarsUseReport("test_0412_01_Look"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)