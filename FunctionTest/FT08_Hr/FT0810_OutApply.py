# -*- coding: utf-8 -*-
from PubliCode.onlineClass import *
from PubliCode.randData import *


class OutApply(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "人事管理", "考勤管理", "单据管理", "外出申请")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000953")

    """人事管理-考勤管理-外出申请添加"""
    def test_0810_01(self):
        """人事管理-考勤管理-外出申请添加功能"""
        driver = self.driver
        driver.find_element_by_id("btnAdd").click()
        time.sleep(3)
        driver.switch_to_frame("winActivity_IFrame")        # 切换到新增页面
        v_tim = time.strftime("%Y%m%d %H:%M")
        # 申请人员
        driver.find_element_by_xpath("//*[@id='trigfiApplyPerson_Container']/div/span").click()
        time.sleep(3)
        driver.switch_to_frame("winEmployee_IFrame")
        v_yhlist = driver.find_elements_by_class_name("x-grid3-row")
        v_yhlist[random.randint(0, len(v_yhlist)-1)].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(1)
        driver.switch_to.parent_frame()
        # 外出原因
        driver.find_element_by_id("txtOutRemark").send_keys(
            "太饿了，只是想出去买个面包。这是测试说的Auto。申请日期：" + v_tim)
        time.sleep(1)
        # 结束时间
        driver.find_element_by_id("EndTime_H").click()
        time.sleep(1)
        v_endlist = driver.find_elements_by_class_name("x-combo-list-item")
        v_endlist[random.randint(1, len(v_endlist)-1)].click()
        time.sleep(1)
        # 自由流审批人选择
        ClasFlow.flow_free(self, "bear")
        driver.find_element_by_id("btnWorkflow").click()
        time.sleep(4)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "流程已触发" in i.text:
                print(i.text)
            elif "成功" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/hr/test_0810_01.jpg")
                print("Error：" + i.text)
                unittest.expectedFailure("test_0810_01")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(OutApply("test_0904_01_add"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)