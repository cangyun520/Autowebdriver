# -*- coding: utf-8 -*-
from PubliCode.onlineClass import *

class ST13_System(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)

# # ------系统管理------系统初始化
    def test_1301_User(self):
        """系统初始化-用户-UI检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"系统管理", uu"用户")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000003")
        User_btnAdd = driver.find_element_by_id("btnAdd")
        try:
            User_btnAdd.is_displayed()
            print("系统管理-系统初始化-用户-页面显示正常")
        except ImportError:
            print("BUG 系统初始化-用户-【添加】-不显示")

    def test_1302_Department(self):
        """系统初始化-部门管理-UI检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"系统管理", uu"用户管理", u"部门管理")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        # 切换到右侧表单页面
        driver.switch_to_frame("frame_tab_PM000006")
        Department_btnAdd = driver.find_element_by_id("btnAdd")
        try:
            Department_btnAdd.is_displayed()
            print("系统管理-系统初始化-部门管理-页面显示正常")
        except ImportError:
            print("BUG 系统初始化-部门管理-【添加】-不显示")

    def test_1303_Post(self):
        """系统初始化-岗位管理-UI检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"系统管理", uu"用户管理", u"岗位管理")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        # 切换到右侧表单页面
        driver.switch_to_frame("frame_tab_PM000005")
        post_btnAdd = driver.find_element_by_id("btnAdd")
        try:
            post_btnAdd.is_displayed()
            print("系统管理-系统初始化-岗位管理-页面显示正常")
        except ImportError:
            print("BUG 系统初始化-岗位管理-【添加】-不显示")

    def test_1304_Role(self):
        """系统初始化-角色管理-UI检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"系统管理", uu"用户管理", u"角色管理")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        # 切换到右侧表单页面
        driver.switch_to_frame("frame_tab_PM000004")
        Role_btnAdd = driver.find_element_by_id("btnAdd")
        try:
            Role_btnAdd.is_displayed()
            print("系统管理-系统初始化-角色管理-页面显示正常")
        except ImportError:
            print("BUG 系统初始化-角色管理-【添加】-不显示")

    def test_1305_Groups(self):
        """系统初始化-组管理-UI检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"系统管理", uu"用户管理", u"组管理")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        # 切换到右侧表单页面
        driver.switch_to_frame("frame_tab_PM000123")
        groups_btnAdd = driver.find_element_by_id("btnAdd")
        try:
            groups_btnAdd.is_displayed()
            print("系统管理-系统初始化-组管理-页面显示正常")
        except ImportError:
            print("BUG 系统初始化-组管理-【添加】-不显示")

    def test_1305_Menu(self):
        """系统初始化-菜单管理-UI检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"系统管理", uu"功能清单", u"菜单管理")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        # 切换到右侧表单页面
        driver.switch_to_frame("frame_tab_PM000411")
        Menu_btnExpand = driver.find_element_by_id("btnExpand")
        try:
            Menu_btnExpand.is_displayed()
            print("系统管理-系统初始化-菜单管理-页面显示正常")
        except ImportError:
            print("BUG 系统初始化-菜单管理-【全部展开】-不显示")

    def test_1306_Config(self):
        """系统初始化-菜单配置-UI检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"系统管理", uu"功能清单", u"菜单配置")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        # 切换到右侧表单页面
        driver.switch_to_frame("frame_tab_PM000179")
        Config_btnExpand = driver.find_element_by_id("btnExpand")
        try:
            Config_btnExpand.is_displayed()
            print("系统管理-系统初始化-菜单配置-页面显示正常")
        except ImportError:
            print("BUG 系统初始化-菜单配置-【全部展开】-不显示")

    def test_1307_Documents(self):
        """系统初始化-单据权限-UI检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"系统管理", uu"权限配置", u"单据权限")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        # 切换到右侧表单页面
        driver.switch_to_frame("frame_tab_PM000007")
        Documents_btnExpand = driver.find_element_by_id("gpRole")
        try:
            Documents_btnExpand.is_displayed()
            print("系统管理-系统初始化-单据权限-页面显示正常")
        except ImportError:
            print("BUG 系统初始化-单据权限-‘角色列表’-不显示")

    def test_1308_Control(self):
        """系统初始化-控件设置-UI检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"系统管理", uu"权限配置", u"控件设置")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        # 切换到右侧表单页面
        driver.switch_to_frame("frame_tab_PM000177")
        Control_btnExpand = driver.find_element_by_id("Button1")
        try:
            Control_btnExpand.is_displayed()
            print("系统管理-系统初始化-控件设置-页面显示正常")
        except ImportError:
            print("BUG 系统初始化-控件设置-【全部展开】-不显示")

    def test_1309_Data(self):
        """系统初始化-数据权限-UI检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"系统管理", uu"权限配置", u"数据权限")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        # 切换到右侧表单页面
        driver.switch_to_frame("frame_tab_PM000384")
        Data_btnExpand = driver.find_element_by_id("btnAdd")
        try:
            Data_btnExpand.is_displayed()
            print("系统管理-系统初始化-控件设置-页面显示正常")
        except ImportError:
            print("BUG 系统初始化-数据权限-【添加】-不显示")

    def test_1310_Decimal(self):
        """系统初始化-读取B1小数位数-UI检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"系统管理", uu"常规设置", u"读取B1小数位数")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        # 切换到右侧表单页面
        driver.switch_to_frame("frame_tab_PM000389")
        Decimal_cbxIsTax = driver.find_element_by_id("cbxIsTax")
        try:
            Decimal_cbxIsTax.is_displayed()
            print("系统管理-系统初始化-读取B1小数位数-页面显示正常")
        except ImportError:
            print("BUG 系统初始化-读取B1小数位数-“含税”-不显示")

    def test_1311_Header(self):
        """系统初始化-表头格式自定义-UI检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"系统管理", uu"常规设置", u"表头格式自定义")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        # 切换到右侧表单页面
        driver.switch_to_frame("frame_tab_PM000172")
        Header_btnRead = driver.find_element_by_id("btnRead")
        try:
            Header_btnRead.is_displayed()
            print("系统管理-系统初始化-表头格式自定义-页面显示正常")
        except ImportError:
            print("BUG 系统初始化-表头格式自定义-【读取文件】-不显示")

    def test_1312_Row(self):
        """系统初始化-行格式自定义-UI检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"系统管理", uu"常规设置", u"行格式自定义")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        # 切换到右侧表单页面
        driver.switch_to_frame("frame_tab_PM000255")
        Row_btnSave = driver.find_element_by_id("btnSave")
        try:
            Row_btnSave.is_displayed()
            print("系统管理-系统初始化-行格式自定义-页面显示正常")
        except ImportError:
            print("BUG 系统初始化-行格式自定义-【保存】-不显示")

    def test_1313_Custom(self):
        """系统初始化-自定义字段权限-UI检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"系统管理", uu"常规设置", u"自定义字段权限")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        # 切换到右侧表单页面
        driver.switch_to_frame("frame_tab_PM000414")
        Row_btnSave = driver.find_element_by_id("gpRole")
        try:
            Row_btnSave.is_displayed()
            print("系统管理-系统初始化-自定义字段权限-页面显示正常")
        except ImportError:
            print("BUG 系统初始化-自定义字段权限-【角色列表】-不显示")

