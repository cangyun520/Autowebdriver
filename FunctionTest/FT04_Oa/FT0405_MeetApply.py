# -*- coding: utf-8 -*-
from PubliCode.onlineClass import *
from PubliCode.randData import *
'''
    *   Arvin
    *   2017-01-13
'''


class MeetApply(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "行政办公", "会议室管理", "会议室申请")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000800")

    # 行政办公-会议室管理-会议室申请添加
    def test_0405_01_add(self):
        """行政办公-会议室管理-会议室申请添加功能"""
        driver = self.driver
        driver.find_element_by_id("btnAdd").click()
        time.sleep(3)
        driver.switch_to.frame("winActivity_IFrame")        # 切换到新增页面
        v_tim = time.strftime("%y%m%d%H%M")
        # 会议主题
        driver.find_element_by_id("txtMeetingSubject").send_keys("会议室主题Auto" + v_tim)
        time.sleep(1)
        # 会议纪要员
        driver.find_element_by_id("txtSummarier").send_keys("会议纪要员：Anne童鞋")
        # 参会人员
        v_log_file = open(root_path() + 'PubliData/LogName.txt', 'r')
        for i in v_log_file:
            driver.find_element_by_id("trigfiJoinPerson").send_keys(i + ",")
        # 会议介绍
        driver.find_element_by_id("txtDescription").send_keys(
            "这是一场高级别互联网视频会议，这是测试说的Auto。申请日期：" + v_tim)
        # 调用自由流审批人选择函数
        ClasFlow.flow_free(self, "bear")
        driver.find_element_by_id("btnWorkflow").click()
        time.sleep(4)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "流程已触发" in i.text:
                print(i.text)
            elif "当前会议室在选择的起止时间中被申请" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/oa/test_0405_01_add.jpg")
                print("Error：" + i.text)
                unittest.expectedFailure("test_0405_01_add")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(MeetApply("test_0904_01_add"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)