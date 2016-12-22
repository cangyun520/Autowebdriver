# -*- coding: utf-8 -*-
from PubliCode.onlineClass import *


class Alarm(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)

    # 系统管理---审批流程---消息模板
    def test_1605_Message(self):
        """系统管理---审批流程---消息模板"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"系统管理", u"审批流程", u"消息模板")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000822")
        driver.find_element_by_id("txtSearchTitle").send_keys("销售报价单")
        driver.find_element_by_id("btnSelect").click()
        time.sleep(2)
        v_list = driver.find_elements_by_class_name("x-grid3-row")
        for i in v_list:
            if "销售报价单" in i.text:
                print("关键字查询 OK")
            else:
                print("BUG 关键字查询")

    def test_1605_MSet(self):
        """系统管理---审批流程---消息配置"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"系统管理", u"审批流程", u"消息配置")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        # 切换到右侧表单页面
        driver.switch_to.frame("frame_tab_PM000146")
        driver.find_element_by_id("btnSet").click()
        time.sleep(3)
        v_title = driver.find_elements_by_class_name("x-window-header-text")
        for i in v_title:
            if "设置流程信息" in i.text:
                print("审批流程-消息配置-页面显示正常")
                break
            else:
                print("BUG 审批流程-消息配置窗体不显示")

    def test_1605_Post(self):
        """系统管理---审批流程---相对岗管理"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"系统管理", u"审批流程", u"相对岗管理")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        # 切换到右侧表单页面
        driver.switch_to.frame("frame_tab_PM000231")
        driver.find_element_by_id("btnAdd").click()
        v_title = driver.find_elements_by_class_name("x-window-header-text")
        for i in v_title:
            if "相对岗信息" in i.text:
                print("审批流程-相对岗管理-页面显示正常")
                break
            else:
                print("BUG 审批流程-相对岗管理配置窗体不显示")

    def test_1605_Field(self):
        """系统管理---审批流程---工作流字段"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"系统管理", u"审批流程", u"工作流字段")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        # 切换到右侧表单页面
        driver.switch_to.frame("frame_tab_PM000424")
        v_field = driver.find_element_by_id("Button1")
        try:
            v_field.is_displayed()
            print("审批流程-固定流程设计-工作流字段-页面显示正常")
        except ImportError:
            print("BUG 审批流程-工作流字段-【全部展开】-不显示")

    def test_1605_Permission(self):
        """系统管理---审批流程---字段权限配置"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"系统管理", u"审批流程", u"字段权限配置")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        # 切换到右侧表单页面
        driver.switch_to.frame("frame_tab_PM000879")
        v_select = driver.find_element_by_id("btnSet")
        try:
            v_select.is_displayed()
            print("审批流程-固定流程设计-字段权限配置-页面显示正常")
        except ImportError:
            print("BUG 审批流程-字段权限配置-【设置】-不显示")

    def test_1605_Designer(self):
        """系统管理---审批流程---流程设计器"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"系统管理", u"审批流程", u"流程设计器")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        # 切换到右侧表单页面
        driver.switch_to.frame("frame_tab_PM000025")
        time.sleep(3)
        v_import = driver.find_element_by_id("btnImport")
        try:
            v_import.is_displayed()
            print("审批流程-固定流程设计-流程设计器-页面显示正常")
        except ImportError:
            print("BUG 审批流程-流程设计器-【导入】-不显示")

    def test_1605_Version(self):
        """系统管理---审批流程---流程版本管理"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"系统管理", u"审批流程", u"流程版本管理")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        # 切换到右侧表单页面
        driver.switch_to.frame("frame_tab_PM000026")
        v_container = driver.find_element_by_id("btnQuery_Container")
        try:
            v_container.is_displayed()
            print("审批流程-固定流程设计-流程版本管理-页面显示正常")
        except ImportError:
            print("BUG 审批流程-流程版本管理-【查询】-不显示")

    def test_1605_Alarm(self):
        """系统管理---审批流程---预警报警"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"系统管理", u"警报设置", u"预警报警")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        # 切换到右侧表单页面
        driver.switch_to.frame("frame_tab_PM000157")
        v_add = driver.find_element_by_id("btnAdd")
        try:
            v_add.is_displayed()
            print("审批流程-警报设置-预警报警-页面显示正常")
        except ImportError:
            print("BUG 审批流程-预警报警-【添加】-不显示")

    def test_1605_FreeStream(self):
        """审批流程-警报设置-自由流设计单据UI检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"系统管理", u"审批流程", u"自由流设计")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000981")
        v_search = driver.find_element_by_id("btnSearch")
        try:
            v_search.is_displayed()
            print("系统管理-审批流程-自由流设计-页面显示正常")
        except ImportError:
            print("BUG 审批流程-自由流设计-【查询】-不显示")

    def test_1605_Billboard(self):
        """系统管理-审批流程-流程看板"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"系统管理", u"审批流程", u"流程看板")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        # 切换到右侧表单页面
        driver.switch_to.frame("frame_tab_PM001019")
        v_search = driver.find_element_by_id("btnSearch")
        try:
            v_search.is_displayed()
            print("系统管理-审批流程-流程看板-页面显示正常")
        except ImportError:
            print("BUG 审批流程-流程看板-【查询】-不显示")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(Alarm("test_1616_Custom"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)