# # ------系统管理------审批警报

    def test_1314_Message(self):
        """固定流程设计-消息模板-UI检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"系统管理", u"审批警报", u"固定流程设计", u"流程基础设置", u"消息模板")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        # 切换到右侧表单页面
        driver.switch_to_frame("frame_tab_PM000822")
        Message_Select = driver.find_element_by_id("btnSelect")
        try:
            Message_Select.is_displayed()
            print("审批警报-固定流程设计-消息模板-页面显示正常")
        except ImportError:
            print("BUG 审批警报-消息模板-【查询】-不显示")

    def test_1315_MSet(self):
        """固定流程设计-消息配置-UI检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"系统管理", u"审批警报", u"固定流程设计", u"流程基础设置", u"消息配置")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        # 切换到右侧表单页面
        driver.switch_to_frame("frame_tab_PM000146")
        MSet_Select = driver.find_element_by_id("btnSelect")
        try:
            MSet_Select.is_displayed()
            print("审批警报-固定流程设计-消息配置-页面显示正常")
        except ImportError:
            print("BUG 审批警报-消息配置-【查询】-不显示")

    def test_1316_Post(self):
        """固定流程设计-相对岗管理-UI检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"系统管理", u"审批警报", u"固定流程设计", u"流程基础设置", u"相对岗管理")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        # 切换到右侧表单页面
        driver.switch_to_frame("frame_tab_PM000231")
        Post_Add = driver.find_element_by_id("btnAdd")
        try:
            Post_Add.is_displayed()
            print("审批警报-固定流程设计-相对岗管理-页面显示正常")
        except ImportError:
            print("BUG 审批警报-相对岗管理-【添加】-不显示")

    def test_1317_Field(self):
        """固定流程设计-工作流字段-UI检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"系统管理", u"审批警报", u"固定流程设计", u"流程基础设置", u"工作流字段")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        # 切换到右侧表单页面
        driver.switch_to_frame("frame_tab_PM000424")
        Field_Button1 = driver.find_element_by_id("Button1")
        try:
            Field_Button1.is_displayed()
            print("审批警报-固定流程设计-工作流字段-页面显示正常")
        except ImportError:
            print("BUG 审批警报-工作流字段-【全部展开】-不显示")

    def test_1318_Permission(self):
        """固定流程设计-字段权限配置-UI检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"系统管理", u"审批警报", u"固定流程设计", u"流程基础设置", u"字段权限配置")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        # 切换到右侧表单页面
        driver.switch_to_frame("frame_tab_PM000879")
        Select = driver.find_element_by_id("btnSelect")
        try:
            Select.is_displayed()
            print("审批警报-固定流程设计-字段权限配置-页面显示正常")
        except ImportError:
            print("BUG 审批警报-字段权限配置-【设置】-不显示")

    def test_1319_Designer(self):
        """审批警报-固定流程设计-流程设计器单据UI检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"系统管理", u"审批警报", u"固定流程设计", u"流程基础设置", u"流程设计器")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        # 切换到右侧表单页面
        driver.switch_to_frame("frame_tab_PM000025")
        Designer_Import = driver.find_element_by_id("btnImport")
        try:
            Designer_Import.is_displayed()
            print("审批警报-固定流程设计-流程设计器-页面显示正常")
        except ImportError:
            print("BUG 审批警报-流程设计器-【导入】-不显示")

    def test_1320_Version(self):
        """审批警报-固定流程设计-流程版本管理单据UI检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"系统管理", u"审批警报", u"固定流程设计", u"流程基础设置", u"流程版本管理")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        # 切换到右侧表单页面
        driver.switch_to_frame("frame_tab_PM000026")
        Version_Container = driver.find_element_by_id("btnQuery_Container")
        try:
            Version_Container.is_displayed()
            print("审批警报-固定流程设计-流程版本管理-页面显示正常")
        except ImportError:
            print("BUG 审批警报-流程版本管理-【查询】-不显示")

    def test_1321_Alarm(self):
        """审批警报-警报设置-预警报警单据UI检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"系统管理", u"审批警报", u"警报设置", u"预警报警")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        # 切换到右侧表单页面
        driver.switch_to_frame("frame_tab_PM000157")
        Alarm_Add = driver.find_element_by_id("btnAdd")
        try:
            Alarm_Add.is_displayed()
            print("审批警报-警报设置-预警报警-页面显示正常")
        except ImportError:
            print("BUG 审批警报-预警报警-【添加】-不显示")

    def test_1322_Association(self):
        """审批警报-警报设置-数据相关单据UI检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"系统管理", u"审批警报", u"数据相关")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        # 切换到右侧表单页面
        driver.switch_to_frame("frame_tab_PM000181")
        Association_Add = driver.find_element_by_id("btnAdd")
        try:
            Association_Add.is_displayed()
            print("系统管理-审批警报-数据相关-页面显示正常")
        except ImportError:
            print("BUG 审批警报-数据相关-【添加】-不显示")

    def test_1323_FreeStream(self):
        """审批警报-警报设置-自由流设计单据UI检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"系统管理", u"审批警报", u"自由流设计")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000981")
        FreeStream_Search = driver.find_element_by_id("btnSearch")
        try:
            FreeStream_Search.is_displayed()
            print("系统管理-审批警报-自由流设计-页面显示正常")
        except ImportError:
            print("BUG 审批警报-自由流设计-【查询】-不显示")

    def test_1324_Billboard(self):
        """系统管理-审批警报-流程看板-UI检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"系统管理", u"审批警报", u"流程看板")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        # 切换到右侧表单页面
        driver.switch_to_frame("frame_tab_PM001019")
        Billboard_Search = driver.find_element_by_id("btnSearch")
        try:
            Billboard_Search.is_displayed()
            print("系统管理-审批警报-流程看板-页面显示正常")
        except ImportError:
            print("BUG 审批警报-流程看板-【查询】-不显示")
# # ------系统管理------支持中心

    def test_1325_HRdictionary(self):
        """系统管理-支持中心-HR字典数据-UI检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"系统管理", u"支持中心", u"数据字典", u"HR字典数据")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        # 切换到右侧表单页面
        driver.switch_to_frame("frame_tab_PM000829")
        HRdictionary_Save = driver.find_element_by_link_text("保存已修改的字典项")
        try:
            HRdictionary_Save.is_displayed()
            print("系统管理-数据字典-HR字典数据-页面显示正常")
        except ImportError:
            print("BUG 数据字典-HR字典数据-【保存已修改的字典项】-不显示")

    def test_1326_view(self):
        """系统管理-支持中心-系统视图-UI检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"系统管理", u"支持中心", u"系统视图")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        # 切换到右侧表单页面
        driver.switch_to_frame("frame_tab_PM000385")
        view_Add = driver.find_element_by_id("btnAdd")
        try:
            view_Add.is_displayed()
            print("系统管理-支持中心-系统视图-页面显示正常")
        except ImportError:
            print("BUG 支持中心-系统视图-【保存已修改的字典项】-不显示")

    def test_1327_log(self):
        """系统管理-支持中心-系统日志-UI检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"系统管理", u"支持中心", u"系统日志")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        # 切换到右侧表单页面
        driver.switch_to_frame("frame_tab_PM000008")
        log_Search = driver.find_element_by_id("btnOpSearch")
        try:
            log_Search.is_displayed()
            print("系统管理-支持中心-系统日志-页面显示正常")
        except ImportError:
            print("BUG 支持中心-系统日志-【查询】-不显示")

    def test_1328_help(self):
        """系统管理-支持中心-帮助中心-UI检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"系统管理", u"支持中心", u"帮助中心")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        # 切换到右侧表单页面
        driver.switch_to_frame("frame_tab_PM000599")
        help_Button2 = driver.find_element_by_id("Button2")
        try:
            help_Button2.is_displayed()
            print("系统管理-支持中心-帮助中心-页面显示正常")
        except ImportError:
            print("BUG 支持中心-帮助中心-【收起】-不显示")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()

    testsuit.addTest(ST13_System("test_1313_Custom"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)