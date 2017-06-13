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

    def test_0101_02_add(self):
        driver = self.driver
        # driver.find_element_by_name("联系人").click()
        try:
            driver.find_element_by_name("工作").click()
        except Exception as err:
            print(err)
        driver.find_element_by_name("业务管理首页").click()
        time.sleep(5)
        v_tim = time.strftime("%y%m%d%H%M%S")
        v_an = driver.find_elements_by_class_name("android.view.View")
        v_an[3].click()
        time.sleep(3)
        driver.find_element_by_accessibility_id(" Link").click()

        # 进入添加页面

        driver.find_element_by_accessibility_id("代码*").click()
        v_num = "KHDD" + str(random.randint(11111, 99999))
        driver.find_element_by_accessibility_id("代码*").send_keys(v_num)
        driver.find_element_by_accessibility_id("名称").click()
        driver.find_element_by_accessibility_id("名称").send_keys("客户DD" + v_tim + "有限公司")
        driver.find_element_by_accessibility_id("外文名称").send_keys(fun_data_englishname())
        driver.find_element_by_accessibility_id("移动电话").send_keys(fun_data_mobile())
        driver.find_element_by_accessibility_id("电话").send_keys("027-" + str(random.randint(111111, 999999)))
        driver.find_element_by_accessibility_id("传真").send_keys("027-" + str(random.randint(111111, 999999)))
        driver.find_element_by_accessibility_id("电子邮件").send_keys(fun_data_email())
        driver.find_element_by_accessibility_id("Web站点").send_keys(fun_data_www())
        # 上下滑动屏幕
        driver.swipe(0, 0, 0, 100)
        time.sleep(1)
        driver.find_element_by_accessibility_id("备注").send_keys("Python应用于钉钉端自动添加数据" + v_tim)
        driver.find_element_by_accessibility_id("添加 Link").click()
        time.sleep(12)

        # e 检测对象是否存在
        v_tip = "保存成功，单号：" + v_num
        try:
            driver.find_element_by_accessibility_id(v_tip).is_displayed()
            print(v_tip)
        except Exception as err:
            print(err)
            driver.get_screenshot_as_file(root_path() + "TestPicture/Ding/test_0101_02_add.jpg")
            unittest.expectedFailure("test_0101_02_add")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

