# -*- coding: utf-8 -*-
from PubliCode.onlineClass import *
from PubliCode.randData import *


class NewsManage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "行政办公", "新闻公告", "新闻公告管理")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000289")

    """行政办公-通知公告-新闻公告管理-单据添加功能"""
    def test_0407_01_Add(self):
        """行政办公-通知公告-新闻公告管理-单据添加功能"""
        driver = self.driver
        driver.find_element_by_xpath("//*[@id='form_wizard_1']/div[2]/div[1]/div/div[2]/a").click()
        time.sleep(3)
        driver.switch_to.default_content()
        driver.switch_to.frame("frame_tab_PM000290")
        v_tim = time.strftime("%Y%m%d%H%M")
        driver.find_element_by_id("txt_title").send_keys("新闻公告(全体)Auto" + v_tim)
        time.sleep(1)
        # 内容
        driver.find_element_by_xpath("//*[@id='tab_Biz']/div/div[5]/div/div/div[2]/iframe").click()
        driver.switch_to.active_element.send_keys(fun_data_character(100, 1000))
        time.sleep(1)
        ClasFlow.flow_free_icon(self, "bear")
        driver.find_element_by_id("btnWorkflow").click()
        time.sleep(3)
        for i in driver.find_elements_by_class_name("bootbox-body"):
            try:
                "添加成功" in i.text
                print("行政办公-通知公告-新闻公告管理-单据添加成功")
            except ImportError:
                driver.get_screenshot_as_file(root_path() + "TestPicture/oa/test_050502_01_Add.jpg")
                print(i.text)
                unittest.expectedFailure("test_050502_01_Add")

    """行政办公-通知公告-新闻公告添加界面必填项校验"""
    def test_0407_02(self):
        """行政办公-通知公告-新闻公告添加界面必填项校验"""
        driver = self.driver
        driver.find_element_by_xpath("//*[@id='form_wizard_1']/div[2]/div[1]/div/div[2]/a").click()
        time.sleep(3)
        driver.switch_to.default_content()
        driver.execute_script("window.scrollTo(0,300)")
        driver.switch_to.frame("frame_tab_PM000290")
        time.sleep(1)
        driver.find_element_by_id("btnWorkflow").click()
        time.sleep(3)
        v_tip = driver.find_elements_by_class_name("bootbox-body")
        for i in v_tip:
            try:
                "请选择审批人" in i.text
                print(i.text)
            except ImportError:
                driver.get_screenshot_as_file(root_path() + "TestPicture/oa/test_0407_02.jpg")
                unittest.expectedFailure("test_0407_02")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(NewsManage("test_0407_01_Add"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)