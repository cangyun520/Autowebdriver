# encoding:utf-8
import time
from appium import webdriver
import unittest


class MyTestCase(unittest.TestCase):
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


    def testFindElements(self):
        driver = self.driver
        time.sleep(3)
        driver.find_element_by_name("钉钉测试").click()
        driver.find_element_by_name("业务管理首页").click()
        time.sleep(5)
        driver.find_element_by_name(" 客户管理 Link").click()

        time.sleep(4)
        v_an = driver.find_elements_by_class_name("android.view.View")
        for i in v_an:
            print(i.text)




    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


