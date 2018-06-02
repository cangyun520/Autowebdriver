# -*- coding: utf-8 -*-
from PubliCode.webClass import *


class Report(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, u"系统管理", u"报表设置", u"查询管理器")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000176")

    """系统管理-报表设置-查询管理器SQL为空执行校验"""
    def test_1501_SqlNone(self):
        """系统管理-报表设置-查询管理器SQL为空执行校验"""
        driver = self.driver
        driver.find_element_by_id("btnRefresh").click()
        time.sleep(1)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "请输入查询语句" in i.text:
                print(i.text)
            else:
                print(i.text)
                unittest.expectedFailure("test_1501_SqlNone")

    """系统管理-报表设置-查询管理器SQL为空执行校验"""
    def test_1501_ExportNone(self):
        """系统管理-报表设置-查询管理器SQL为空执行校验"""
        driver = self.driver
        driver.find_element_by_id("btnexl").click()
        time.sleep(1)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "没有导出数据" in i.text:
                print(i.text)
            else:
                print(i.text)
                unittest.expectedFailure("test_1501_ExportNone")

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