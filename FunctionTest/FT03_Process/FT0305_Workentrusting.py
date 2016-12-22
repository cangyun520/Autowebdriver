
import random
from PubliCode.onlineClass import *


class Workentrusting(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        ClasMenu.menu_full_text(self, "流程处理", "委托工作", "被委托工作")
        driver.switch_to.frame("frame_tab_PM000090")

    # 流程处理-被委托工作
    def test_0305(self):
        """流程处理-被委托工作-【查询】检查"""
        driver = self.driver
        v_list_no = driver.find_element_by_xpath("//*[@id='ext-gen25']/div/table/thead/tr/td[1]")
        try:
            v_list_no.is_displayed()
            print("被委托工作-页面-显示正常")
        except ImportError:
            print("BUG 被委托工作-【查询】-不显示")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(Workentrusting("test_0301"))
    testsuit.addTest(Workentrusting("test_0302"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)