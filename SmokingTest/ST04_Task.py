# -*- coding: utf-8 -*-
from PubliCode.webClass import *

class ST04_Task(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)

# ------任务协作模块------
    def test_0401(self):
        """任务协作-日程管理-【查询】检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "任务协作", "日程管理")
        driver.switch_to_frame("frame_tab_PM000794")
        v_seach = driver.find_element_by_id("ext-gen25")
        try:
            v_seach.is_displayed()
            print("日程管理-页面-显示正常")
        except ImportError:
            print("BUG 日程管理-【查询】-不显示")
            unittest.expectedFailure("test_0401")

    def test_0402(self):
        """任务协作-工作任务-【查询】检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "任务协作", "工作任务")
        driver.switch_to_frame("frame_tab_PM000795")
        v_seach = driver.find_element_by_id("btnSelect")
        try:
            v_seach.is_displayed()
        except ImportError:
            print("BUG 工作任务-【查询】-不显示，工作任务")
        else:
            print("工作任务-页面-显示正常")

    def test_0402_01(self):
        """任务协作-工作任务-查看任务详细"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "任务协作", "工作任务")
        driver.switch_to_frame("frame_tab_PM000795")
        v_list = driver.find_elements_by_class_name("x-grid3-row")
        try:
            len(v_list) != 0
            v_list[random.randint(0, len(v_list)-1)].click()
            driver.find_element_by_id("btnLook").click()
            time.sleep(3)
            for i in driver.find_elements_by_class_name("x-window-header-text"):
                if i.text == "查看任务":
                    print("工作任务,查看任务页面显示OK")
                    break
        except ImportError:
            pass
            print("工作任务，列表无数据可操作")

    def test_0402_02(self):
        """任务协作-工作任务-【日历视图】检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "任务协作", "工作任务")
        driver.switch_to_frame("frame_tab_PM000795")
        driver.find_element_by_id("Button1").click()
        time.sleep(3)
        try:
            driver.find_element_by_id("calendar").is_displayed()
            print("工作任务-日历视图页面-显示OK")
        except ImportError:
            print("BUG 工作任务-日历视图页面-显示错误")

    def test_0403(self):
        """任务协作-日志填报-【发日志】检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "任务协作", "工作日志", "日志填报")
        driver.switch_to_frame("frame_tab_PM000483")
        v_sendLog  = driver.find_element_by_link_text("发日志")
        v_daily = driver.find_element_by_link_text("日报")
        try:
            v_daily.is_displayed()
        except ImportError:
            print("BUG 日志填报-发日志-不显示")
        else:
            print("日志填报-页面-显示正常")

    def test_0404(self):
        """任务协作-日志报表-【查询】检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "任务协作", "工作日志", "日志报表")
        driver.switch_to_frame("frame_tab_PM000489")
        v_daily = driver.find_element_by_link_text("日报")
        try:
            v_daily.is_displayed()
        except ImportError:
            print("BUG 日志报表-日报-不显示")
        else:
            print("日志报表-页面-显示正常")

    def test_0405(self):
        """任务协作-日报分析-【查询】检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "任务协作", "工作日志", "日报分析")
        driver.switch_to_frame("frame_tab_PM000989")
        v_yesterday = driver.find_element_by_id("btnYesterday")
        try:
            v_yesterday.is_displayed()
        except ImportError:
            print("BUG 日报分析-昨-不显示")
        else:
            print("日报分析-页面-显示正常")

    def test_0406(self):
        """任务协作-外勤轨迹-【列表查询】检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "任务协作", "外勤管理", "外勤轨迹")
        driver.switch_to_frame("frame_tab_PM000825")
        v_listSeach = driver.find_element_by_id("ext-gen60")
        try:
            v_listSeach.is_displayed()
        except ImportError:
            print("BUG 外勤轨迹-【列表查询】-不显示")
        else:
            print("外勤轨迹-列表查询页面-显示正常")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(ST04_Task("test_0401"))
    testsuit.addTest(ST04_Task("test_0402"))
    testsuit.addTest(ST04_Task("test_0403"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)