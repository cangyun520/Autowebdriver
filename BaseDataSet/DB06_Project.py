# -*- coding: utf-8 -*-
from PubliCode.webClass import *


class DB06_Project(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)

    # 系统管理-业务设置-项目设置
    def test_DB06_01_TypeAdd(self):
        """业务设置-项目设置-项目类型添加功能检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "订货管理", "系统管理", "业务设置", "项目设置", "项目类型")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000758")
        v_add = driver.find_element_by_id("btnAdd")
        v_tim = time.strftime("%y%m%d%H%M")
        if v_add.is_displayed():
            v_add.click()
            time.sleep(2)
            driver.find_element_by_id("txtTitle_F").send_keys("项目类型Auto" + v_tim)
            driver.find_element_by_id("BtnSaveForm").click()
            time.sleep(3)
            print("项目设置-项目类型-页面显示正常")
        else:
            print("BUG 项目设置-项目类型-【添加】-不显示，请检查页面是否正常")
            unittest.expectedFailure("test_DB06_01_TypeAdd")

    # 业务设置-项目设置-项目组加功
    def test_DB06_02_GroupAdd(self):
        """业务设置-项目设置-项目组加功能检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "订货管理", "系统管理", "业务设置", "项目设置", "项目组")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000759")
        v_tim = time.strftime("%m%d%H%M")
        driver.find_element_by_id("btnAdd").click()
        driver.find_element_by_id("txtTitle_F").send_keys("项目组名称Auto" + v_tim)
        time.sleep(1)
        driver.find_element_by_class_name("x-form-twin-triggers").find_element_by_id("ext-gen68").click()
        time.sleep(2)
        for i in driver.find_elements_by_class_name("x-grid3-row-checker"):
            i.click()
        time.sleep(1)
        driver.find_element_by_id("Button2").click()
        time.sleep(3)
        driver.find_element_by_id("BtnSaveForm").click()
        time.sleep(3)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "添加成功" in i.text:
                print(v_tip)
            else:
                print(v_tip)
                unittest.expectedFailure("test_DB06_02_GroupAdd")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(DB06_Project("test_DB06_01_TypeAdd"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)