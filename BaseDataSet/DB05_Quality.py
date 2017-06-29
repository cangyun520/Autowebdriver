# -*- coding: utf-8 -*-
from PubliCode.onlineClass import *


class DB05_Quality(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)

    # 系统管理-业务设置-质检设置
    def test_DB05_01_SubmissionType(self):
        """业务设置-质检设置-送检类型添加功能检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "订货管理", "系统管理", "业务设置", "质检设置", "送检类型")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000838")
        v_add = driver.find_element_by_id("btnAdd")
        v_tim = time.strftime("%y%m%d%H%M")
        if v_add.is_displayed():
            v_add.click()
            time.sleep(2)
            driver.find_element_by_id("txtTitle_F").send_keys("送检类型Auto" + v_tim)
            driver.find_element_by_id("BtnSaveForm").click()
            time.sleep(3)
            print("质检设置-送检类型-添加数据OK")
        else:
            print("BUG 质检设置-送检类型-添加数据错误")
            unittest.expectedFailure("test_DB05_01_SubmissionType")

    # 业务设置-质检设置-质检方式添加
    def test_DB05_02_QCManner(self):
        """业务设置-质检设置-质检方式添加功能检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "订货管理", "系统管理", "业务设置", "质检设置", "质检方式")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000837")
        v_add = driver.find_element_by_id("btnAdd")
        v_tim = time.strftime("%y%m%d%H%M")
        if v_add.is_displayed():
            v_add.click()
            time.sleep(2)
            driver.find_element_by_id("txtTitle_F").send_keys("质检方式Auto" + v_tim)
            driver.find_element_by_id("BtnSaveForm").click()
            time.sleep(3)
            print("质检设置-质检方式-添加数据OK")
        else:
            print("BUG 质检设置-质检方式-添加数据错误")
            unittest.expectedFailure("test_DB05_02_QCManner")

    # 业务设置-质检设置-质检依据添加
    def test_DB05_03_QCEvidence(self):
        """业务设置-质检设置-质检依据添加功能检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "订货管理", "系统管理", "业务设置", "质检设置", "质检依据")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000839")
        v_tim = time.strftime("%y%m%d%H%M")
        if driver.find_element_by_id("btnAdd").is_displayed():
            driver.find_element_by_id("btnAdd").click()
            time.sleep(2)
            driver.find_element_by_id("txtTitle_F").send_keys("质检依据Auto" + v_tim)
            driver.find_element_by_id("BtnSaveForm").click()
            time.sleep(3)
            print("质检设置-质检依据-添加数据OK")
        else:
            print("BUG 质检设置-质检依据-添加数据错误")
            unittest.expectedFailure("test_DB05_03_QCEvidence")
            
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(DB05_Quality("test_DB05_Quality_SubmissionType"))
    testsuit.addTest(DB05_Quality("test_DB05_Quality_QCManner"))
    testsuit.addTest(DB05_Quality("test_DB05_Quality_QCEvidence"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)