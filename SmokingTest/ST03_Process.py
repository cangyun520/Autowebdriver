from PubliCode.webClass import *

class ST03_Process(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)

# # ------流程处理模块------
    def test_0301(self):
        """流程处理-待办工作-【查询】检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "流程处理", "待办工作")
        driver.switch_to_frame("frame_tab_PM000040")
        v_seach = driver.find_element_by_name("txtSearchWK")
        try:
            v_seach.is_displayed()
            print("待办工作-页面-显示正常")
        except ImportError:
            print("BUG 待办工作-【查询】-不显示")
            unittest.expectedFailure("test_0301")

    def test_0301_01(self):
        """流程处理-待办工作-查看流程图"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "流程处理", "待办工作")
        driver.switch_to_frame("frame_tab_PM000040")
        v_list = driver.find_elements_by_class_name("x-grid3-row")
        try:
            len(v_list) != 0
            v_list[random.randint(0,len(v_list)-1)].click()
            try:
                driver.find_element_by_id("btnView2").is_displayed()
                driver.find_element_by_id("btnView2").click()
                time.sleep(3)
                for i in driver.find_elements_by_class_name("x-window-header-text"):
                    if i.text == "流程进度跟踪":
                        print("流程进度跟踪,查看页面显示OK")
                        break
            except ImportError:
                print("自由流无法查看流程")
        except ImportError:
            pass
            print("待办工作列表无数据可操作")

    def test_0302(self):
        """流程处理-已办工作-【查询】检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "流程处理", "已办工作")
        driver.switch_to_frame("frame_tab_PM000031")
        v_Seach = driver.find_element_by_id("ext-gen57")
        try:
            v_Seach.is_displayed()
            print("已办工作-页面-显示正常")
        except ImportError:
            print("BUG 已办工作-【查询】-不显示")

    def test_0303(self):
        """流程处理-办结工作-【查询】检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "流程处理", "办结工作")
        driver.switch_to_frame("frame_tab_PM000032")
        v_seach = driver.find_element_by_id("ext-gen57")
        try:
            v_seach.is_displayed()
            print("办结工作-页面-显示正常")
        except ImportError:
            print("BUG 办结工作-【查询】-不显示")

    def test_0304(self):
        """流程处理-已委托工作-【查询】检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "流程处理", "委托工作", "已委托工作")
        driver.switch_to_frame("frame_tab_PM000089")
        v_listNo = driver.find_element_by_xpath("//*[@id='ext-gen25']/div/table/thead/tr/td[1]")
        try:
            v_listNo.is_displayed()
            print("已委托工作-页面-显示正常")
        except ImportError:
            print("BUG 已委托工作-【查询】-不显示")

    def test_0305(self):
        """流程处理-被委托工作-【查询】检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "流程处理", "委托工作", "被委托工作")
        driver.switch_to_frame("frame_tab_PM000090")
        v_ListNo = driver.find_element_by_xpath("//*[@id='ext-gen25']/div/table/thead/tr/td[1]")
        try:
            v_ListNo.is_displayed()
            print("被委托工作-页面-显示正常")
        except ImportError:
            print("BUG 被委托工作-【查询】-不显示")

    def test_0306(self):
        """流程处理-超时工作-【查询】检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "流程处理", "超时工作")
        driver.switch_to_frame("frame_tab_PM000318")
        v_Seach = driver.find_element_by_id("ext-gen57")
        try:
            v_Seach.is_displayed()
            print("超时工作-页面-显示正常")
        except ImportError:
            print("BUG 超时工作-【查询】-不显示")

    def test_0307(self):
        """流程处理-可参与项-【查询】检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "流程处理", "可参与项")
        driver.switch_to_frame("frame_tab_PM000034")
        v_ListNo = driver.find_element_by_xpath("//*[@id='ext-gen24']/div/table/thead/tr/td[1]")
        try:
            v_ListNo.is_displayed()
            print("可参与项-页面-显示正常")
        except ImportError:
            print("BUG 可参与项-【查询】-不显示")

    def test_0307_01(self):
        """流程处理-可参与项-查看流程图"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "流程处理", "可参与项")
        driver.switch_to_frame("frame_tab_PM000034")
        v_list = driver.find_elements_by_class_name("x-grid3-row")
        try:
            len(v_list) != 0
            v_list[random.randint(0, len(v_list)- 1)].click()
            driver.find_element_by_id("btnView2").click()
            time.sleep(3)
            for i in driver.find_elements_by_class_name("x-window-header-text"):
                if i.text == "流程参与环节":
                    print("可参与项,查看页面显示OK")
                    break
        except ImportError:
            pass
            print("可参与项，列表无数据可操作")

    def test_0308(self):
        """流程处理-流程进度跟踪-【查询】检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "流程处理", "流程进度跟踪")
        driver.switch_to_frame("frame_tab_PM000030")
        v_Seach = driver.find_element_by_id("ext-gen57")
        try:
            v_Seach.is_displayed()
            print("流程进度跟踪-页面-显示正常")
        except ImportError:
            print("BUG 流程进度跟踪-【查询】-不显示")

    def test_0308_01(self):
        """流程处理-待办工作-查看流程进度跟踪"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "流程处理", "流程进度跟踪")
        driver.switch_to_frame("frame_tab_PM000030")
        v_list = driver.find_elements_by_class_name("x-grid3-row")
        try:
            len(v_list) != 0
            v_list[random.randint(0,len(v_list)-1)].click()
            try:
                driver.find_element_by_id("btnView2").is_displayed()
                driver.find_element_by_id("btnView2").click()
                time.sleep(3)
                for i in driver.find_elements_by_class_name("x-window-header-text"):
                    if i.text == "流程进度跟踪":
                        print("流程进度跟踪,查看页面显示OK")
                        break
            except ImportError:
                print("自由流无法查看流程")
        except ImportError:
            pass
            print("流程进度跟踪，列表无数据可操作")

    def test_0309(self):
        """流程处理-流程监控-【查询】检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "流程处理", "流程监控")
        driver.switch_to_frame("frame_tab_PM000028")
        v_Seach = driver.find_element_by_id("ext-gen52")
        try:
            v_Seach.is_displayed()
        except ImportError:
            print("BUG 流程监控-【查询】-不显示")
        else:
            print("流程监控-页面-显示正常")

    def test_0309_01(self):
        """流程处理-待办工作-查看流程进度跟踪"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "流程处理", "流程监控")
        driver.switch_to_frame("frame_tab_PM000028")
        v_list = driver.find_elements_by_class_name("x-grid3-row")
        try:
            len(v_list) != 0
            v_list[random.randint(0,len(v_list)-1)].click()
            try:
                driver.find_element_by_id("btnView2").is_displayed()
                driver.find_element_by_id("btnView2").click()
                time.sleep(3)
                for i in driver.find_elements_by_class_name("x-window-header-text"):
                    if i.text == "流程监控":
                        print("流程监控,查看页面显示OK")
                        break
            except ImportError:
                print("自由流无法查看流程")
        except ImportError:
            pass
            print("流程监控，列表无数据可操作")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(ST03_Process("test_0301"))
    testsuit.addTest(ST03_Process("test_0302"))
    testsuit.addTest(ST03_Process("test_0303"))
    testsuit.addTest(ST03_Process("test_0304"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)