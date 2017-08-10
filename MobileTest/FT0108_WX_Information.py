# encoding:utf-8
from PubliCode.PubMobile import *
import win32api
import win32con


class WorkLog(unittest.TestCase):
    def setUp(self):
        # 调用微信初始化公共方法
        desired_caps = WeChatPublic.start_weixin(self)
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(25)

        try:
            self.driver.find_element_by_name("OnlineBox产品").click()
        except Exception as err:
            print(err)
        self.driver.find_element_by_name("信息中心").click()
        timesl(3)
        # 全局变量
        global v_time
        v_time = time.strftime("%Y-%m-%d %H:%M:%S")

        """信息中心-我的日程"""

    """信息中心-待办提醒-页面检查"""
    def test_0106_01_todocheck(self):
        """信息中心-代办提醒-页面检查"""
        driver = self.driver

        driver.find_element_by_name("待办提醒").click()
        timesl(5)
        try:
            driver.find_element_by_name("待办提醒").is_displayed()
        except Exception as err:
            print(err)
            driver.get_screenshot_as_file(root_path() + "TestPicture/WeChat/test_0106_01_todocheck.jpg")
            unittest.expectedFailure("test_0106_01_todocheck")

    """信息中心-新闻公告-页面检查"""
    def test_0106_02_newscheck(self):
        """信息中心-新闻公告-页面检查"""
        driver = self.driver

        driver.find_element_by_name("新闻公告").click()
        timesl(5)
        v_list = driver.find_element_by_class_name("android.widget.ListView")
        v_list.click()
        timesl(3)
        try:
            driver.find_element_by_accessibility_id("详情").is_displayed()
        except Exception as err:
            print(err)
            driver.get_screenshot_as_file(root_path() + "TestPicture/WeChat/test_0106_02_newscheck.jpg")
            unittest.expectedFailure("test_0106_02_newscheck")

    """信息中心-通知消息-页面检查"""
    def test_0106_03_notecheck(self):
        """信息中心-通知消息-页面检查"""
        driver = self.driver

        driver.find_element_by_name("通知消息").click()
        timesl(3)
        try:
            driver.find_element_by_id("text1").is_displayed()
        except Exception as err:
            print(err)
            driver.get_screenshot_as_file(root_path() + "TestPicture/WeChat/test_0106_03_notecheck.jpg")
            unittest.expectedFailure("test_0106_03_notecheck")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
