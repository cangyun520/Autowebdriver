
import random
from PubliCode.onlineClass import *
'''
    *   Arvin
    *   2017-01-13
'''


class Workcontact(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        ClasMenu.menu_full_text(self, "流程处理", "流程进度跟踪")
        driver.switch_to.frame("frame_tab_PM000030")

    # 流程处理-流程进度跟踪
    def test_0307_01(self):
        """流程处理-流程进度跟踪-【查询】检查"""
        driver = self.driver
        v_seach = driver.find_element_by_id("btnSelect")
        try:
            v_seach.is_displayed()
            print("流程进度跟踪-页面-显示正常")
        except ImportError:
            print("BUG 流程进度跟踪-【查询】-不显示")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(Workcontact("test_0307_01"))
    testsuit.addTest(Workcontact("test_0307_02"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)