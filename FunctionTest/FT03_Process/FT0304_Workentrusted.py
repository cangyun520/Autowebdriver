
import random
from PubliCode.onlineClass import *
'''
    *   Arvin
    *   2017-01-13
'''


class Workentrusted(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        ClasMenu.menu_full_text(self, "流程处理", "委托工作", "已委托工作")
        driver.switch_to.frame("frame_tab_PM000089")

    # 流程处理-已委托工作
    def test_0304(self):
        """流程处理-已委托工作-【查询】检查"""
        driver = self.driver
        v_list_no = driver.find_element_by_xpath("//*[@id='ext-gen25']/div/table/thead/tr/td[1]")
        try:
            v_list_no.is_displayed()
            print("已委托工作-页面-显示正常")
        except ImportError:
            print("BUG 已委托工作-【查询】-不显示")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(Workentrusted("test_0301"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)