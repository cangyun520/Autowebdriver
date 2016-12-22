
from PubliCode.onlineClass import *

class ST12_Weixin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)

# # ------微信营销------
    def test_1201_Menu(self):
        """微信营销-微菜单管理-【上传】检查"""
        driver = self.driver
        driver.find_element_by_link_text(u"微信营销").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"微菜单管理").click()
        time.sleep(3)
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)

        driver.switch_to_frame("frame_tab_PM000391")
        # 切换到右侧表单页面
        v_save = driver.find_element_by_id("btnSave")
        try:
            v_save.is_displayed()
        except ImportError:
            print("BUG 微信营销-微菜单管理-【上传】-不显示")
        else:
            print("微信营销-微菜单管理-页面显示正常")

    def test_1202_Concern(self):
        """微信营销-已关注用户-【获取最新关注用户】检查"""
        driver = self.driver
        driver.find_element_by_link_text(u"微信营销").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"已关注用户").click()
        time.sleep(3)
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)

        driver.switch_to_frame("frame_tab_PM000407")
        # 切换到右侧表单页面
        v_getUser = driver.find_element_by_id("btnGetUser")
        try:
            v_getUser.is_displayed()
            print("微信营销-已经关注用户-页面显示正常")
        except ImportError:
            print("BUG 微信营销-已经关注用户-【获取最新关注用户】-不显示")

    def test_1203_Packet(self):
        """微信营销-用户分组-【一键导入】检查"""
        driver = self.driver
        driver.find_element_by_link_text(u"微信营销").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"用户分组").click()
        time.sleep(2)
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)

        driver.switch_to_frame("frame_tab_PM000408")
        v_oneStep = driver.find_element_by_id("btnOneStep")
        try:
            v_oneStep.is_displayed()
            print("微信营销-用户分组-页面显示正常")
        except ImportError:
            print("BUG 微信营销-用户分组-【一键导入】-不显示")

    def test_1204_Template(self):
        """微信营销-模板管理-【添加】检查"""
        driver = self.driver
        driver.find_element_by_link_text(u"微信营销").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"模板管理").click()
        time.sleep(3)
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)

        driver.switch_to_frame("frame_tab_PM000739")
        v_add = driver.find_element_by_id("btnAdd")
        try:
            v_add.is_displayed()
            print("微信营销-模板管理-页面显示正常")
        except ImportError:
            print("BUG 微信营销-模板管理-【添加】-不显示")

    def test_1205_Resources(self):
        """微信营销-资源管理-【保存】检查"""
        driver = self.driver
        driver.find_element_by_link_text(u"微信营销").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"资源管理").click()
        time.sleep(3)
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)

        driver.switch_to_frame("frame_tab_PM000393")
        driver.switch_to_frame("pText_IFrame")
        v_add = driver.find_element_by_id("Button11")
        try:
            v_add.is_displayed()
            print("微信营销-资源管理-页面显示正常")
        except ImportError:
            print("BUG 微信营销-资源管理-【添加】-不显示")

    def test_1206_Welcome(self):
        """微信营销-关注欢迎语-【保存】检查"""
        driver = self.driver
        driver.find_element_by_link_text(u"微信营销").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"回复管理").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"关注欢迎语").click()
        time.sleep(3)
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)

        driver.switch_to_frame("frame_tab_PM000405")
        v_save = driver.find_element_by_id("btnSave")
        try:
            v_save.is_displayed()
            print("微信营销-关注欢迎语-页面显示正常")
        except ImportError:
            print("BUG 微信营销-关注欢迎语-【保存】-不显示")

    def test_1207_Reply(self):
        """微信营销-关键字回复-【保存】检查"""
        driver = self.driver
        driver.find_element_by_link_text(u"微信营销").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"回复管理").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"关键字回复").click()
        time.sleep(3)
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)

        driver.switch_to_frame("frame_tab_PM000397")
        v_save = driver.find_element_by_id("btnAdd")
        try:
            v_save.is_displayed()
            print("微信营销-关键字回复-页面显示正常")
        except ImportError:
            print("BUG 微信营销-关键字回复-【添加】-不显示")

    def test_1208_SqlReply(self):
        """微信营销-SQL回复-【保存】检查"""
        driver = self.driver
        driver.find_element_by_link_text(u"微信营销").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"回复管理").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"SQL回复").click()
        time.sleep(3)
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)

        driver.switch_to_frame("frame_tab_PM000398")
        v_add = driver.find_element_by_id("btnAdd")
        try:
            v_add.is_displayed()
            print("微信营销-SQL回复-页面显示正常")
        except ImportError:
            print("BUG 微信营销-SQL回复-【添加】-不显示")

    def test_1209_NReply(self):
        """微信营销-异常回复-【保存】检查"""
        driver = self.driver
        driver.find_element_by_link_text(u"微信营销").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"回复管理").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"异常回复").click()
        time.sleep(2)
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)

        driver.switch_to_frame("frame_tab_PM000406")
        # 切换到右侧表单页面
        v_save = driver.find_element_by_id("btnSave")
        try:
            v_save.is_displayed()
            print("微信营销-异常回复-页面显示正常")
        except ImportError:
            print("BUG 微信营销-异常回复-【保存】-不显示")

    def test_1210_Message(self):
        """微信营销-微留言-【保存】检查"""
        driver = self.driver
        driver.find_element_by_link_text(u"微信营销").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"微互动").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"微留言").click()
        time.sleep(2)
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)

        driver.switch_to_frame("frame_tab_PM000418")
        v_button1 = driver.find_element_by_id("Button1")
        try:
            v_button1.is_displayed()
            print("微信营销-微留言-页面显示正常")
        except ImportError:
            print("BUG 微信营销-微留言-【保存】-不显示")

    def test_1211_Photo(self):
        """微信营销-微相册-【保存】检查"""
        driver = self.driver
        driver.find_element_by_link_text(u"微信营销").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"微互动").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"微相册").click()
        time.sleep(2)
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)

        driver.switch_to_frame("frame_tab_PM000419")
        # 切换到右侧表单页面
        v_button6 = driver.find_element_by_id("Button6")
        try:
            v_button6.is_displayed()
            print("微信营销-微相册-页面显示正常")
        except ImportError:
            print("BUG 微信营销-微相册-【保存】-不显示")

    def test_1212_Feedback(self):
        """微信营销-微反馈-【保存】检查"""
        driver = self.driver
        driver.find_element_by_link_text(u"微信营销").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"微互动").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"微反馈").click()
        time.sleep(2)
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)

        driver.switch_to_frame("frame_tab_PM000420")
        # 切换到右侧表单页面
        v_button2 = driver.find_element_by_id("Button2")
        try:
            v_button2.is_displayed()
            print("微信营销-微反馈-页面显示正常")
        except ImportError:
            print("BUG 微信营销-微反馈-【保存】-不显示")

    def test_1213_Vote(self):
        """微信营销-微投票-【保存】检查"""
        driver = self.driver
        driver.find_element_by_link_text(u"微信营销").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"微互动").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"微投票").click()
        time.sleep(2)
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)

        driver.switch_to_frame("frame_tab_PM000421")
        # 切换到右侧表单页面
        Vote_Query = driver.find_element_by_id("btnQuery")
        try:
            Vote_Query.is_displayed()
            print("微信营销-微投票-页面显示正常")
        except ImportError:
            print("BUG 微信营销-微投票-【保存】-不显示")

    def test_1214_Positioning(self):
        """微信营销-微信定位-【保存】检查"""
        driver = self.driver
        driver.find_element_by_link_text(u"微信营销").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"微互动").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"微信定位").click()
        time.sleep(2)
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)

        driver.switch_to_frame("frame_tab_PM000422")
        # 切换到右侧表单页面
        v_query = driver.find_element_by_id("btnQuery")
        try:
            v_query.is_displayed()
            print("微信营销-微信定位-页面显示正常")
        except ImportError:
            print("BUG 微信营销-微信定位-【保存】-不显示")
