# -*- coding: utf-8 -*-
from PubliCode.onlineClass import *

class ST06_Expenses(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)

# # ------费用管理------
    def test_0601_ExpensesApply(self):
        """费用管理-费用申请-【添加】检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "费用管理", "费用申请")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000764")
        try:
            driver.find_element_by_id("btnAdd").is_displayed()
            print("费用管理-费用申请-页面-显示正常")
        except ImportError:
            print("BUG 费用管理-费用申请-【添加】-不显示")
            unittest.expectedFailure("test_075_ExpensesApply")

    def test_0602_Circulate_TripApply(self):
        """费用管理-出差借支申请-【添加】检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "费用管理", "借还款", "出差借支申请")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000767")
        try:
            driver.find_element_by_id("btnAdd").is_displayed()
        except ImportError:
            print("BUG 费用管理-出差借支申请-【添加】-不显示")
        else:
            print("费用管理-出差借支申请-页面-显示正常")

    def test_0603_Circulate_Borrowing(self):
        """费用管理-借款-【添加】检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "费用管理", "借还款", "借款")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000768")
        try:
            driver.find_element_by_id("btnAdd").is_displayed()
            print("费用管理-借款-页面-显示正常")
        except ImportError:
            print("BUG 费用管理-借款-【添加】-不显示")

    def test_0604_Circulate_Repayment(self):
        """费用管理-还款-【添加】检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "费用管理", "借还款", "还款")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000769")
        try:
            driver.find_element_by_id("btnAdd").is_displayed()
            print("费用管理-还款-页面-显示正常")
        except ImportError:
            print("BUG 费用管理-还款-【添加】-不显示")

    def test_0605_Reimbursement_Expenses(self):
        """费用管理-费用报销-【添加】检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "费用管理", "报销管理", "费用报销")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000784")
        try:
            driver.find_element_by_id("btnAdd").is_displayed()
            print("费用管理-费用报销-页面-显示正常")
        except ImportError:
            print("BUG 费用管理-费用报销-【添加】-不显示")

    def test_0606_Reimbursement_Travel(self):
        """费用管理-差旅费报销-【添加】检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "费用管理", "报销管理", "差旅费报销")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000782")
        try:
            driver.find_element_by_id("btnAdd").is_displayed()
            print("费用管理-差旅费报销-页面-显示正常")
        except ImportError:
            print("BUG 费用管理-差旅费报销-【添加】-不显示")

    def test_0607_Payment(self):
        """费用管理-付款-【添加】检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "费用管理", "付款")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000786")
        try:
            driver.find_element_by_id("btnAdd").is_displayed()
            print("费用管理-付款-页面-显示正常")
        except ImportError:
            print("BUG 费用管理-付款-【添加】-不显示")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(ST06_Expenses("test_0607_Payment"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)