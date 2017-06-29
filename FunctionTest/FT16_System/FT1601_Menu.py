# -*- coding: utf-8 -*-
from PubliCode.onlineClass import *


class Menu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        ClasLogin.login_setup(self)
        driver = self.driver
        ClasMenu.menu_full_text(self, u"系统管理", u"菜单设置", u"菜单配置")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        # 切换到右侧表单页面
        driver.switch_to.frame("frame_tab_PM000179")

    '''系统管理-菜单管理-菜单配置'''
    def test_1601_Config(self):
        """系统初始化-菜单配置-菜单配置"""
        driver = self.driver
        driver.find_element_by_id("txtSelectMenuName").send_keys("动态表单")
        driver.find_element_by_id("btnSelect").click()
        time.sleep(2)
        v_expand = driver.find_element_by_id("btnExpand")
        try:
            v_expand.is_displayed()
            print("系统管理-系统初始化-菜单配置-页面显示正常")
        except ImportError:
            print("BUG 系统初始化-菜单配置-【全部展开】-不显示")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(Menu("test_1616_Custom"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)