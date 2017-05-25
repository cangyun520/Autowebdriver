# encoding:utf-8
from PubliCode.config import *
from PubliCode.PubMobile import *
from appium import webdriver
import unittest


class CustomerManage(unittest.TestCase):
    def setUp(self):
        # 调用钉钉初始化公共方法
        desired_caps = Ding_StartOpen(self)
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test_0101_01_check(self):
        driver = self.driver
        driver.find_element_by_name("联系人").click()
        try:
            driver.find_element_by_name("钉钉测试").click()
        except Exception as err:
            print(err)

        driver.find_element_by_name("业务管理首页").click()
        time.sleep(3)

        v_an = driver.find_elements_by_class_name("android.view.View")
        for i in v_an:
            print(i.id)
        v_an[3].click()
        time.sleep(3)

        # 进入到客户管理页面
        try:
            driver.find_element_by_name("客户管理").is_displayed()

        except Exception as err:
            print(err)
            driver.get_screenshot_as_file(root_path() + "TestPicture/Ding/test_0101_01_check.jpg")
            unittest.expectedFailure("test_0101_01_check")

    def test_0101_02_check(self):
        driver = self.driver
        driver.find_element_by_name("联系人").click()
        try:
            driver.find_element_by_name("钉钉测试").click()
        except Exception as err:
            print(err)
        driver.find_element_by_name("业务管理首页").click()
        time.sleep(3)
        v_an = driver.find_elements_by_class_name("android.view.View")
        v_an[3].click()
        time.sleep(3)

        # UiObject obj = new UiObject(new UiSelector().className("android.widget.TextView").instance(1)); // textview1

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


