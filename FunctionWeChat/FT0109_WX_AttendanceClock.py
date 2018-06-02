# encoding:utf-8
from PubliCode.dingTalkClass import *


class AttendanceClock(unittest.TestCase):
    def setUp(self):
        # 调用微信初始化公共方法
        desired_caps = WeChatPublic.start_weixin(self)
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(25)

        try:
            self.driver.find_element_by_name("OnlineBox产品").click()
        except Exception as err:
            print(err)
        self.driver.find_element_by_name("考勤打卡").click()
        timesl(3)
        # 全局变量
        global v_tim
        v_tim = time.strftime("%Y-%m-%d %H:%M:%S")

    """考勤打卡-提醒设置-页面检查"""
    def test_0109_01_remindcheck(self):
        """考勤打卡-提醒设置-页面检查"""
        driver = self.driver

        driver.find_element_by_name("内勤").click()
        driver.find_element_by_name("提醒设置").click()
        timesl(5)
        try:
            driver.find_element_by_name("提醒设置").is_displayed()
        except Exception as err:
            print(err)
            driver.get_screenshot_as_file(root_path() + "TestPicture/WeChat/test_0109_01_remindcheck.jpg")
            unittest.expectedFailure("test_0109_01_remindcheck")

    """考勤打卡-签到-页面检查"""
    def test_0109_02_signInCheck(self):
        """考勤打卡-签到-页面检查"""
        driver = self.driver

        driver.find_element_by_name("内勤").click()
        driver.find_element_by_name("签到").click()
        timesl(5)
        try:
            driver.find_element_by_name("签到").is_displayed()
        except Exception as err:
            print(err)
            driver.get_screenshot_as_file(root_path() + "TestPicture/WeChat/test_0109_02_signInCheck.jpg")
            unittest.expectedFailure("test_0109_02_signInCheck")

    """考勤打卡-签退-页面检查"""
    def test_0109_03_signOutCheck(self):
        """考勤打卡-签退-页面检查"""
        driver = self.driver

        driver.find_element_by_name("内勤").click()
        driver.find_element_by_name("签退").click()
        timesl(5)
        try:
            driver.find_element_by_name("签退").is_displayed()
        except Exception as err:
            print(err)
            driver.get_screenshot_as_file(root_path() + "TestPicture/WeChat/test_0109_03_signOutCheck.jpg")
            unittest.expectedFailure("test_0109_03_signOutCheck")

    """考勤打卡-外勤-添加"""
    def test_0109_04_fieldAdd(self):
        """考勤打卡-外勤-添加"""
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
            driver.get_screenshot_as_file(root_path() + "TestPicture/WeChat/test_0109_04_fieldAdd.jpg")
            unittest.expectedFailure("test_0109_04_fieldAdd")

    """考勤打卡-打卡记录-页面检查"""
    def test_0109_05_recordCheck(self):
        """考勤打卡-打卡记录-页面检查"""
        driver = self.driver

        driver.find_element_by_name("打卡记录").click()
        timesl(5)
        try:
            driver.find_element_by_name("打卡记录").is_displayed()
        except Exception as err:
            print(err)
            driver.get_screenshot_as_file(root_path() + "TestPicture/WeChat/test_0109_05_recordCheck.jpg")
            unittest.expectedFailure("test_0109_05_recordCheck")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
