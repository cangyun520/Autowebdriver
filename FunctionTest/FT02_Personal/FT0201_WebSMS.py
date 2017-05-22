
from PubliCode.onlineClass import *
from PubliCode.randData import *
import re
'''
    *   Arvin
    *   2017-01-13
'''


class WebSMS(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "事务处理", "消息中心")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 500)
        driver.switch_to.frame("frame_tab_PM000416")

    '''事务处理-站内短信'''
    def test_0201_01(self):
        """事务处理-站内短信,【发消息】按钮功能测试"""
        driver = self.driver
        driver.find_element_by_link_text("发消息").click()
        time.sleep(3)
        driver.switch_to.default_content()
        driver.switch_to.frame("frame_tab_PM001067")
        try:
            driver.find_element_by_id("btnsave").is_displayed()
            print("事务处理-消息中心,【发消息】跳转功能正常")
        except ImportError:
            print("BUG 事务处理-消息中心,【发消息】跳转页面错误")

    """事务处理-站内短信-站内短信发送"""
    def test_0201_02(self):
        """事务处理-站内短信发送"""
        driver = self.driver
        driver.find_element_by_link_text("发消息").click()
        time.sleep(3)
        driver.switch_to.default_content()
        driver.switch_to.frame("frame_tab_PM001067")
        v_tim = time.strftime("%Y-%m-%d %H:%M:%S")
        # 选择收件人
        driver.find_element_by_xpath(
            "//*[@id='ngSection']/div[1]/div/div/div/div/div/div[1]/div[1]/div/div/span/span[1]/span/ul"
        ).click()
        time.sleep(1)
        '''正则匹配数据'''
        for i in driver.find_elements_by_tag_name("li"):
            pa = re.compile(r"Arvin")
            match = pa.match(i.text)
            if match:
                i.click()
                break
        driver.find_element_by_id("txt_title").send_keys(v_tim + "消息标题Auto")
        time.sleep(1)
        v_content = "//*[@id='ngSection']/div[1]/div/div/div/div/div/div[1]/div[3]/div/div[2]/div[4]/div[3]"
        driver.find_element_by_xpath(v_content).send_keys(v_tim + fun_data_character(10, 200))
        time.sleep(2)
        driver.find_element_by_id("btnsave").click()
        time.sleep(3)
        ClasForm.form_top(self, 0)
        v_masg = driver.find_elements_by_class_name("bootbox-body")
        for i in v_masg:
            if "发送成功" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/oa/test_0201_02.jpg")
                print(i.text)
                unittest.expectedFailure("test_0201_02")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(WebSMS("test_0201_01"))
    testsuit.addTest(WebSMS("test_0201_02"))
    v_tim = time.strftime("%y%m%d%H%M")
    FileName = root_path() + 'TestReport/STRport/' + v_tim + ' ST01_Index.html'
    ReportFile = open(FileName, 'wb')
    runner = HTMLTestRunner(stream=ReportFile,
                            title="首页冒烟测试",
                            description="用例执行情况")
    # 运行测试用例集合
    runner.run(testsuit)
    ReportFile.close()
