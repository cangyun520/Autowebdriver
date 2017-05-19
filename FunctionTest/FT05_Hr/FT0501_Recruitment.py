# -*- coding: utf-8 -*-
from PubliCode.onlineClass import *
from PubliCode.randData import *


class Recruitment(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self,"人事管理", "招聘管理", "招聘需求申请")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM001013")

    '''人事管理-招聘管理-招聘需求申请'''
    def test_0501_01(self):
        """人事管理-招聘管理-招聘需求申请"""
        driver = self.driver
        v_write_file = open(root_path() + 'PubliData/hr/zhaopin.txt', 'r')
        v_lines = v_write_file.read()
        # 现有需求岗位
        driver.find_element_by_id("trigWinJob").click()
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='gridJob']/tbody/tr[1]").click()
        driver.find_element_by_id("btnOK").click()
        time.sleep(1)
        # 需求人数
        driver.find_element_by_id("NeedNum").send_keys(random.randint(1, 10))
        time.sleep(1)
        # 需求类别
        driver.find_element_by_id("NeedType").click()
        time.sleep(1)
        driver.find_elements_by_tag_name("option")[random.randint(1, 8)].click()
        # 需求详情
        driver.find_element_by_id("NeedDetail").clear()
        driver.find_element_by_id("NeedDetail").send_keys(v_lines)
        # 新UI自由流审批人选择'
        ClasFlow.flow_free_icon(self, "bear")
        driver.find_element_by_id("btnWorkflow").click()
        time.sleep(3)
        v_tip = driver.find_elements_by_class_name("bootbox-body")
        for i in v_tip:
            if "保存单据成功" in i.text:
                print(i.text)
            elif "流程已触发" in i.text:
                print(i.text)
            elif "需求部门不能为空" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + 'TestPicture/oa/test_0501_01.jpg')
                print("Error：" + i.text)
                unittest.expectedFailure("test_0501_01")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(Recruitment("test_0501_01"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)