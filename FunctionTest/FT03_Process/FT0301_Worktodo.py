
import random
from PubliCode.onlineClass import *


class Worktodo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "流程处理", "待办工作")
        driver.switch_to.frame("frame_tab_PM000040")

    # 流程处理-待办工作
    def test_0301(self):
        """流程处理-待办工作-【查询】检查"""
        driver = self.driver
        v_seach = driver.find_element_by_name("txtSearchWK")
        try:
            v_seach.is_displayed()
            print("待办工作-页面-显示正常")
        except ImportError:
            print("BUG 待办工作-【查询】-不显示")
            unittest.expectedFailure("test_0301")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(Worktodo("test_0301"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)