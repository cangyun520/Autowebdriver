
from PubliCode.onlineClass import *

class ST11_Report(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)

# # ------报表平台------
    def test_1101_Manage(self):
        """报表平台-报表管理-【上传】检查"""
        driver = self.driver
        driver.find_element_by_link_text(u"报表平台").click()
        time.sleep(2)
        # 移动到页面底部，防止对象遮挡
        js_down = "window.scrollTo(0,500)"
        driver.execute_script(js_down)
        driver.find_element_by_link_text(u"报表管理").click()
        time.sleep(2)
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000016")
        v_expand = driver.find_element_by_id("btnExpand")
        try:
            v_expand.is_displayed()
        except ImportError:
            print("BUG 报表平台-报表管理-【上传】-不显示")
        else:
            print("报表平台-报表管理-页面显示正常")

    def test_1102_Collect(self):
        """报表平台-我的收藏报表-【上传】检查"""
        driver = self.driver
        driver.find_element_by_link_text(u"报表平台").click()
        time.sleep(2)
        # 移动到页面底部，防止对象遮挡
        js_down = "window.scrollTo(0,500)"
        driver.execute_script(js_down)
        driver.find_element_by_link_text(u"我的收藏报表").click()
        time.sleep(2)
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)

        driver.switch_to_frame("frame_tab_PM000014")
        v_expand = driver.find_element_by_id("btnExpand")
        try:
            v_expand.is_displayed()
        except ImportError:
            print("BUG 报表平台-我的收藏报表-【上传】-不显示")
        else:
            print("报表平台-我的收藏报表-页面显示正常")
# # ------系统管理------报表&打印------

    def test_1103_Design(self):
        """报表平台-查询管理器-【B1导入】检查"""
        driver = self.driver
        driver.find_element_by_link_text(u"系统管理").click()
        time.sleep(2)
        # 移动到页面底部，防止对象遮挡
        js_down = "window.scrollTo(0,500)"
        driver.execute_script(js_down)
        driver.find_element_by_link_text(u"报表&打印").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"报表设计").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"查询管理器").click()
        time.sleep(2)
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)

        driver.switch_to_frame("frame_tab_PM000176")
        v_import = driver.find_element_by_id("btnImport")
        try:
            v_import.is_displayed()
            print("系统管理-报表&打印-查询管理器-页面显示正常")
        except ImportError:
            print("BUG 报表&打印-查询管理器-【B1导入】-不显示")

    def test_1104_H5Design(self):
        """报表平台-Html5设计器-【查询】检查"""
        driver = self.driver
        driver.find_element_by_link_text(u"系统管理").click()
        time.sleep(2)
        # 移动到页面底部，防止对象遮挡
        js_down = "window.scrollTo(0,500)"
        driver.execute_script(js_down)
        driver.find_element_by_link_text(u"报表&打印").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"报表设计").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"Html5报表设计器").click()
        time.sleep(2)
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)

        driver.switch_to_frame("frame_tab_PM000656")
        v_carriedOut = driver.find_element_by_id("btnCarriedOut")
        try:
            v_carriedOut.is_displayed()
            print("系统管理-报表&打印-Html5报表设计器-页面显示正常")
        except ImportError:
            print("BUG 报表&打印-Html5报表设计器-【查询】-不显示")

    def test_1105_Release(self):
        """报表平台-报表发布-【查询】检查"""
        driver = self.driver
        driver.find_element_by_link_text(u"系统管理").click()
        time.sleep(2)
        # 移动到页面底部，防止对象遮挡
        js_down = "window.scrollTo(0,500)"
        driver.execute_script(js_down)
        driver.find_element_by_link_text(u"报表&打印").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"报表发布").click()
        time.sleep(2)
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)

        driver.switch_to_frame("frame_tab_PM000013")
        v_search = driver.find_element_by_id("btnSearch")
        try:
            v_search.is_displayed()
            print("系统管理-报表&打印-报表发布-页面显示正常")
        except ImportError:
            print("BUG 报表&打印-报表发布-【查询】-不显示")

    def test_1106_Permission(self):
        """报表平台-报表权限-【查询】检查"""
        driver = self.driver
        driver.find_element_by_link_text(u"系统管理").click()
        time.sleep(2)
        # 移动到页面底部，防止对象遮挡
        js_down = "window.scrollTo(0,500)"
        driver.execute_script(js_down)
        driver.find_element_by_link_text(u"报表&打印").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"报表权限").click()
        time.sleep(2)
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)

        driver.switch_to_frame("frame_tab_PM000180")
        v_gpRole = driver.find_element_by_id("gpRole")
        try:
            v_gpRole.is_displayed()
            print("系统管理-报表&打印-报表权限-页面显示正常")
        except ImportError:
            print("BUG 报表&打印-报表权限-【角色列表】-不显示")

    def test_1107_Packet(self):
        """报表平台-报表分组-【查询】检查"""
        driver = self.driver
        driver.find_element_by_link_text(u"系统管理").click()
        time.sleep(2)
        # 移动到页面底部，防止对象遮挡
        js_down = "window.scrollTo(0,500)"
        driver.execute_script(js_down)
        driver.find_element_by_link_text(u"报表&打印").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"报表分组").click()
        time.sleep(2)
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)

        driver.switch_to_frame("frame_tab_PM000657")
        v_setBase = driver.find_element_by_id("gpReportSetBase")
        try:
            v_setBase.is_displayed()
            print("系统管理-报表&打印-报表分组-页面显示正常")
        except ImportError:
            print("BUG 报表&打印-报表分组-【角色列表】-不显示")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(ST11_Report("test_1102_Collect"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)