# -*- coding: utf-8 -*-
from PubliCode.onlineClass import *
from PubliCode.randData import *


class HomePage(unittest.TestCase):
    """登录后首页"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        # 打开登录页面
        ClasLogin.login_setup(self)

    # 首页-我的任务-新增
    def test_01_Task(self):
        """首页-我的任务-新增功能检查"""
        driver = self.driver
        v_time = time.strftime("%Y%m%d")
        driver.find_element_by_link_text(u"查看我的任务").click()
        time.sleep(3)
        driver.switch_to.frame("frame_tab_PM000789")
        driver.find_element_by_id("btnAdd").click()
        time.sleep(2)
        driver.switch_to.frame("winEdit_IFrame")     # 切换到新建页面
        # 任务内容
        driver.find_element_by_id("fieldTitle").send_keys("任务内容Auto" + v_time)
        driver.find_element_by_id("fieldTitle").send_keys(Keys.ENTER)
        # 备注
        driver.find_element_by_id("txtContent").send_keys(fun_data_character(500, 1000))
        # 负责人
        driver.find_element_by_xpath("//*[@id='Container3']/div[3]/div[1]/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winSelectUser_IFrame")      # 切换到用户选择窗体
        driver.find_element_by_id("gpReciver").click()
        v_user_list = driver.find_elements_by_class_name("x-grid3-row")
        v_user_list[random.randint(0, len(v_user_list) - 1)].click()
        driver.find_element_by_id("btnConfirm").click()
        time.sleep(1)
        driver.switch_to.parent_frame()
        # 参与人
        driver.find_element_by_xpath("//*[@id='x-form-el-fieldReciver']/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winSelectUser_IFrame")      # 切换到用户选择窗体
        driver.find_element_by_id("gpReciver").click()
        v_list = driver.find_elements_by_class_name("x-grid3-row")
        n = 1
        while n < len(v_list):
            v_list[n].click()
            n += 1
        time.sleep(1)
        driver.find_element_by_id("btnConfirm").click()
        time.sleep(1)
        driver.switch_to.parent_frame()
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 100)
        driver.find_element_by_id("btnEdit").click()
        time.sleep(2)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "添加成功" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/oa/test_01_Task.jpg")
                print(i.text)
                unittest.expectedFailure("test_01_Task")

    # 首页-工作汇报页面检查
    def test_02_work(self):
        """首页-工作汇报页面检查"""
        driver = self.driver
        driver.find_element_by_link_text(u"查看汇报给我的工作").click()
        time.sleep(3)
        driver.switch_to.frame("frame_tab_PM000483")
        # 清空
        driver.find_element_by_xpath(
            "//*[@id='tab3']/div[1]/div/div/div/div/form/div[2]/div/div[1]/div/div/button[1]"
        ).click()
        time.sleep(1)
        # 查询
        driver.find_element_by_xpath(
            "//*[@id='tab3']/div[1]/div/div/div/div/form/div[2]/div/div[1]/div/div/button[1]"
        ).click()
        time.sleep(2)

    # 首页-工作汇报页面检查
    def test_03_file(self):
        """首页-查看我的文件"""
        driver = self.driver
        driver.find_element_by_link_text(u"查看我的文件").click()
        time.sleep(3)
        driver.switch_to.frame("frame_tab_PM000815")
        driver.find_element_by_id("btnAddCategory").click()
        time.sleep(1)
        v_time = time.strftime("%Y%m%d")
        driver.find_element_by_id("txtCategoryName").send_keys(v_time)
        driver.find_element_by_id("Button1").click()
        time.sleep(2)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功" in i.text:
                print(i.text)
            elif "名称已存在" in i.text:
                print(i.text)
            else:
                print(i.text)
                unittest.expectedFailure("test_03_file")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # 模块被引入时，模块中的某一程序块不执行，可以用__name__属性来使该程序块仅在该模块自身运行时执行
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(HomePage("test_01_Task"))
    v_tim = time.strftime("%y%m%d%H%M")
    FileName = root_path() + 'TestReport/STRport/' + v_tim + ' ST01_HomePage.html'
    ReportFile = open(FileName, 'wb')
    runner = HTMLTestRunner(stream=ReportFile,
                            title="首页冒烟测试",
                            description="用例执行情况")
    # 运行测试用例集合
    runner.run(testsuit)
    ReportFile.close()
