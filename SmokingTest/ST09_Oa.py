# -*- coding: utf-8 -*-
from PubliCode.onlineClass import *

class OnlineSmoking(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)

    # # ------行政办公------新闻公告
    def test_0901_News_type(self):
        """行政办公-新闻公告类型-【新增】检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"行政办公", u"新闻公告", u"新闻公告类型")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000288")
        v_add = driver.find_element_by_xpath("//*[@id='form_wizard_1']/div[2]/div[1]/div/div[2]/a")
        try:
            v_add.is_displayed()
        except ImportError:
            print("BUG 行政办公-新闻公告-新闻公告类型-【新增】-不显示，请检查页面是否正常")
        else:
            print("行政办公-新闻公告-新闻公告类型-页面显示正常")

    def test_0902_News_manager(self):
        driver = self.driver
        ClasMenu.menu_full_text(self, u"行政办公", u"新闻公告", u"新闻公告管理")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000289")
        v_add = driver.find_element_by_xpath("//*[@id='form_wizard_1']/div[2]/div[1]/div/div[2]/a")
        try:
            v_add.is_displayed()
        except ImportError:
            print("BUG 行政办公-新闻公告-新闻公告管理-【新增】-不显示，请检查页面是否正常")
        else:
            print("行政办公-新闻公告-新闻公告管理-页面显示正常")

    def test_0907_Circular_OfficeSupplies(self):
        driver = self.driver
        ClasMenu.menu_full_text(self, u"行政办公", u"新闻公告", u"办公用品管理")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000796")
        v_add = driver.find_element_by_id("btnAdd")
        try:
            v_add.is_displayed()
        except ImportError:
            print("BUG 行政办公-办公用品管理-【添加】-不显示，请检查页面是否正常")
        else:
            print("行政办公-办公用品管理-页面显示正常")

    def test_0908_Circular_Book(self):
        """行政办公-图书管理-页面检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "行政办公", "图书管理")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000797")
        try:
            driver.find_element_by_id("btnAdd").is_displayed()
            print("行政办公-通知公告-图书管理-页面显示正常")
        except ImportError:
            print("BUG 行政办公-通知公告-图书管理-【添加】-不显示，请检查页面是否正常")
    # # ------行政办公------会议室管理

    def test_0909_Meeting_Archives(self):
        """行政办公-会议室档案-页面检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "行政办公", "会议室管理", "会议室档案")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000799")
        try:
            driver.find_element_by_id("btnAdd").is_displayed()
            print("会议室管理-会议室档案-页面显示OK")
        except ImportError:
            print("BUG 会议室管理-会议室档案-【添加】-不显示")

    def test_0910_Meeting_Apply(self):
        driver = self.driver
        ClasMenu.menu_full_text(self, u"行政办公", u"会议室管理", u"会议室申请")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000800")
        v_add = driver.find_element_by_id("btnAdd")
        try:
            v_add.is_displayed()
            print("行政办公-会议室管理-会议室申请-页面显示正常")
        except ImportError:
            print("BUG 行政办公-会议室管理-会议室申请-【添加】-不显示")
    # # ------行政办公------车辆管理

    def test_0911_Car_Archives(self):
        driver = self.driver
        ClasMenu.menu_full_text(self, u"行政办公", u"车辆管理", u"车辆档案")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000802")
        v_add = driver.find_element_by_id("btnAdd")
        try:
            v_add.is_displayed()
            print("行政办公-车辆管理-车辆档案-页面显示正常")
        except ImportError:
            print("BUG 行政办公-车辆管理-车辆档案-【添加】-不显示")

    def test_0912_Car_Apply(self):
        driver = self.driver
        ClasMenu.menu_full_text(self, u"行政办公", u"车辆管理", u"车辆申请")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000803")
        v_apply = driver.find_element_by_id("btnApply")
        try:
            v_apply.is_displayed()
            print("行政办公-车辆管理-车辆申请-页面显示正常")
        except ImportError:
            print("BUG 行政办公-车辆管理-车辆申请-【添加】-不显示")

    def test_0913_Car_Use(self):
        driver = self.driver
        ClasMenu.menu_full_text(self, u"行政办公", u"车辆管理", u"车辆使用查询")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000804")
        v_apply = driver.find_element_by_id("btnSearch")
        try:
            v_apply.is_displayed()
            print("行政办公-车辆管理-车辆使用查询-页面显示正常")
        except ImportError:
            print("BUG 行政办公-车辆管理-车辆使用查询-【查询】-不显示")

    def test_0914_Car_Promise(self):
        driver = self.driver
        ClasMenu.menu_full_text(self, u"行政办公", u"车辆管理", u"车辆预约情况")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000805")
        v_content = driver.find_element_by_id("ext-gen34")
        try:
            v_content.is_displayed()
            print("行政办公-车辆管理-车辆预约情况-页面显示正常")
        except ImportError:
            print("BUG 行政办公-车辆管理-车辆预约情况-‘红色：使用中’-不显示")
    # # ------行政办公------投票管理

    def test_0915_Vote_Create(self):
        """行政办公-投票管理-创建投票UI检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"行政办公", u"投票管理", u"创建投票")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000487")
        v_vote = driver.find_element_by_id("btnCreateVote")
        try:
            v_vote.is_displayed()
            print("行政办公-投票管理-创建投票-页面显示正常")
        except ImportError:
            print("BUG 行政办公-投票管理-创建投票-【创建投票】-不显示")

    def test_0916_Vote_List(self):
        driver = self.driver
        ClasMenu.menu_full_text(self, u"行政办公", u"投票管理", u"投票")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000481")
        v_query = driver.find_element_by_id("btnQuery")
        try:
            v_query.is_displayed()
            print("行政办公-投票管理-投票-页面显示正常")
        except ImportError:
            print("BUG 行政办公-投票管理-投票-【查询】-不显示")

    def test_0917_EaddressBook(self):
        driver = self.driver
        ClasMenu.menu_full_text(self, u"行政办公", u"企业通讯录")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000295")
        v_seach = driver.find_element_by_id("Button1")
        try:
            v_seach.is_displayed()
            print("行政办公-企业通讯录-页面显示正常")
        except ImportError:
            print("BUG 行政办公-企业通讯录-【查询】-不显示")

    def test_0918_UaddressBook(self):
        driver = self.driver
        ClasMenu.menu_full_text(self, u"行政办公", u"个人通讯录")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM001018")
        v_add = driver.find_element_by_id("btnNew")
        try:
            v_add.is_displayed()
            print("行政办公-个人通讯录-页面显示正常")
        except ImportError:
            print("BUG 行政办公-个人通讯录-【新增】-不显示")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(OnlineSmoking("test_0915_Vote_Create"))
    testsuit.addTest(OnlineSmoking("test_0916_Vote_List"))
    testsuit.addTest(OnlineSmoking("test_0917_EaddressBook"))
    testsuit.addTest(OnlineSmoking("test_0918_UaddressBook"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)