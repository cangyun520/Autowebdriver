# -*- coding: utf-8 -*-
from PubliCode.config import *
from PubliCode.onlineClass import *
from PubliCode.randData import *


class OvertimeApply(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "人事管理", "考勤管理", "单据管理", "加班申请")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000949")

    """人事管理-考勤管理-加班申请添加"""
    def test_0535_01(self):
        """人事管理-考勤管理-加班申请添加功能"""
        driver = self.driver
        driver.find_element_by_id("btnAdd").click()
        time.sleep(3)
        driver.switch_to.frame("winActivity_IFrame")        # 切换到新增页面
        v_tim = time.strftime("%Y%m%d %H:%M")
        # 加班原因
        driver.find_element_by_id("txtOvertimeRemark").send_keys(
            "BT客户又变需求了，赶进度赶进度赶进度。这是测试说的Auto。申请日期：" + v_tim)
        time.sleep(1)
        # 结束时间
        driver.find_element_by_id("EndTime_H").click()
        time.sleep(1)
        v_endlist = driver.find_elements_by_class_name("x-combo-list-item")
        v_endlist[random.randint(1, len(v_endlist)-1)].click()
        time.sleep(1)
        # 加班类型
        driver.find_element_by_id("cmbOvertimeType").click()
        time.sleep(1)
        driver.find_element_by_id("cmbOvertimeType_SelIndex")
        time.sleep(1)
        # 补偿方式
        driver.find_element_by_id("cmbCompensationType").click()
        time.sleep(1)
        random.choice([driver.find_elements_by_class_name("x-combo-list-item")])
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
            elif "开始时间不能超过" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/hr/test_0535_01.jpg")
                print(i.text)
                unittest.expectedFailure("test_0535_01")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    unittest.main()
