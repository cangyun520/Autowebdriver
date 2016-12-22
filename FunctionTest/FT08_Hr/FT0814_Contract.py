# -*- coding: utf-8 -*-
from PubliCode.onlineClass import *
from PubliCode.randData import *
import datetime


class ReleaseTrain(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self,"人事管理", "员工合同", "合同管理")
        # 移动到页面顶部，防止对象遮挡
        time.sleep(3)
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000939")

    """人事管理-员工合同-合同管理"""
    def test_0814_01(self):
        """人事管理-员工合同-合同管理"""
        driver = self.driver
        v_tim = time.strftime("%Y%m%d %H:%M")
        driver.find_element_by_id("btnSign").click()
        time.sleep(3)
        driver.switch_to.parent_frame()
        driver.switch_to_frame("frame_tab_PM000940")
        # 档案编号
        driver.find_element_by_xpath("//*[@id='txtEmployeeID_Container']/div/span").click()
        time.sleep(2)
        v_list = driver.find_elements_by_class_name("x-grid3-row")
        v_list[random.randint(0, len(v_list)-1)].click()
        driver.find_element_by_id("Button4").click()
        time.sleep(1)
        # 合同类型
        driver.find_element_by_id("txtContractType").click()
        v_list_type = driver.find_elements_by_class_name("x-combo-list-item")
        v_list_type[random.randint(0, len(v_list_type)-1)].click()
        # 合同期限类型
        driver.find_element_by_id("txtContractlimitType").click()
        v_list_litype = driver.find_elements_by_class_name("x-combo-list-item")
        v_list_litype[random.randint(len(v_list_type), len(v_list_litype)-1)].click()
        # 合同状态
        driver.find_element_by_id("txtContractStatus").click()
        v_list_statu = driver.find_elements_by_class_name("x-combo-list-item")
        for i in v_list_statu:
            if i.text == "新签":
                i.click()
                break
        # 合同起始日期
        ClasForm.form_today(self, "txtStartTime")
        # 合同结束日期
        ClasForm.form_today_next(self, 2, "txtEndTime", 20, 20)         # 第2个时间控件，下20个月的20号
        # 到期提醒日期
        ClasForm.form_today_next(self, 3, "txtRemindTime", 18, 20)      # 第3个时间控件，下18个月的20号
        # 备注
        driver.find_element_by_id("txtNote").send_keys(fun_data_character(50, 200))
        # 自由流程审批
        ClasFlow.flow_free(self, "bear")
        driver.find_element_by_id("btnWorkflow").click()
        time.sleep(3)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "发布成功" in i.text:
                print(i.text)
            elif "流程已触发" in i.text:
                print(i.text)
            elif "存在合同编号" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + 'TestPicture/hr/test_0814_01.jpg')
                print("Error：" + i.text)
                unittest.expectedFailure("test_0814_01")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(ReleaseTrain("test_0814_01"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)