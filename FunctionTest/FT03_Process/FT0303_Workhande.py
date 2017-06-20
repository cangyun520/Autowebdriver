
from PubliCode.onlineClass import *
'''
    *   Arvin
    *   2017-01-13
'''


class Workhande(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        # self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        ClasMenu.menu_full_text(self, "事务处理", "流程处理", "办结工作")
        driver.switch_to.frame("frame_tab_PM000032")

    '''流程处理-办结工作'''
    def test_0303(self):
        """流程处理-办结工作-【查询】检查"""
        driver = self.driver
        v_seach = driver.find_element_by_id("ext-gen57")
        try:
            v_seach.is_displayed()
            print("办结工作-页面-显示正常")
        except ImportError:
            print("BUG 办结工作-【查询】-不显示")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(Workhande("test_0302"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)