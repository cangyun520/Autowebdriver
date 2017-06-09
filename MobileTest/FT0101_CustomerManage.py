# encoding:utf-8
from PubliCode.config import *
from PubliCode.PubMobile import *
from PubliCode.randData import *
from appium import webdriver


class CustomerManage(unittest.TestCase):
    def setUp(self):
        # 调用钉钉初始化公共方法
        desired_caps = DingPublic.start_ding(self)
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(25)

    def test_0101_01_check(self):
        driver = self.driver
        # driver.find_element_by_name("联系人").click()
        try:
            driver.find_element_by_name("工作").click()
        except Exception as err:
            print(err)

        driver.find_element_by_name("业务管理首页").click()
        time.sleep(5)

        v_an = driver.find_elements_by_class_name("android.view.View")
        # for i in v_an:
        #     print(i.id)
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
        # driver.find_element_by_name("联系人").click()
        try:
            driver.find_element_by_name("工作").click()
        except Exception as err:
            print(err)
        driver.find_element_by_name("业务管理首页").click()
        time.sleep(5)
        v_an = driver.find_elements_by_class_name("android.view.View")
        v_an[3].click()
        time.sleep(3)
        driver.find_element_by_accessibility_id(" Link").click()

        # 进入添加页面

        driver.find_element_by_accessibility_id("代码*").click()
        driver.find_element_by_accessibility_id("代码*").send_keys(u"Python客户574975")
        driver.find_element_by_accessibility_id("名称").click()
        driver.find_element_by_accessibility_id("名称").send_keys(u"超级上市公司牛叉客户")
        driver.find_element_by_accessibility_id("外文名称").send_keys("gfiuuiguidgggdfgdg")
        driver.find_element_by_accessibility_id("移动电话").send_keys("15645678945")
        driver.find_element_by_accessibility_id("电话").send_keys("027-857463")
        driver.find_element_by_accessibility_id("传真").send_keys("027-857463")
        driver.find_element_by_accessibility_id("电子邮件").send_keys("15645678945@163.com")
        driver.find_element_by_accessibility_id("Web站点").send_keys("https://app.huoban.com")
        # 网上滑动屏幕
        driver.find_element_by_accessibility_id("备注").send_keys("027-857463")
        driver.find_element_by_accessibility_id("添加 Link").click()
        time.sleep(10)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

