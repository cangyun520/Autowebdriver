# -*- coding: utf-8 -*-
from PubliCode.config import *
from PubliCode.onlineClass import *
from PubliCode.randData import *


class LeaveApply(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self,"人事管理", "考勤管理", "单据管理", "请假申请")
        driver.switch_to.frame("frame_tab_PM000947")

    """人事管理-考勤管理-请假申请添加"""
    def test_0532_01_add(self):
        """人事管理-考勤管理-请假申请添加功能"""
        driver = self.driver
        driver.find_element_by_id("btnAdd").click()
        time.sleep(3)
        # 切换到新增页面
        driver.switch_to.frame("winActivity_IFrame")
        v_tim = time.strftime("%Y%m%d %H:%M")
        # 请假类型
        driver.find_element_by_xpath("//*[@id='AttendanceType_Container']/div/span").click()
        time.sleep(2)
        v_lxlist = driver.find_elements_by_class_name("x-tree-node")
        v_lxlist[random.randint(0, len(v_lxlist)-1)].click()
        driver.find_element_by_id("btnSaveOrg").click()
        time.sleep(1)
        # 请假原因
        driver.find_element_by_id("txtAttendanceRemark").send_keys(
            "世界那么大想出去走走，这是测试说的Auto。申请日期：" + v_tim)
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
                driver.get_screenshot_as_file(root_path() + "TestPicture/hr/test_0532_01_add.jpg")
                print("Error：" + i.text)
                unittest.expectedFailure("test_0532_01_add")

    """人事管理-考勤管理-请假申请草稿功能"""
    def test_0532_02(self):
        """人事管理-考勤管理-请假申请草稿功能"""
        driver = self.driver
        driver.find_element_by_id("btnAdd").click()
        time.sleep(3)
        driver.switch_to.frame("winActivity_IFrame")        # 切换到新增页面
        v_tim = time.strftime("%Y%m%d %H:%M")
        # 申请人员
        # driver.find_element_by_xpath("//*[@id='trigfiApplyPerson_Container']/div/span").click()
        # time.sleep(3)
        # driver.switch_to.frame("winEmployee_IFrame")
        # v_yhlist = driver.find_elements_by_class_name("x-grid3-row")
        # v_yhlist[random.randint(0,len(v_yhlist)-1)].click()
        # driver.find_element_by_id("btnSelect").click()
        # time.sleep(1)
        # driver.switch_to.parent_frame()
        # 请假类型
        driver.find_element_by_xpath("//*[@id='AttendanceType_Container']/div/span").click()
        time.sleep(2)
        v_lxlist = driver.find_elements_by_class_name("x-tree-node")
        v_lxlist[random.randint(0, len(v_lxlist)-1)].click()
        driver.find_element_by_id("btnSaveOrg").click()
        time.sleep(1)
        # 请假原因
        driver.find_element_by_id("txtAttendanceRemark").send_keys("世界那么大想出去走走，这是测试说的Auto。申请日期：" + v_tim)
        driver.find_element_by_id("btnSave").click()
        time.sleep(4)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/hr/test_0532_02.jpg")
                print("Error：" + i.text)
                unittest.expectedFailure("test_0532_02")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(LeaveApply("test_0904_01_add"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)