# # ------系统管理------移动端配置

    def test_1215_public(self):
        """系统管理-微信公众号-公众号设置-【查询】检查"""
        driver = self.driver
        driver.find_element_by_link_text(u"系统管理").click()
        time.sleep(2)
        # 移动到页面底部，防止对象遮挡
        js_down = "window.scrollTo(0,500)"
        driver.execute_script(js_down)
        driver.find_element_by_link_text(u"移动端配置").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"微信公众号").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"公众号设置").click()
        time.sleep(2)
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)

        # 切换到右侧表单页面
        driver.switch_to_frame("frame_tab_PM000392")
        v_add = driver.find_element_by_id("btnAdd")
        try:
            v_add.is_displayed()
            print("系统管理-微信公众号-公众号设置-页面显示正常")
        except ImportError:
            print("BUG 微信公众号-公众号设置-【保存】-不显示")

    def test_1216_enterprise(self):
        """系统管理-微信企业号-企业号设置-【添加】检查"""
        driver = self.driver
        driver.find_element_by_link_text(u"系统管理").click()
        time.sleep(2)
        # 移动到页面底部，防止对象遮挡
        js_down = "window.scrollTo(0,500)"
        driver.execute_script(js_down)
        driver.find_element_by_link_text(u"移动端配置").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"微信企业号").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"企业号设置").click()
        time.sleep(2)
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)

        # 切换到右侧表单页面
        driver.switch_to_frame("frame_tab_PM000598")
        v_add = driver.find_element_by_id("btnAdd")
        try:
            v_add.is_displayed()
            print("系统管理-微信企业号-企业号设置-页面显示正常")
        except ImportError:
            print("BUG 微信企业号-企业号设置-【添加】-不显示")

    def test_1217_application(self):
        """系统管理-微信企业号-应用中心-【添加】检查"""
        driver = self.driver
        driver.find_element_by_link_text(u"系统管理").click()
        time.sleep(2)
        # 移动到页面底部，防止对象遮挡
        js_down = "window.scrollTo(0,500)"
        driver.execute_script(js_down)
        driver.find_element_by_link_text(u"移动端配置").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"微信企业号").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"应用中心").click()
        time.sleep(2)
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)

        driver.switch_to_frame("frame_tab_PM000596")
        v_add = driver.find_element_by_id("btnAdd")
        try:
            v_add.is_displayed()
            print("系统管理-微信企业号-应用中心-页面显示正常")
        except ImportError:
            print("BUG 微信企业号-应用中心-【添加】-不显示")

    def test_1218_event(self):
        """系统管理-微信企业号-自定义事件-【添加】检查"""
        driver = self.driver
        driver.find_element_by_link_text(u"系统管理").click()
        time.sleep(2)
        # 移动到页面底部，防止对象遮挡
        js_down = "window.scrollTo(0,500)"
        driver.execute_script(js_down)
        driver.find_element_by_link_text(u"移动端配置").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"微信企业号").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"自定义事件").click()
        time.sleep(2)
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)

        driver.switch_to_frame("frame_tab_PM000595")
        v_add = driver.find_element_by_id("btnAdd")
        try:
            v_add.is_displayed()
            print("系统管理-微信企业号-自定义事件-页面显示正常")
        except ImportError:
            print("BUG 微信企业号-自定义事件-【添加】-不显示")

    def test_1219_user(self):
        """系统管理-微信企业号-微信用户管理-【导出】检查"""
        driver = self.driver
        driver.find_element_by_link_text(u"系统管理").click()
        time.sleep(2)
        # 移动到页面底部，防止对象遮挡
        js_down = "window.scrollTo(0,500)"
        driver.execute_script(js_down)
        driver.find_element_by_link_text(u"移动端配置").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"微信企业号").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"微信用户管理").click()
        time.sleep(2)
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)

        driver.switch_to_frame("frame_tab_PM000615")
        v_export = driver.find_element_by_id("BtnExport")
        try:
            v_export.is_displayed()
            print("系统管理-微信企业号-微信用户管理-页面显示正常")
        except ImportError:
            print("BUG 微信企业号-微信用户管理-【导出】-不显示")

    def test_1220_reply(self):
        """系统管理-微信企业号-微信用户管理-【添加】检查"""
        driver = self.driver
        driver.find_element_by_link_text(u"系统管理").click()
        time.sleep(2)
        # 移动到页面底部，防止对象遮挡
        js_down = "window.scrollTo(0,500)"
        driver.execute_script(js_down)
        driver.find_element_by_link_text(u"移动端配置").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"微信企业号").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"企业回复管理").click()
        time.sleep(2)
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)

        driver.switch_to_frame("frame_tab_PM000653")
        v_keyword = driver.find_element_by_link_text("关键字回复")
        try:
            v_keyword.is_displayed()
            print("系统管理-微信企业号-企业回复管理-页面显示正常")
        except ImportError:
            print("BUG 微信企业号-企业回复管理-'关键字回复'-不显示")

    def test_1221_mass(self):
        """系统管理-微信企业号-群发管理-【添加】检查"""
        driver = self.driver
        driver.find_element_by_link_text(u"系统管理").click()
        time.sleep(2)
        # 移动到页面底部，防止对象遮挡
        js_down = "window.scrollTo(0,500)"
        driver.execute_script(js_down)
        driver.find_element_by_link_text(u"移动端配置").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"微信企业号").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"群发管理").click()
        time.sleep(2)
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)

        driver.switch_to_frame("frame_tab_PM000738")
        v_add = driver.find_element_by_id("btnAdd")
        try:
            v_add.is_displayed()
            print("系统管理-微信企业号-群发管理-页面显示正常")
        except ImportError:
            print("BUG 微信企业号-群发管理-【添加】-不显示")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(ST12_Weixin("test_1214_Positioning"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)