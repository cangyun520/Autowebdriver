
import random
from PubliCode.onlineClass import *
'''
    *   Arvin
    *   2017-01-13
'''


class Processmonitoring(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        ClasMenu.menu_full_text(self, "事务处理", "流程处理", "流程监控")
        driver.switch_to.frame("frame_tab_PM000028")

    # 流程处理-流程监控
    def test_0309_01(self):
        """流程处理-流程监控-【查询】检查"""
        driver = self.driver
        v_seach = driver.find_element_by_id("btnSelect")
        try:
            v_seach.is_displayed()
        except ImportError:
            print("BUG 流程监控-【查询】-不显示")
        else:
            print("流程监控-页面-显示正常")

    # 流程处理-流程监控
    def test_0309_02(self):
        """流程处理-流程监控-查看流程进度跟踪"""
        driver = self.driver
        v_list = driver.find_elements_by_class_name("x-grid3-row")
        try:
            len(v_list) != 0
            v_list[random.randint(0, len(v_list) - 1)].click()
            try:
                driver.find_element_by_id("btnManage").is_displayed()
                driver.find_element_by_id("btnManage").click()
                time.sleep(3)
                for i in driver.find_elements_by_class_name("x-window-header-text"):
                    if i.text == "流程管理历史记录":
                        print("流程监控,管理历史查看页面显示OK")
                        break
            except ImportError:
                print("自由流无法查看流程")
        except ImportError:
            pass
            print("流程监控，列表无数据可操作")

    def tearDown(self):
        self.driver.quit()
        # self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    suit = unittest.suite()
    suit.addTest(Processmonitoring("test_0301"))
    suit.addTest(Processmonitoring("test_0302"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(suit)