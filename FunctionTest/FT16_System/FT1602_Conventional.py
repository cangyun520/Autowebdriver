# -*- coding: utf-8 -*-

from PubliCode.onlineClass import *


class Conventional(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        # self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)

    '''系统管理-常规设置'''
    def test_1602_Conventional(self):
        """系统初始化-读取B1小数位数"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"系统管理", u"常规设置", u"读取B1小数位数")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        # 切换到右侧表单页面
        driver.switch_to.frame("frame_tab_PM000389")
        v_cbx = driver.find_element_by_id("cbxIsTax")
        try:
            v_cbx.is_displayed()
            print("系统管理-系统初始化-读取B1小数位数-页面显示正常")
        except ImportError:
            print("BUG 系统初始化-读取B1小数位数-“含税”-不显示")

    '''系统初始化-常规设置-表头格式自定义'''
    def test_1602_Header(self):
        """系统初始化-常规设置-表头格式自定义"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"系统管理", u"常规设置", u"表头格式自定义")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        # 切换到右侧表单页面
        driver.switch_to.frame("frame_tab_PM000172")
        Header_btnRead = driver.find_element_by_id("btnRead")
        try:
            Header_btnRead.is_displayed()
            print("系统管理-系统初始化-表头格式自定义-页面显示正常")
        except ImportError:
            print("BUG 系统初始化-表头格式自定义-【读取文件】-不显示")

    '''系统初始化-常规设置-行格式自定义'''
    def test_1602_Row(self):
        """系统初始化-常规设置-行格式自定义"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"系统管理", u"常规设置", u"行格式自定义")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        # 切换到右侧表单页面
        driver.switch_to.frame("frame_tab_PM000255")
        v_btnSave = driver.find_element_by_id("btnSave")
        try:
            v_btnSave.is_displayed()
            print("系统管理-系统初始化-行格式自定义-页面显示正常")
        except ImportError:
            print("BUG 系统初始化-行格式自定义-【保存】-不显示")

    '''系统初始化-常规设置-自定义字段权限'''
    def test_1602_Custom(self):
        """系统初始化-常规设置-自定义字段权限"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"系统管理", u"权限配置", u"自定义字段权限")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        # 切换到右侧表单页面
        driver.switch_to.frame("frame_tab_PM000414")
        v_btnSave = driver.find_element_by_id("gpRole")
        try:
            v_btnSave.is_displayed()
            print("系统管理-系统初始化-自定义字段权限-页面显示正常")
        except ImportError:
            print("BUG 系统初始化-自定义字段权限-【角色列表】-不显示")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()

    testsuit.addTest(Conventional("test_1602_Custom"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)