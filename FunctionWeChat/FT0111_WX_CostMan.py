# encoding:utf-8
from PubliCode.dingTalkClass import *


class CostMan(unittest.TestCase):
    def setUp(self):
        # 调用微信初始化公共方法
        desired_caps = WeChatPublic.start_weixin(self)
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(25)

        try:
            self.driver.find_element_by_name("OnlineBox产品").click()
        except Exception as err:
            print(err)
        self.driver.find_element_by_name("费用管理").click()
        timesl(3)
        # 全局变量
        global v_tim
        v_tim = time.strftime("%Y-%m-%d %H:%M:%S")

    """费用管理-页面检查"""
    def test_0110_01_mainCheck(self):
        """费用管理-页面检查"""
        driver = self.driver
        try:
            driver.find_element_by_name("云报销").is_displayed()
        except Exception as err:
            print(err)
            driver.get_screenshot_as_file(root_path() + "TestPicture/WeChat/test_0110_01_mainCheck.jpg")
            unittest.expectedFailure("test_0110_01_mainCheck")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
