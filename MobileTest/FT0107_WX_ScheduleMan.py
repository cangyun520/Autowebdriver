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
        self.driver.find_element_by_name("日程管理").click()
        timesl(3)
        # 全局变量
        global v_time
        v_time = time.strftime("%Y-%m-%d %H:%M:%S")

        """日程管理-我的日程"""

    """日程管理-我的日程-创建日程"""
    def test_0106_01_addDaily(self):
        """日程管理-我的日程"""
        driver = self.driver

        driver.find_element_by_name("我的日程").click()
        timesl(5)
        # 上下滑动屏幕
        driver.swipe(0, 0, 0, 1)
        driver.find_element_by_id("ajp").click()
        driver.find_element_by_accessibility_id("创建日程 Link").click()
        timesl(2)

        driver._switch_to.context("NATIVE_APP")
        win32api.keybd_event(9, 0, 0, 0)
        win32api.keybd_event(9, 0, win32con.KEYEVENTF_KEYUP, 0)
        driver.find_element_by_accessibility_id("标题").send_keys("常规日程" + v_time)
        win32api.keybd_event(9, 0, 0, 0)
        win32api.keybd_event(9, 0, win32con.KEYEVENTF_KEYUP, 0)
        driver.find_element_by_accessibility_id("地点").send_keys(fun_data_address())

        driver.find_element_by_accessibility_id("抄送").click()
        timesl(3)
        driver.find_element_by_id("ajp").click()
        driver.find_element_by_accessibility_id("Bear-技术经理（微信）").click()
        driver.find_element_by_accessibility_id("Sunny-技术总监").click()
        # 其中键盘输入，tab定位
        driver._switch_to.context("NATIVE_APP")
        win32api.keybd_event(9, 0, 0, 0)
        win32api.keybd_event(9, 0, win32con.KEYEVENTF_KEYUP, 0)
        win32api.keybd_event(13, 0, 0, 0)
        win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)
        timesl(2)

        driver.find_element_by_id("ajp").click()
        driver.find_element_by_accessibility_id("添加 Link").click()
        timesl(3)
        print(driver.contexts)
        # driver._switch_to.context("NATIVE_APP")
        driver.find_element_by_id("ajo").click()

        try:
            driver.find_element_by_accessibility_id("添加成功").is_displayed()
        except Exception as err:
            print(err)
            driver.get_screenshot_as_file(root_path() + "TestPicture/WeChat/test_0106_01_addDaily.jpg")
            unittest.expectedFailure("test_0106_01_addDaily")

    """日程管理-全部日程-页面检查"""
    def test_0106_03_analysis(self):
        """日程管理-全部日程-页面检查"""
        driver = self.driver

        driver.find_element_by_name("全部日程").click()
        timesl(5)
        try:
            driver.find_element_by_accessibility_id("未来五天").is_displayed()
        except Exception as err:
            print(err)
            driver.get_screenshot_as_file(root_path() + "TestPicture/WeChat/test_0106_03_check.jpg")
            unittest.expectedFailure("test_0106_03_check")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
