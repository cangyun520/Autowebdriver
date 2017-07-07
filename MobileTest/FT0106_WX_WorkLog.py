# encoding:utf-8
from PubliCode.PubMobile import *
from PubliCode.config import *


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
        self.driver.find_element_by_name("工作日志").click()
        time.sleep(3)
        # 全局变量
        global v_time
        v_time = time.strftime("%Y-%m-%d %H:%M:%S")

    def test_0106_01_addDaily(self):
        """工作日志-我发出的-页面检查"""
        driver = self.driver

        driver.find_element_by_name("工作日志").click()
        timesl(1)
        driver.find_element_by_name("添加日志").click()
        timesl(1)
        driver.find_element_by_name("日报").click()
        timesl(5)
        # 上下滑动屏幕
        driver.swipe(0, 0, 0, 100)
        timesl(1)
        print(driver.contexts)

        driver.find_element_by_name("明日计划").click()
        v_edit = driver.find_elements_by_class_name("android.widget.EditText")
        # 今日完成
        print(len(v_edit))
        v_edit[0].click()
        timesl(3)
        v_edit[0].send_keys('Arvin-日报-微信端自动化测试 ' + v_time)
        # 明日计划
        v_edit[1].click()
        v_edit[1].send_keys(v_time + fun_data_character(10, 200))
        # 需协调工作
        v_edit[2].click()
        v_edit[2].send_keys(v_time + fun_data_character(100, 500))

        driver.find_element_by_accessibility_id("汇报人*").click()
        timesl(3)
        driver.find_element_by_accessibility_id("Bear-技术经理（微信）").click()
        driver.find_element_by_accessibility_id("确定 Link").click()
        timesl(2)

        driver.find_element_by_accessibility_id("添加 Link").click()
        timesl(3)

        try:
            driver.find_element_by_accessibility_id("工作日报添加成功！").is_displayed()
        except Exception as err:
            print(err)
            driver.get_screenshot_as_file(root_path() + "TestPicture/WeChat/test_0106_01_addDaily.jpg")
            unittest.expectedFailure("test_0106_01_addDaily")

    """工作日志-我发出的-页面检查"""

    def test_0106_01_check(self):
        """工作日志-我发出的-页面检查"""
        driver = self.driver

        driver.find_element_by_name("工作日报").click()
        timesl(1)
        driver.find_element_by_name("我发出的").click()
        timesl(5)



        try:
            driver.find_element_by_id("android:id/text1")
        except Exception as err:
            print(err)
            driver.get_screenshot_as_file(root_path() + "TestPicture/WeChat/test_0106_01_check.jpg")
            unittest.expectedFailure("test_0106_01_check")

    """工作日志-我发出的-客户管理添加"""
    def test_0101_02_CustomerAdd(self):
        """工作日志-我发出的-客户管理添加"""
        driver = self.driver

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
        driver.find_element_by_accessibility_id("电话").send_keys("027-" + str(random.randint(111111, 999999)))
        driver.find_element_by_accessibility_id("移动电话").send_keys(fun_data_mobile())
        driver.find_element_by_accessibility_id("传真").send_keys("027-" + str(random.randint(111111, 999999)))
        driver.find_element_by_accessibility_id("电子邮件").send_keys(fun_data_email())
        driver.find_element_by_accessibility_id("Web站点").send_keys(fun_data_www())
        # 上下滑动屏幕
        driver.swipe(0, 0, 0, 100)
        time.sleep(1)
        driver.find_element_by_accessibility_id("备注").send_keys("Python应用于微信端自动添加数据" + v_tim)

        driver.find_element_by_accessibility_id("添加 Link").click()
        time.sleep(8)

        # e 检测对象是否存在
        v_tip = "保存成功，单号：" + v_num
        try:
            driver.find_element_by_accessibility_id(v_tip).is_displayed()
            print(v_tip)
        except Exception as err:
            print(err)
            driver.get_screenshot_as_file(root_path() + "TestPicture/Ding/test_0101_02_CustomerAdd.jpg")
            unittest.expectedFailure("test_0101_02_Customer")


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
