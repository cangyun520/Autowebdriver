import time
import unittest
from selenium import webdriver
from PubliCode.onlineClass import *


class WorkFlow(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_part_text(self, "系统管理", "审批流程", "流程设计器")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000025")

    '''审批警报-固定流程设计-流程设计器导入流程xml'''
    def test_Int02_05(self):
        """审批警报-固定流程设计-流程设计器导入流程xml"""
        driver = self.driver
        v_total = 1
        while v_total <= 22:
            driver.find_element_by_id("btnImport").click()
            time.sleep(2)
            driver.find_element_by_id("fuImpotXml-file").send_keys(root_path() + "PubliData/workFlowData/work" + str(v_total) + ".xml")
            time.sleep(1)
            driver.find_element_by_id("btnImpot").click()
            time.sleep(2)
            driver.find_element_by_id("btnSave").click()
            time.sleep(2)
            driver.find_element_by_id("ext-comp-1109").click()
            time.sleep(2)
            v_total += 1

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(WorkFlow("test_Int02_01"))
    testsuit.addTest(WorkFlow("test_Int02_05"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)