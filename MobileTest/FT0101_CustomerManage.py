# encoding:utf-8
from PubliCode.config import *
from appium import webdriver
import unittest


class CustomerManage(unittest.TestCase):
    def setUp(self):
        # 定义初始化的属性信息
        self.desired_caps = {}
        desired_caps = self.desired_caps
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.0'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['appPackage'] = 'com.alibaba.android.rimet'
        desired_caps['appActivity'] = '.biz.home.activity.HomeActivity'
        # self.desired_caps["unicodeKeyboard"] = "True"
        # self.desired_caps["resetKeyboard"] = "True"
        # self.desired_caps["automationName"] = "Selendroid"
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test_0101_01_check(self):
        driver = self.driver
        time.sleep(2)
        driver.find_element_by_name("钉钉测试").click()

        driver.find_element_by_name("业务管理首页").click()
        time.sleep(3)
        v_an = driver.find_elements_by_class_name("android.view.View")
        v_an[2].click()
        time.sleep(3)

        # 进入到客户管理页面
        try:
            driver.find_element_by_name("客户管理1").is_displayed()
        except Exception as err:
            print(err)
            driver.get_screenshot_as_file(root_path() + "TestPicture/Ding/test_0101_01_check.jpg")
            unittest.expectedFailure("test_0101_01_check")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


