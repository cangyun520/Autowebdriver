# -*- coding: utf-8 -*-
from PubliCode.onlineClass import *
from PubliCode.randData import *


class Leave(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "人事管理", "员工异动", "离职")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000898")

    """人事管理-员工异动-离职"""
    def test_0507_01(self):
        """人事管理-员工异动-离职"""
        driver = self.driver
        driver.find_element_by_id("Button7").click()
        time.sleep(3)
        driver.switch_to.frame("winEdit_IFrame")        # 切换到新增页面
        # v_tim = time.strftime("%Y%m%d %H:%M")
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
            # 离职类型
            driver.find_element_by_id("cmbLeaveType").click()
            time.sleep(1)
            v_type = driver.find_elements_by_class_name("x-combo-list-item")
            v_type[random.randint(0, len(v_type)-1)].click()
            # 离职原因
            driver.find_element_by_id("cmbLeaveReason").click()
            time.sleep(1)
            v_reason = driver.find_elements_by_class_name("x-combo-list-item")
            v_reason[random.randint(len(v_type), len(v_reason)-1)].click()
            # 申请离职时间
            ClasForm.form_today(self, 'txtLeaveTime')
            # 详述
            driver.find_element_by_id("txtDetailed").send_keys(fun_data_character(400, 800))
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
                    driver.get_screenshot_as_file(root_path() + "TestPicture/hr/test_0507_01.jpg")
                    print("Error：" + i.text)
                    unittest.expectedFailure("test_0507_01")
        else:
            print("档案数据为空，不能添加")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(Leave.py("test_0507_01_add"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)