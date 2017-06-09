from PubliCode.config import *
from PubliCode.onlineClass import *
from PubliCode.randData import *
'''
    *   Arvin
    *   2017-01-13
'''


class NewLook(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        ClasMenu.menu_full_text(self, "行政办公", "新闻公告", "查看新闻公告")
        driver.switch_to.frame("frame_tab_PM000292")

    """行政办公-新闻公告-查看新闻公告"""

    def test_0409_01_Look(self):
        """行政办公-新闻公告-查看新闻公告"""
        driver = self.driver
        v_trs = driver.find_elements_by_class_name("fa-eye")
        if len(v_trs) > 0:
            v_trs[0].click()
            time.sleep(3)
            driver.switch_to.default_content()
            # 进入到信息详情页面
            driver.switch_to.frame("frame_tab_PM000291")
            v_check = driver.find_element_by_id("btnPrint")
            if v_check.is_displayed():
                pass
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/oa/test_0409_01_Look.jpg")
                unittest.expectedFailure("test_0409_01_Look")
        else:
            print("列表数据为空，不操作")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(NewLook("test_0409_01_Look"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)