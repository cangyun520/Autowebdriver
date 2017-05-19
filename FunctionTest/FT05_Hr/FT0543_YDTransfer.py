# -*- coding: utf-8 -*-
from PubliCode.onlineClass import *
from PubliCode.randData import *


class Transfer(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "人事管理", "员工异动", "调动")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000894")

    """人事管理-员工异动-调动"""
    def test_0506_01(self):
        """人事管理-员工异动-调动"""
        driver = self.driver
        driver.find_element_by_id("btnEdit").click()
        time.sleep(3)
        driver.switch_to.frame("winEdit_IFrame")        # 切换到新增页面
        # 员工姓名
        driver.find_element_by_xpath("//*[@id='txtEmployeeName_Container']/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winItem_IFrame")
        v_yhlist = driver.find_elements_by_class_name("x-grid3-row")
        if len(v_yhlist) > 0:
            v_yhlist[random.randint(0, len(v_yhlist)-1)].click()
            driver.find_element_by_id("btnSelect").click()
            time.sleep(1)
            driver.switch_to.parent_frame()
            # 调动后部门
            driver.find_element_by_xpath("//*[@id='hidOrgNameAfter_Container']/div/span").click()
            time.sleep(3)
            driver.switch_to.frame("winItem_IFrame")
            v_yhlist = driver.find_elements_by_class_name("x-grid3-row")
            v_yhlist[random.randint(0, len(v_yhlist)-1)].click()
            driver.find_element_by_id("btnSelect").click()
            time.sleep(1)
            driver.switch_to.parent_frame()
            # 调动后岗位
            driver.find_element_by_xpath("//*[@id='txtAfterJobs_Container']/div/span").click()
            time.sleep(3)
            driver.switch_to.frame("winItem_IFrame")
            v_yhlist = driver.find_elements_by_class_name("x-grid3-row")
            v_yhlist[random.randint(0, len(v_yhlist)-1)].click()
            driver.find_element_by_id("btnSelect").click()
            time.sleep(1)
            driver.switch_to.parent_frame()
            # 调动生效日期
            ClasForm.form_today(self, "txtTransferDate")
            # 转岗类型
            driver.find_element_by_id("cmbTransferType").click()
            driver.find_elements_by_class_name("x-combo-list-item")[random.randint(1, 2)].click()
            # 原因
            driver.find_element_by_id("txtTransferReason").send_keys(fun_data_character(200, 400))
            # 自由流审批人选择
            ClasFlow.flow_free(self, "bear")
            driver.find_element_by_id("btnWorkflow").click()
            time.sleep(4)
            v_tip = driver.find_elements_by_class_name("ext-mb-text")
            for i in v_tip:
                if "流程已触发" in i.text:
                    print(i.text)
                elif "保存单据成功" in i.text:
                    print(i.text)
                else:
                    unittest.expectedFailure("test_0506_01")
                    driver.get_screenshot_as_file(root_path() + "TestPicture/hr/test_0506_01.jpg")
                    print("Error：" + i.text)
        else:
            print("档案数据为空，不能添加")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(Transfer.py("test_0506_01_add"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)