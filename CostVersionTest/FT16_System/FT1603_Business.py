# -*- coding: utf-8 -*-
from PubliCode.onlineClass import *


class Business(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)

    '''系统管理-系统初始化'''
    def test_1603_FreeStream(self):
        """审批流程-警报设置-自由流设计单据UI检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"系统管理", u"流程设置", u"自由流设计")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000981")
        v_search = driver.find_element_by_id("btnSearch")
        try:
            v_search.is_displayed()
            print("系统管理-审批流程-自由流设计-页面显示正常")
        except ImportError:
            print("BUG 审批流程-自由流设计-【查询】-不显示")

    # 系统管理-审批流程-流程看板
    def test_1603_Billboard(self):
        """系统管理-审批流程-流程看板"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"系统管理", u"流程设置", u"流程看板")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        # 切换到右侧表单页面
        driver.switch_to.frame("frame_tab_PM001019")
        v_search = driver.find_element_by_id("btnSearch")
        try:
            v_search.is_displayed()
            print("系统管理-审批流程-流程看板-页面显示正常")
        except ImportError:
            print("BUG 审批流程-流程看板-【查询】-不显示")
# # ---系统管理---支持中心

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()

    testsuit.addTest(Business("test_1603_FreeStream"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)