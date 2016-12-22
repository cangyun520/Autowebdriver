# -*- coding: utf-8 -*-
from PubliCode.onlineClass import *

class ST08_Hr(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)

# # ------人力资源------
    def test_0801_Recruitment_Plan(self):
        """人力资源-招聘需求-【添加】检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"人力资源", u"招聘管理", u"招聘需求与计划")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM001012")
        Recruitment_Plan_add = driver.find_element_by_id("btnAdd")
        try:
            Recruitment_Plan_add.is_displayed()
        except ImportError:
            print("BUG 招聘需求与计划-【添加】错误")
        else:
            print("招聘需求与计划-页面-显示正常")

    def test_0802_Recruitment_Apply(self):
        """人力资源-招聘需求申请-UI检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"人力资源", u"招聘管理", u"招聘需求申请")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM001013")
        Recruitment_Apply_General = driver.find_element_by_link_text("常规")
        try:
            Recruitment_Apply_General.is_displayed()
        except ImportError:
            print("BUG 招聘需求申请-‘常规’错误")
        else:
            print("招聘需求申请-页面-显示正常")
    # # ------人力资源------人员管理
    def test_0803_People_Archives(self):
        """人力资源-档案管理-UI检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"人力资源", u"人员管理", u"档案管理")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000888")
        People_Archives_add = driver.find_element_by_id("btnAdd")
        try:
            People_Archives_add.is_displayed()
        except ImportError:
            print("BUG 人员管理-档案管理-【添加】错误")
        else:
            print("人员管理-档案管理-页面-显示正常")

    def test_0804_People_Documents(self):
        """人力资源-证照提醒-UI检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"人力资源", u"人员管理", u"证照提醒")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000889")
        People_v_search = driver.find_element_by_id("btnSearch")
        try:
            People_v_search.is_displayed()
        except ImportError:
            print("BUG 人员管理-证照提醒-【查询】错误")
        else:
            print("人员管理-证照提醒-页面-显示正常")

    def test_0805_PeopleMove_Birthday(self):
        """人力资源-生日提醒-UI检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"人力资源", u"人员管理", u"生日提醒")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000890")
        PeopleMove_Birthday_add = driver.find_element_by_id("btnSearch")
        try:
            PeopleMove_Birthday_add.is_displayed()
        except ImportError:
            print("BUG 人员管理-生日提醒-【查询】错误")
        else:
            print("人员管理-生日提醒-页面-显示正常")
    # # ------人力资源------员工异动
    def test_0806_People_TakingWork(self):
        """人力资源-入职-UI检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"人力资源", u"员工异动", u"入职")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000892")
        People_TakingWork_add = driver.find_element_by_id("btnAdd")
        try:
            People_TakingWork_add.is_displayed()
        except ImportError:
            print("BUG 员工异动-入职-【入职申请】错误")
        else:
            print("员工异动-入职-页面-显示正常")

    def test_0807_People_Regularization(self):
        """人力资源-试用转正-UI检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"人力资源", u"员工异动", u"试用转正")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000896")
        People_Regularization_add = driver.find_element_by_id("Button5")
        try:
            People_Regularization_add.is_displayed()
        except ImportError:
            print("BUG 员工异动-试用转正-【转正申请】错误")
        else:
            print("员工异动-试用转正-页面-显示正常")

    def test_0808_People_Transfer(self):
        """人力资源-调动-UI检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"人力资源", u"员工异动", u"调动")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000894")
        People_Transfer_add = driver.find_element_by_id("btnEdit_Container")
        try:
            People_Transfer_add.is_displayed()
        except ImportError:
            print("BUG 员工异动-调动-【调动申请】错误")
        else:
            print("员工异动-调动-页面-显示正常")

    def test_0809_People_Leaving(self):
        """人力资源-离职-UI检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"人力资源", u"员工异动", u"离职")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000898")
        People_Leaving_add = driver.find_element_by_id("Button7")
        try:
            People_Leaving_add.is_displayed()
        except ImportError:
            print("BUG 员工异动-离职-【离职申请】错误")
        else:
            print("员工异动-离职-页面-显示正常")

    def test_0810_People_List(self):
        """人力资源-员工花名册-UI检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"人力资源", u"员工异动", u"员工花名册")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM001008")
        People_List_Wrapper = driver.find_element_by_id("sample_2_wrapper")
        try:
            People_List_Wrapper.is_displayed()
        except ImportError:
            print("BUG 员工异动-员工花名册-数据列表错误")
        else:
            print("员工异动-员工花名册-页面-显示正常")
    # # ------人力资源------员工合同
    def test_0811_Contract_Manage(self):
        """人力资源-合同管理-UI检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"人力资源", u"员工合同", u"合同管理")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000939")
        Contract_Manage_Sign = driver.find_element_by_id("btnSign")
        try:
            Contract_Manage_Sign.is_displayed()
        except ImportError:
            print("BUG 员工合同-合同管理-【新签续签】错误")
        else:
            print("员工合同-合同管理-页面显示OK")

    def test_0812_Contract_Signed(self):
        """人力资源-合同新签/续签-UI检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"人力资源", u"员工合同", u"合同新签/续签")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000940")
        v_process = driver.find_element_by_link_text("工作流程")
        try:
            v_process.is_displayed()
        except ImportError:
            print("BUG 员工合同-合同新签/续签-工作流程错误")
        else:
            print("员工合同-合同新签/续签-页面显示OK")
            
    def test_0813_Contract_Remove(self):
        """人力资源-合同解除-UI检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"人力资源", u"员工合同", u"合同解除")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000942")
        v_add = driver.find_element_by_id("btnAdd")
        try:
            v_add.is_displayed()
        except ImportError:
            print("BUG 员工合同-合同解除-【添加】错误")
        else:
            print("员工合同-合同解除-页面显示OK")

    def test_0814_HR_Contract_Change(self):
        """人力资源-合同变更-UI检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"人力资源", u"员工合同", u"合同变更")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000944")
        Contract_Change_add = driver.find_element_by_id("btnAdd")
        try:
            Contract_Change_add.is_displayed()
        except ImportError:
            print("BUG 员工合同-合同变更-【添加】错误")
        else:
            print("员工合同-合同变更-页面显示OK")

    def test_0815_Contract_Maturity(self):
        """人力资源-合同到期-UI检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"人力资源", u"员工合同", u"合同到期")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000941")
        Contract_Maturity_ExcelExport = driver.find_element_by_id("ExcelExport")
        try:
            Contract_Maturity_ExcelExport.is_displayed()
        except ImportError:
            print("BUG 员工合同-合同到期-【添加】错误")
        else:
            print("员工合同-合同到期-页面显示OK")
    # # ------人力资源------培训管理
    def test_0812_Training_Release(self):
        """人力资源-发布培训-UI检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"人力资源", u"培训管理", u"指定培训", u"发布培训")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM001053")
        Training_data_up = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div/form/div[2]/div/div[1]/div/div/button[1]")
        try:
            Training_data_up.is_displayed()
            print("培训管理-发布培训-页面显示OK")
        except ImportError:
            print("BUG 培训管理-发布培训-【发布】错误")

    def test_0813_Training_data(self):
        """人力资源-培训资料-UI检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"人力资源", u"培训管理", u"指定培训", u"培训资料")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM001054")
        Training_data_up = driver.find_element_by_link_text(" 上传资料")
        try:
            Training_data_up.is_displayed()
            print("培训管理-培训资料-页面显示OK")
        except ImportError:
            print("BUG 培训管理-培训资料-【上传资料】错误")

    def test_0814_Training_Confirm(self):
        """人力资源-培训确认-UI检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, u"人力资源", u"培训管理", u"指定培训", u"培训确认")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM001055")
        Confirm_Refresh = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div[2]/div/div[1]/div/div/button")
        try:
            Confirm_Refresh.is_displayed()
            print("培训管理-培训确认-页面显示OK")
        except ImportError:
            print("BUG 培训管理-培训确认-【刷新】错误")

    def test_0815_v(self):
        """人力资源-培训记录-UI检查"""
        driver = self.driver
        driver.find_element_by_link_text(u"人力资源").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"培训管理").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"培训记录").click()
        # 移动到页面顶部，防止对象遮挡
        time.sleep(3)
        js = "window.scrollTo(0,0)"
        driver.execute_script(js)
        driver.switch_to_frame("frame_tab_PM001052")
        v_exportExcel = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div[1]/div/div/button")
        try:
            v_exportExcel.is_displayed()
            print("培训管理-培训记录-页面显示OK")
        except ImportError:
            print("BUG 培训管理-培训记录-【导出】错误")
    # # ------人力资源------考勤管理
    def test_0816_v(self):
        """人力资源-考勤规则设置-UI检查"""
        driver = self.driver
        driver.find_element_by_link_text(u"人力资源").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"考勤管理").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"考勤制度").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"考勤规则设置").click()
        # 移动到页面顶部，防止对象遮挡
        time.sleep(3)
        js = "window.scrollTo(0,0)"
        driver.execute_script(js)
        driver.switch_to_frame("frame_tab_PM000902")
        v_add = driver.find_element_by_id("btnAdd")
        try:
            v_add.is_displayed()
        except ImportError:
            print("BUG 考勤制度-考勤规则设置-【添加】错误")
        else:
            print("考勤制度-考勤规则设置-页面显示OK")

    def test_0817_v(self):
        """人力资源-考勤地址设置-UI检查"""
        driver = self.driver
        driver.find_element_by_link_text(u"人力资源").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"考勤管理").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"考勤制度").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"考勤地址设置").click()
        # 移动到页面顶部，防止对象遮挡
        time.sleep(3)
        js = "window.scrollTo(0,0)"
        driver.execute_script(js)
        driver.switch_to_frame("frame_tab_PM000905")
        v_add = driver.find_element_by_id("btnAdd")
        try:
            v_add.is_displayed()
        except ImportError:
            print("BUG 考勤制度-考勤地址设置-【添加】错误")
        else:
            print("考勤制度-考勤地址设置-页面显示OK")

    def test_0818_v(self):
        """人力资源-节假日设置-UI检查"""
        driver = self.driver
        driver.find_element_by_link_text(u"人力资源").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"考勤管理").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"考勤制度").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"节假日设置").click()
        # 移动到页面顶部，防止对象遮挡
        time.sleep(3)
        js = "window.scrollTo(0,0)"
        driver.execute_script(js)
        driver.switch_to_frame("frame_tab_PM000907")
        v_add = driver.find_element_by_id("btnAdd")
        try:
            v_add.is_displayed()
        except ImportError:
            print("BUG 考勤制度-节假日设置-【添加】错误")
        else:
            print("考勤制度-节假日设置-页面显示OK")

    def test_0820_v(self):
        """人力资源-员工考勤档案-UI检查"""
        driver = self.driver
        driver.find_element_by_link_text(u"人力资源").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"考勤管理").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"考勤制度").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"员工考勤档案").click()
        # 移动到页面顶部，防止对象遮挡
        time.sleep(3)
        js = "window.scrollTo(0,0)"
        driver.execute_script(js)
        driver.switch_to_frame("frame_tab_PM000904")
        v_search = driver.find_element_by_id("btnSearch")
        try:
            v_search.is_displayed()
        except ImportError:
            print("BUG 考勤制度-员工考勤档案-【添加】错误")
        else:
            print("考勤制度-员工考勤档案-页面显示OK")

    def test_0821_Attendance_Calendar(self):
        """人力资源-工作日历-UI检查"""
        driver = self.driver
        driver.find_element_by_link_text(u"人力资源").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"考勤管理").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"考勤制度").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"工作日历").click()
        # 移动到页面顶部，防止对象遮挡
        time.sleep(3)
        js = "window.scrollTo(0,0)"
        driver.execute_script(js)
        driver.switch_to_frame("frame_tab_PM000908")
        v_select = driver.find_element_by_id("btnSelect")
        try:
            v_select.is_displayed()
        except ImportError:
            print("BUG 考勤制度-工作日历-【查询】错误")
        else:
            print("考勤制度-工作日历-页面显示OK")
    # # ------人力资源------单据管理
    def test_0822_v_Leave(self):
        """人力资源-请假申请-UI检查"""
        driver = self.driver
        driver.find_element_by_link_text(u"人力资源").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"考勤管理").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"单据管理").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"请假申请").click()
        # 移动到页面顶部，防止对象遮挡
        time.sleep(3)
        js = "window.scrollTo(0,0)"
        driver.execute_script(js)
        driver.switch_to_frame("frame_tab_PM000947")
        v_add = driver.find_element_by_id("btnAdd")
        try:
            v_add.is_displayed()
        except ImportError:
            print("BUG 单据管理-工作日历-【添加】错误")
        else:
            print("单据管理-工作日历-页面显示OK")

    def test_0823_v_Trip(self):
        """人力资源-出差申请-UI检查"""
        driver = self.driver
        driver.find_element_by_link_text(u"人力资源").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"考勤管理").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"单据管理").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"出差申请").click()
        # 移动到页面顶部，防止对象遮挡
        time.sleep(3)
        js = "window.scrollTo(0,0)"
        driver.execute_script(js)
        driver.switch_to_frame("frame_tab_PM000951")
        v_add = driver.find_element_by_id("btnAdd")
        try:
            v_add.is_displayed()
        except ImportError:
            print("BUG 单据管理-出差申请-【添加】错误")
        else:
            print("单据管理-出差申请-页面显示OK")

    def test_0824_v_Goout(self):
        """人力资源-外出申请-UI检查"""
        driver = self.driver
        driver.find_element_by_link_text(u"人力资源").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"考勤管理").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"单据管理").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"外出申请").click()
        # 移动到页面顶部，防止对象遮挡
        time.sleep(3)
        js = "window.scrollTo(0,0)"
        driver.execute_script(js)
        driver.switch_to_frame("frame_tab_PM000953")
        v_add = driver.find_element_by_id("btnAdd")
        try:
            v_add.is_displayed()
        except ImportError:
            print("BUG 单据管理-外出申请-【添加】错误")
        else:
            print("单据管理-外出申请-页面显示OK")

    def test_0825_v_Overtime(self):
        """人力资源-加班申请-UI检查"""
        driver = self.driver
        driver.find_element_by_link_text(u"人力资源").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"考勤管理").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"单据管理").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"加班申请").click()
        # 移动到页面顶部，防止对象遮挡
        time.sleep(3)
        js = "window.scrollTo(0,0)"
        driver.execute_script(js)
        driver.switch_to_frame("frame_tab_PM000949")
        v_add = driver.find_element_by_id("btnAdd")
        try:
            v_add.is_displayed()
        except ImportError:
            print("BUG 单据管理-加班申请-【添加】错误")
        else:
            print("单据管理-加班申请-页面显示OK")

    def test_0826_v_Retroactive(self):
        """人力资源-补签申请-UI检查"""
        driver = self.driver
        driver.find_element_by_link_text(u"人力资源").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"考勤管理").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"单据管理").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"补签申请").click()
        # 移动到页面顶部，防止对象遮挡
        time.sleep(3)
        js = "window.scrollTo(0,0)"
        driver.execute_script(js)
        driver.switch_to_frame("frame_tab_PM001022")
        v_print = driver.find_element_by_id("btnPrint")
        try:
            v_print.is_displayed()
        except ImportError:
            print("BUG 单据管理-补签申请-【导出】错误")
        else:
            print("单据管理-补签申请-页面显示OK")
    # # ------人力资源------考勤报表
    def test_0827_v_PunchCard(self):
        """人力资源-打卡统计-UI检查"""
        driver = self.driver
        driver.find_element_by_link_text(u"人力资源").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"考勤管理").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"考勤报表").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"打卡统计").click()
        # 移动到页面顶部，防止对象遮挡
        time.sleep(3)
        js = "window.scrollTo(0,0)"
        driver.execute_script(js)
        driver.switch_to_frame("frame_tab_PM000999")
        v_export = driver.find_element_by_id("btnSuperSearch")
        try:
            v_export.is_displayed()
        except ImportError:
            print("BUG 考勤报表-打卡统计-【导出】错误")
        else:
            print("考勤报表-打卡统计-页面显示OK")

    def test_0828_v_Adjust(self):
        """人力资源-汇总调整-UI检查"""
        driver = self.driver
        driver.find_element_by_link_text(u"人力资源").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"考勤管理").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"考勤报表").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"汇总调整").click()
        # 移动到页面顶部，防止对象遮挡
        time.sleep(3)
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM001002")
        v_export = driver.find_element_by_id("Button2")
        try:
            v_export.is_displayed()
        except ImportError:
            print("BUG 汇总调整-汇总调整-【导入】错误")
        else:
            print("汇总调整-汇总调整-页面显示OK")

    def test_0829_v_Summary(self):
        """人力资源-考勤汇总-UI检查"""
        driver = self.driver
        driver.find_element_by_link_text(u"人力资源").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"考勤管理").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"考勤报表").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"考勤汇总").click()
        # 移动到页面顶部，防止对象遮挡
        time.sleep(3)
        js = "window.scrollTo(0,0)"
        driver.execute_script(js)
        driver.switch_to_frame("frame_tab_PM001003")
        v_search = driver.find_element_by_id("btnSearch")
        try:
            v_search.is_displayed()
        except ImportError:
            print("BUG 汇总调整-考勤汇总-【导入】错误")
        else:
            print("汇总调整-考勤汇总-页面显示OK")
    # # ------人力资源------社保管理
    def test_0830_v_Summary(self):
        """人力资源-员工社保档案-UI检查"""
        driver = self.driver
        driver.find_element_by_link_text(u"人力资源").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"社保管理").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"员工社保档案").click()
        # 移动到页面顶部，防止对象遮挡
        time.sleep(3)
        js = "window.scrollTo(0,0)"
        driver.execute_script(js)
        driver.switch_to_frame("frame_tab_PM001015")
        v_export = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div[2]"
                                                                "/div/div[1]/div/div/button[3]")
        try:
            v_export.is_displayed()
        except ImportError:
            print("BUG 社保管理-员工社保档案-【导出】错误")
        else:
            print("社保管理-员工社保档案-页面显示OK")

    def test_0831_v_GuaranteeDo(self):
        """人力资源-社保处理-UI检查"""
        driver = self.driver
        driver.find_element_by_link_text(u"人力资源").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"社保管理").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"社保处理").click()
        # 移动到页面顶部，防止对象遮挡
        time.sleep(3)
        js = "window.scrollTo(0,0)"
        driver.execute_script(js)
        driver.switch_to_frame("frame_tab_PM001016")
        v_export = driver.find_element_by_link_text("社保")
        try:
            v_export.is_displayed()
        except ImportError:
            print("BUG 社保管理-社保处理-【导出】错误")
        else:
            print("社保管理-社保处理-页面显示OK")
    # # ------人力资源------薪酬管理
    def test_0838_v_Program(self):
        """人力资源-薪酬方案-UI检查"""
        driver = self.driver
        driver.find_element_by_link_text(u"人力资源").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"薪酬管理").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"薪酬方案").click()
        # 移动到页面顶部，防止对象遮挡
        time.sleep(2)
        js = "window.scrollTo(0,0)"
        driver.execute_script(js)
        driver.switch_to_frame("frame_tab_PM001057")
        v_Program_add = driver.find_element_by_id("a_add")
        try:
            v_Program_add.is_displayed()
            print("薪酬管理-薪酬方案-页面显示OK")
        except ImportError:
            print("BUG 薪酬管理-薪酬方案-【新增】错误")

    def test_0839_v_Archives(self):
        """人力资源-薪酬档案-UI检查"""
        driver = self.driver
        driver.find_element_by_link_text(u"人力资源").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"薪酬管理").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"薪酬档案").click()
        # 移动到页面顶部，防止对象遮挡
        time.sleep(3)
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM001058")
        v_export = driver.find_element_by_id("btnExport")
        try:
            v_export.is_displayed()
            print("薪酬管理-薪酬档案-页面显示OK")
        except ImportError:
            print("BUG 薪酬管理-薪酬档案-【导出】错误")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(ST08_Hr("test_0827_v_PunchCard"))
    testsuit.addTest(ST08_Hr("test_0828_v_Adjust"))
    testsuit.addTest(ST08_Hr("test_0829_v_Summary"))
    testsuit.addTest(ST08_Hr("test_0830_v_Summary"))
    testsuit.addTest(ST08_Hr("test_0831_v_GuaranteeDo"))
    testsuit.addTest(ST08_Hr("test_0832_v_GuaranteeReport"))
    v_tim = time.strftime("%y%m%d%H%M")
    FileName =root_path() + 'TestReport/STRport/' + v_tim + ' ST08_Hr.html'
    fp = open(FileName, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'百度搜索测试报告',
                                           description=u'用例执行情况：')
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)
