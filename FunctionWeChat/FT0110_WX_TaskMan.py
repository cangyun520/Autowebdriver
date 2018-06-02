# encoding:utf-8
from PubliCode.dingTalkClass import *


class TaskMan(unittest.TestCase):
    def setUp(self):
        # 调用微信初始化公共方法
        desired_caps = WeChatPublic.start_weixin(self)
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(25)

        try:
            self.driver.find_element_by_name("OnlineBox产品").click()
        except Exception as err:
            print(err)
        self.driver.find_element_by_name("任务管理").click()
        timesl(3)
        # if self.driver.find_element_by_accessibility_id("提示").is_displayed():
        #     self.driver.find_element_by_accessibility_id("确定").click()
        # else:
        #     pass
        # 全局变量
        global v_tim
        v_tim = time.strftime("%Y-%m-%d %H:%M:%S")

    """任务管理-我的任务-添加"""
    def test_0110_01_remindAdd(self):
        """任务管理-我的任务-添加"""
        driver = self.driver

        driver.find_element_by_name("我的任务").click()
        timesl(5)
        # driver.find_element_by_id("ajp").click()
        driver.find_element_by_accessibility_id("我的任务").click()
        driver.find_element_by_accessibility_id("创建任务 Link").click()
        timesl(2)

        # 任务内容
        driver.find_element_by_accessibility_id("任务内容").click()
        driver.find_element_by_accessibility_id("任务内容").send_keys(v_tim + "任务")
        driver.find_element_by_accessibility_id("负责人").click()
        timesl(1)
        driver.find_element_by_accessibility_id("Aaron-采购经理").click()
        timesl(1)
        v_edit = driver.find_elements_by_class_name("android.widget.EditText")
        v_edit[1].click()
        v_edit[1].send_keys(v_tim + fun_data_character(100, 150))
        driver.find_element_by_accessibility_id("添加 Link").click()
        timesl(2)

        try:
            driver.find_element_by_accessibility_id("工作任务添加成功！").is_displayed()
        except Exception as err:
            print(err)
            driver.get_screenshot_as_file(root_path() + "TestPicture/WeChat/test_0110_01_remindAdd.jpg")
            unittest.expectedFailure("test_0110_01_remindAdd")

    """任务管理-签到-添加"""
    def test_0110_02_signInCheck(self):
        """任务管理-签到-添加"""
        driver = self.driver

        driver.find_element_by_name("内勤").click()
        driver.find_element_by_name("签到").click()
        timesl(5)
        try:
            driver.find_element_by_name("签到").is_displayed()
        except Exception as err:
            print(err)
            driver.get_screenshot_as_file(root_path() + "TestPicture/WeChat/test_0110_02_signInCheck.jpg")
            unittest.expectedFailure("test_0110_02_signInCheck")

    """任务管理-签退-添加"""
    def test_0110_03_signOutCheck(self):
        """任务管理-签退-添加"""
        driver = self.driver

        driver.find_element_by_name("内勤").click()
        driver.find_element_by_name("签退").click()
        timesl(5)
        try:
            driver.find_element_by_name("签退").is_displayed()
        except Exception as err:
            print(err)
            driver.get_screenshot_as_file(root_path() + "TestPicture/WeChat/test_0110_03_signOutCheck.jpg")
            unittest.expectedFailure("test_0110_03_signOutCheck")

    def test_0110_04_fieldAdd(self):
        """任务管理-外勤-添加"""
        driver = self.driver

        driver.find_element_by_name("外勤").click()
        timesl(5)
        driver.find_element_by_accessibility_id("外勤签到").click()
        v_edit = driver.find_element_by_class_name("android.widget.EditText")
        v_edit.click()
        v_edit.send_keys(v_tim + fun_data_character(50, 100))

        driver.find_element_by_accessibility_id("选择文件").click()
        timesl(1)
        driver.find_element_by_name("文档").click()
        timesl(1)
        driver.find_element_by_name("图库").click()
        timesl(1)
        driver.find_element_by_id("content").click()
        timesl(1)
        driver.find_element_by_accessibility_id("签到 Link").click()

        try:
            driver.find_element_by_accessibility_id("签到成功！").is_displayed()
        except Exception as err:
            print(err)
            driver.get_screenshot_as_file(root_path() + "TestPicture/WeChat/test_0110_04_fieldAdd.jpg")
            unittest.expectedFailure("test_0110_04_fieldAdd")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
