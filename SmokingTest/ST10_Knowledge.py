# -*- coding: utf-8 -*-
from PubliCode.onlineClass import *

class ST10_Knowledge(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)

# # ------知识文库------
    def test_1001_File(self):
        """知识文库-公用文件柜-【上传】检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"知识文库", u"公用文件柜")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000809")
        v_add = driver.find_element_by_id("btnAdd")
        try:
            v_add.is_displayed()
        except ImportError:
            print("BUG 知识文库-公用文件柜-【上传】-不显示")
        else:
            print("知识文库-公用文件柜-页面显示正常")

    def test_1002_Harddisk(self):
        driver = self.driver
        driver.find_element_by_link_text(u"知识文库").click()
        time.sleep(2)
        # 移动到页面底部，防止对象遮挡
        js_down = "window.scrollTo(0,500)"
        driver.execute_script(js_down)
        driver.find_element_by_link_text(u"网络硬盘").click()
        time.sleep(2)
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)

        driver.switch_to_frame("frame_tab_PM000810")
        v_add = driver.find_element_by_id("btnAdd")
        try:
            v_add.is_displayed()
        except ImportError:
            print("BUG 知识文库-网络硬盘-【上传】-不显示")
        else:
            print("知识文库-网络硬盘-页面显示正常")

    def test_1003_Harddisk(self):
        driver = self.driver
        driver.find_element_by_link_text(u"知识文库").click()
        time.sleep(2)
        # 移动到页面底部，防止对象遮挡
        js_down = "window.scrollTo(0,500)"
        driver.execute_script(js_down)
        driver.find_element_by_link_text(u"图片浏览").click()
        time.sleep(2)
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)

        driver.switch_to_frame("frame_tab_PM000811")
        v_add = driver.find_element_by_id("btnAdd")
        try:
            v_add.is_displayed()
        except ImportError:
            print("BUG 知识文库-图片浏览-【上传】-不显示")
        else:
            print("知识文库-图片浏览-页面显示正常")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(ST10_Knowledge("test_1003_Harddisk"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)