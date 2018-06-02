# -*- coding: utf-8 -*-
from PubliCode.webClass import *

class ST07_Crm(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)

    def test_050401_01_Add(self):
        """客户关系-竞争对手维护--新增单据功能"""
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "客户关系", "售前管理", "竞争对手维护")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM001073")
        # 新增
        try:
            driver.find_element_by_id("btnAdd").is_displayed()
            print("客户关系-服务呼叫-页面-显示正常")
        except ImportError:
            print("BUG 客户关系-服务呼叫-【添加】-不显示")

    def test_0702_ServiceCall(self):
        """客户关系-服务呼叫-【添加】检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "客户关系", "售后管理", "服务呼叫")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000277")
        try:
            driver.find_element_by_link_text("常规").is_displayed()
            print("客户关系-服务呼叫-页面-显示正常")
        except ImportError:
            print("BUG 客户关系-服务呼叫-【添加】-不显示")

    def test_0703_Solution(self):
        """客户关系-解决方案-【添加】检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "客户关系", "售后管理", "解决方案")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000279")
        try:
            driver.find_element_by_link_text("描述").is_displayed()
            print("客户关系-解决方案-页面-显示正常")
        except ImportError:
            print("BUG 客户关系-解决方案-【添加】-不显示")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(ST07_Crm("test_0703_Solution"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)