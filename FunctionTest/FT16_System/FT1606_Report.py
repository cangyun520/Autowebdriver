# -*- coding: utf-8 -*-
from PubliCode.onlineClass import *


class Report(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)

# # ---系统管理---系统初始化

    def test_1606_view(self):
        """系统管理-支持中心-系统视图"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"系统管理", u"支持中心", u"系统视图")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        # 切换到右侧表单页面
        driver.switch_to_frame("frame_tab_PM000385")
        v_add = driver.find_element_by_id("btnAdd")
        try:
            v_add.is_displayed()
            print("系统管理-支持中心-系统视图-页面显示正常")
        except ImportError:
            print("BUG 支持中心-系统视图-【保存已修改的字典项】-不显示")

    def test_1606_log(self):
        """系统管理-支持中心-系统日志"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"系统管理", u"支持中心", u"系统日志")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        # 切换到右侧表单页面
        driver.switch_to_frame("frame_tab_PM000008")
        v_search = driver.find_element_by_id("btnOpSearch")
        try:
            v_search.is_displayed()
            print("系统管理-支持中心-系统日志-页面显示正常")
        except ImportError:
            print("BUG 支持中心-系统日志-【查询】-不显示")

    def test_1606_help(self):
        """系统管理-支持中心-帮助中心"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"系统管理", u"支持中心", u"帮助中心")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        # 切换到右侧表单页面
        driver.switch_to_frame("frame_tab_PM000599")
        v_help = driver.find_element_by_id("Button2")
        try:
            v_help.is_displayed()
            print("系统管理-支持中心-帮助中心-页面显示正常")
        except ImportError:
            print("BUG 支持中心-帮助中心-【收起】-不显示")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(Report("test_1616_Custom"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)