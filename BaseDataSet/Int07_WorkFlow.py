import time
import unittest
from selenium import webdriver
from PubliCode.onlineClass import *
import re


class Int07_WorkFlow(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver

        # 打开菜单
        ClasMenu.menu_part_text(self, "订货管理", "系统管理", "流程设置", "流程设计器")
        driver.switch_to.frame("frame_tab_PM000025")

    '''审批警报-固定流程设计-流程设计器导入流程xml'''

    def test_Int07_01(self):
        """审批警报-固定流程设计-流程设计器导入流程xml"""
        driver = self.driver

        # 第二版，通用模版导入
        driver.find_element_by_id("btnNewAdd").click()
        driver.find_element_by_xpath(
            "//*[@id='ext-comp-1005']/table/tbody/tr/td/table/tbody/tr/td/div/div/div/span").click()
        time.sleep(1)
        v_lists = driver.find_elements_by_class_name("x-tree-node-anchor")
        v_meus = []
        for i in v_lists:
            if re.search('[^\W]管理', i.text):
                pass
            elif re.search('[^\W]料单', i.text):
                pass
            elif re.search('[\W]合同', i.text):
                pass
            elif re.search('[^\W]申请单', i.text):
                pass
            elif re.search('[^\W]申请', i.text):
                pass
            elif re.search('[^\W]报销单', i.text):
                pass
            else:
                v_meus.append(i.text)
        for j in v_meus:
            l = ['行政办公', '入职申请', '借料还料', '订货单', '库存盘点', '员工异动', '盘点登记单']
            for d in l:
                if d in j:
                    v_meus.remove(j)
        # print(v_meus)
        # quit()
        n = len(v_meus)
        m = 0
        driver.find_element_by_link_text(v_meus[m]).click()
        time.sleep(1)

        # 开始循环

        while m < n:
            # 导入
            driver.find_element_by_id("btnImport").click()
            driver.find_element_by_id("fuImpotXml-file").send_keys(root_path() + "PubliData/xml/通用4步审批模版.xml")
            time.sleep(1)
            driver.find_element_by_id("btnImpot").click()
            time.sleep(1)

            driver.find_element_by_xpath(
                "//*[@id='ext-comp-1005']/table/tbody/tr/td/table/tbody/tr/td/div/div/div/span").click()
            time.sleep(1)
            driver.find_element_by_link_text(v_meus[m]).click()
            time.sleep(2)

            driver.find_element_by_id("btnSave").click()
            time.sleep(2)

            v_tip = driver.find_elements_by_class_name("ext-mb-text")
            # 提示
            for i in v_tip:
                if "保存成功" in i.text:
                    ClasForm.form_button_yes(self, "确定")
                    print(v_meus[m])
                else:
                    driver.get_screenshot_as_file(root_path() + "TestPicture/BD/test_Int07_01.jpg")
                    print(m)
                    unittest.expectedFailure("test_Int07_01")

            m += 1

            # 结束循环

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
