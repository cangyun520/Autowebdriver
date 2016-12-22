
from selenium.webdriver.common.action_chains import ActionChains
from PubliCode.onlineClass import *
from PubliCode.randData import *
import win32api


class FT01_FixedProcesses(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        # 打开登录页面
        ClasLogin.login_setup_fq(self)

    # 项目管理
    def test_050302_01_Initiate(self):
        """项目管理-项目立项-添加单据功能"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "项目管理", "项目立项")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000755")
        v_tim = time.strftime("%y%m%d%H%M")
        # 项目编号
        driver.find_element_by_id("txtProjectCode").send_keys("PRJNO_" + v_tim)
        # 项目名称
        write_file = open(root_path() + 'PubliData/character5K.txt', 'r')
        v_lines = write_file.read()
        v_project = random.choice([
            '南方电网公司', '国家电网公司', '郑州铁路局', '湖北交通局', '广西税务局', '上海进出口局', '南昌盐业公司',
            '新疆烟草公司', '云南公安厅', '武汉移动通信', '南京移动通信', '青海旅游局']
        )
        driver.find_element_by_id("txtProjectName").send_keys(v_project + "21世纪信息化总建设--" + v_tim)
        # 提前执行合同
        driver.find_element_by_id("cbIshasContract").click()
        driver.find_element_by_id("btnSave").click()
        time.sleep(3)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "添加成功" in i.text:
                print(i.text)
            elif "流程已触发" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_050302_01_Initiate.jpg")
                print(i.text)
                unittest.expectedFailure("test_050302_01_Initiate")

    # 项目管理------项目信息变更
    def test_050303_01_Initiate(self):
        """项目管理-项目信息变更-新增变更功能检查"""
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "项目管理", "项目信息变更")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        time.sleep(2)
        driver.switch_to_frame("frame_tab_PM000756")
        driver.find_element_by_xpath("//*[@id='trProjectCode_Container']/div/span").click()
        time.sleep(2)
        driver.switch_to_frame("winProjectNo_IFrame")
        # 查询筛选数据
        driver.find_element_by_id("txtSearchText").send_keys("PRJ")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(2)
        v_list = driver.find_elements_by_class_name("x-grid3-row")
        v_list[random.randint(0, len(v_list) - 1)].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(2)
        driver.switch_to.parent_frame()
        # 项目类型
        driver.find_element_by_id("cbProjectType").click()
        time.sleep(1)
        driver.find_elements_by_class_name("x-combo-list-item")[1].click()
        # 项目经理
        driver.find_element_by_xpath("//*[@id='tfProjectManager_Container']/div/span").click()
        time.sleep(2)
        driver.switch_to_frame("winReciver_IFrame")
        v_list_user = driver.find_elements_by_class_name("x-grid3-row")
        v_list_user[random.randint(0, len(v_list_user) - 1)].click()
        driver.find_element_by_id("btnConfirm").click()
        time.sleep(2)
        driver.switch_to.parent_frame()

        # 立项时间
        ClasForm.form_today(self, "dateBuildsData")
        # 计划开始日期
        ClasForm.form_today(self, "dateBuildsStart")
        # 预计关闭日期
        ClasForm.form_today(self, "dateBuildsEnd")
        # 合同编号
        driver.find_element_by_xpath("//*[@id='trContractNo_Container']/div/span").click()
        time.sleep(2)
        driver.switch_to_frame("winContact_IFrame")
        v_list_contract = driver.find_elements_by_class_name("x-grid3-row")
        v_list_contract[random.randint(0, len(v_list_contract) - 1)].click()
        driver.find_element_by_id("Button1").click()
        time.sleep(2)
        driver.switch_to.parent_frame()
        # 保存单据
        driver.find_element_by_id("btnSave").click()
        time.sleep(3)
        for i in driver.find_elements_by_tag_name("span"):
            if i.text == "添加成功":
                print(i.text)
                break

    # -----销售管理------销售报价单
    def test_050401_01_Initiate(self):
        """销售管理-销售报价单-新增单据功能"""
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_part_text(self, "销售管理", "销售报价单")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000192")
        # 排除自定义字段遮挡干扰
        ClasForm.form_field_hide(self, driver)
        driver.find_element_by_xpath("//*[@id='CompositeField2_Container']/div/div/div/span").click()
        time.sleep(3)
        driver.switch_to_frame("winAdd_IFrame")     # 切换到业务伙伴选择窗体
        driver.find_element_by_id("txtSearchText").send_keys("C")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(2)
        driver.find_elements_by_class_name("x-grid3-row")[1].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        v_tim = time.strftime("%Y-%m-%d %H:%M:%S")
        driver.switch_to_default_content()
        driver.switch_to_frame("frame_tab_PM000192")
        driver.find_element_by_xpath("//*[@id='GridPanelItem']/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='GridPanelItem']/div/div/div/div/div[2]/div[2]/div/span").click()
        time.sleep(2)
        driver.switch_to_frame("winAdd_IFrame")     # 切换到物料选择窗体
        driver.find_element_by_id("txtSearchText").send_keys("A000")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(1)
        v_wlcode = driver.find_elements_by_class_name("x-grid3-row")
        v_total = 0
        while v_total <= 4:
            v_wlcode[v_total].click()
            v_total += 1
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        driver.switch_to.parent_frame()
        driver.find_element_by_id("txtComments").send_keys("销售报价单添加Auto" + v_tim)
        driver.find_element_by_id("btnSave").click()
        time.sleep(4)
        driver.switch_to_default_content()
        ClasForm.form_top(self, 0)
        time.sleep(1)
        driver.switch_to_frame("frame_tab_PM000192")
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功，单号" in i.text:
                print(i.text)
            elif "流程已触发" in i.text:
                print(i.text)
            else:
                print(i.text)
                unittest.expectedFailure("test_050401_01_Initiate")

    # -----销售管理------销售订单
    def test_050402_01_Initiate(self):
        """销售管理-销售订单-新增单据功能"""
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_part_text(self, "销售管理", "销售订单")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000190")
        # 排除自定义字段遮挡干扰
        ClasForm.form_field_hide(self, driver)
        # 业务伙伴
        driver.find_element_by_xpath("//*[@id='bodyContent_ctl72_Container']/div/div/div/span").click()
        time.sleep(3)
        driver.switch_to_frame("winAdd_IFrame")     # 切换到业务伙伴选择窗体
        driver.find_element_by_id("txtSearchText").send_keys("C")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(2)
        driver.find_elements_by_class_name("x-grid3-row")[1].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        driver.switch_to.parent_frame()
        v_tim = time.strftime("%Y-%m-%d %H:%M:%S")
        driver.find_element_by_xpath("//*[@id='GridPanelItem']/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='GridPanelItem']/div/div/div/div/div[2]/div[2]/div/span").click()
        time.sleep(2)
        driver.switch_to_frame("winAdd_IFrame")     # 切换到物料选择窗体
        driver.find_element_by_id("txtSearchText").send_keys("A000")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(1)
        v_wlcode = driver.find_elements_by_class_name("x-grid3-row")
        v_total = 0
        while v_total <= 4:
            v_wlcode[v_total].click()
            v_total += 1
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        driver.switch_to.parent_frame()
        driver.find_element_by_id("txtComments").send_keys("销售订单添加Auto" + v_tim)
        driver.find_element_by_id("btnSave").click()
        time.sleep(4)
        driver.switch_to_default_content()
        ClasForm.form_top(self, 0)
        time.sleep(1)
        driver.switch_to_frame("frame_tab_PM000190")
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功" in i.text:
                print(i.text)
            elif "流程已触发" in i.text:
                print(i.text)
            else:
                print(i.text)
                unittest.expectedFailure("test_050402_01_Initiate")

    # -----销售管理------预收款申请
    def test_050403_01_Initiate(self):
        """销售管理-预收款申请-新增单据功能"""
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_part_text(self, "销售管理", "预收款申请")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000198")
        # 排除自定义字段遮挡干扰
        ClasForm.form_field_hide(self, driver)
        driver.find_element_by_xpath("//*[@id='CompositeField2_Container']/div/div/div/span").click()
        time.sleep(3)
        driver.switch_to_frame("winAdd_IFrame")     # 切换到业务伙伴选择窗体
        driver.find_element_by_id("txtSearchText").send_keys("C")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(2)
        driver.find_elements_by_class_name("x-grid3-row")[1].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        v_tim = time.strftime("%Y-%m-%d %H:%M:%S")
        driver.switch_to.parent_frame()
        # 有效期至
        ClasForm.form_today(self, "dfDocDueDate")
        driver.find_element_by_xpath("//*[@id='GridPanelItem']/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='GridPanelItem']/div/div/div/div/div[2]/div[2]/div/span").click()
        time.sleep(2)
        driver.switch_to_frame("winAdd_IFrame")     # 切换到物料选择窗体
        driver.find_element_by_id("txtSearchText").send_keys("A000")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(1)
        v_wlcode = driver.find_elements_by_class_name("x-grid3-row")
        v_total = 0
        while v_total <= 4:
            v_wlcode[v_total].click()
            v_total += 1
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        driver.switch_to.parent_frame()
        driver.find_element_by_id("txtComments").send_keys("预收款申请添加Auto" + v_tim)
        driver.find_element_by_id("btnSave").click()
        time.sleep(4)
        driver.switch_to_default_content()
        ClasForm.form_top(self, 0)
        time.sleep(1)
        driver.switch_to_frame("frame_tab_PM000198")
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功，单号" in i.text:
                print(i.text)
            elif "流程已触发" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_050403_01_Initiate.jpg")
                print(i.text)
                unittest.expectedFailure("test_050403_01_Initiate")

    # -----销售管理------应收发票
    def test_050404_01_Initiate(self):
        """销售管理-应收发票-新增单据功能"""
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_part_text(self, "销售管理", "应收发票")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000200")
        # 排除自定义字段遮挡干扰
        ClasForm.form_field_hide(self, driver)
        driver.find_element_by_xpath("//*[@id='CompositeField2_Container']/div/div/div/span").click()
        time.sleep(3)
        driver.switch_to_frame("winAdd_IFrame")     # 切换到业务伙伴选择窗体
        driver.find_element_by_id("txtSearchText").send_keys("C")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(2)
        driver.find_elements_by_class_name("x-grid3-row")[1].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        v_tim = time.strftime("%Y-%m-%d %H:%M:%S")
        driver.switch_to.parent_frame()
        driver.find_element_by_xpath("//*[@id='GridPanelItem']/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='GridPanelItem']/div/div/div/div/div[2]/div[2]/div/span").click()
        time.sleep(2)
        driver.switch_to_frame("winAdd_IFrame")     # 切换到物料选择窗体
        driver.find_element_by_id("txtSearchText").send_keys("A000")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(1)
        v_wlcode = driver.find_elements_by_class_name("x-grid3-row")
        v_total = 0
        while v_total <= 4:
            v_wlcode[v_total].click()
            v_total += 1
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        driver.switch_to.parent_frame()
        driver.find_element_by_id("txtComments").send_keys("应收发票添加Auto" + v_tim)
        driver.find_element_by_id("btnSave").click()
        time.sleep(4)
        driver.switch_to_default_content()
        ClasForm.form_top(self, 0)
        time.sleep(1)
        driver.switch_to_frame("frame_tab_PM000200")
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功，单号" in i.text:
                print(i.text)
            elif "流程已触发" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_050404_01_Initiate.jpg")
                print(i.text)
                unittest.expectedFailure("test_050404_01_Initiate")

    # -----销售管理------应收发票+付款
    def test_050405_01_Initiate(self):
        """销售管理-应收发票+付款-新增单据功能"""
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "销售管理", "应收发票+付款")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000202")
        # 排除自定义字段遮挡干扰
        ClasForm.form_field_hide(self, driver)
        v_tim = time.strftime("%Y-%m-%d %H:%M:%S")
        driver.find_element_by_xpath("//*[@id='GridPanelItem']/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='GridPanelItem']/div/div/div/div/div[2]/div[2]/div/span").click()
        time.sleep(2)
        driver.switch_to_frame("winAdd_IFrame")     # 切换到物料选择窗体
        driver.find_element_by_id("txtSearchText").send_keys("A000")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(1)
        v_wlcode = driver.find_elements_by_class_name("x-grid3-row")
        v_total = 0
        while v_total <= 4:
            v_wlcode[v_total].click()
            v_total += 1
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        driver.switch_to.parent_frame()
        driver.find_element_by_id("btnPayments").click()
        time.sleep(3)
        driver.find_element_by_id("tfTrsfrAcct").send_keys("100101")
        driver.find_element_by_id("Button11111").click()
        time.sleep(1)
        driver.find_element_by_id("btnPaySave").click()
        time.sleep(1)
        driver.find_element_by_id("txtComments").send_keys("应收发票+付款添加Auto" + v_tim)
        driver.find_element_by_id("btnSave").click()
        time.sleep(5)
        driver.switch_to_default_content()
        ClasForm.form_top(self, 0)
        time.sleep(1)
        driver.switch_to_frame("frame_tab_PM000202")
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功，单号" in i.text:
                print(i.text)
            elif "流程已触发" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_050405_01_Initiate.jpg")
                print(i.text)
                unittest.expectedFailure("test_050405_01_Initiate")

    # -----销售管理------应收贷项凭证
    def test_050406_01_Initiate(self):
        """销售管理-应收贷项凭证-新增单据功能"""
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_part_text(self, "销售管理", "应收贷项凭证")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000196")
        # 排除自定义字段遮挡干扰
        ClasForm.form_field_hide(self, driver)
        driver.find_element_by_xpath("//*[@id='CompositeField2_Container']/div/div/div/span").click()
        time.sleep(3)
        driver.switch_to_frame("winAdd_IFrame")     # 切换到业务伙伴选择窗体
        driver.find_element_by_id("txtSearchText").send_keys("C")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(2)
        driver.find_elements_by_class_name("x-grid3-row")[1].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        v_tim = time.strftime("%Y-%m-%d %H:%M:%S")
        driver.switch_to.parent_frame()
        driver.find_element_by_xpath("//*[@id='GridPanelItem']/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='GridPanelItem']/div/div/div/div/div[2]/div[2]/div/span").click()
        time.sleep(2)
        driver.switch_to_frame("winAdd_IFrame")     # 切换到物料选择窗体
        driver.find_element_by_id("txtSearchText").send_keys("A000")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(1)
        v_wlcode = driver.find_elements_by_class_name("x-grid3-row")
        v_total = 0
        while v_total <= 4:
            v_wlcode[v_total].click()
            v_total += 1
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        driver.switch_to.parent_frame()
        driver.find_element_by_id("txtComments").send_keys("应收贷项凭证添加Auto" + v_tim)
        driver.find_element_by_id("btnSave").click()
        time.sleep(4)
        driver.switch_to_default_content()
        ClasForm.form_top(self, 0)
        time.sleep(1)
        driver.switch_to_frame("frame_tab_PM000196")
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功" in i.text:
                print(i.text)
            elif "流程已触发" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_050406_01_Initiate.jpg")
                print(i.text)
                unittest.expectedFailure("test_050406_01_Initiate")

    # -----销售管理------应收预留发票
    def test_050407_01_Initiate(self):
        """销售管理-应收预留发票-新增单据功能"""
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_part_text(self, "销售管理", "应收预留发票")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000223")
        # 排除自定义字段遮挡干扰
        ClasForm.form_field_hide(self, driver)
        driver.find_element_by_xpath("//*[@id='CompositeField2_Container']/div/div/div/span").click()
        time.sleep(3)
        driver.switch_to_frame("winAdd_IFrame")     # 切换到业务伙伴选择窗体
        driver.find_element_by_id("txtBPartners").send_keys("C")
        driver.find_element_by_id("Button6").click()
        time.sleep(2)
        driver.find_elements_by_class_name("x-grid3-row")[1].click()
        time.sleep(1)
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        v_tim = time.strftime("%Y-%m-%d %H:%M:%S")
        driver.switch_to.parent_frame()
        driver.find_element_by_xpath("//*[@id='GridPanelItem']/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='GridPanelItem']/div/div/div/div/div[2]/div[2]/div/span").click()
        time.sleep(2)
        driver.switch_to_frame("winAdd_IFrame")     # 切换到物料选择窗体
        driver.find_element_by_id("txtSearchText").send_keys("A000")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(1)
        v_wlcode = driver.find_elements_by_class_name("x-grid3-row")
        v_total = 0
        while v_total <= 4:
            v_wlcode[v_total].click()
            v_total += 1
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        driver.switch_to.parent_frame()
        driver.find_element_by_id("txtComments").send_keys("应收预留发票添加Auto" + v_tim)
        driver.find_element_by_id("btnSave").click()
        time.sleep(4)
        driver.switch_to_default_content()
        ClasForm.form_top(self, 0)
        time.sleep(1)
        driver.switch_to_frame("frame_tab_PM000223")
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功" in i.text:
                print(i.text)
            elif "流程已触发" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_050407_01_Initiate.jpg")
                print(i.text)
                unittest.expectedFailure("test_050407_01_Initiate")

    # -----采购管理------采购申请
    def test_050501_01_Initiate(self):
        """采购管理-采购申请-新增单据功能检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "采购管理", "采购申请")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000294")
        # 排除自定义字段遮挡干扰
        ClasForm.form_field_hide(self, driver)
        driver.find_element_by_id("dfReqDate").send_keys(time.strftime("%Y/%m/%d"))
        v_tim = time.strftime("%Y-%m-%d %H:%M:%S")
        # 行列表区域添加行
        var_line_Initiate = driver.find_element_by_id("GridPanelItem")
        ActionChains(driver).context_click(var_line_Initiate).perform()
        driver.find_element_by_id("AddRecord").click()
        time.sleep(1)
        # 操作行物料
        driver.find_element_by_xpath("//*[@id='GridPanelItem']/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='GridPanelItem']/div/div/div/div/div[2]/div[2]/div/span").click()
        time.sleep(2)
        driver.switch_to_frame("winAdd_IFrame")     # 切换到物料选择窗体
        driver.find_element_by_id("txtSearchText").send_keys("A000")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(1)
        v_wlcode = driver.find_elements_by_class_name("x-grid3-row")
        v_total = 0
        while v_total <= 4:
            v_wlcode[v_total].click()
            v_total += 1
        time.sleep(1)
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        driver.switch_to.parent_frame()
        driver.find_element_by_id("txtComments").send_keys("采购申请添加Auto" + v_tim)
        driver.find_element_by_id("btnSave").click()
        time.sleep(4)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功" in i.text:
                print(i.text)
            elif "流程已触发" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_050501_01_Initiate.jpg")
                print(i.text)
                unittest.expectedFailure("test_050501_01_Initiate")

    # -----采购管理------采购报价单
    def test_050502_01_Initiate(self):
        """采购管理-采购报价单-新增单据功能检查"""
        driver = self.driver
        ClasMenu.menu_part_text(self, "采购管理", "采购报价单")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000193")
        # 排除自定义字段遮挡干扰
        ClasForm.form_field_hide(self, driver)
        # 选择供应商
        driver.find_element_by_xpath("//*[@id='CompositeField2_Container']/div/div/div/span").click()
        time.sleep(3)
        driver.switch_to_frame("winAdd_IFrame")     # 切换到业务伙伴选择窗体
        driver.find_element_by_id("gpSelect").click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        v_tim = time.strftime("%Y-%m-%d %H:%M:%S")
        driver.switch_to.parent_frame()
        # 要求日期
        ClasForm.form_today(self, "dfReqDate")
        # 行物料选择
        driver.find_element_by_xpath("//*[@id='GridPanelItem']/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='GridPanelItem']/div/div/div/div/div[2]/div[2]/div/span").click()
        time.sleep(2)
        driver.switch_to_frame("winAdd_IFrame")     # 切换到物料选择窗体
        driver.find_element_by_id("txtSearchText").send_keys("A000")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(1)
        v_wlcode = driver.find_elements_by_class_name("x-grid3-row")
        v_total = 0
        while v_total <= 4:
            v_wlcode[v_total].click()
            v_total += 1
        time.sleep(1)
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        driver.switch_to.parent_frame()
        driver.find_element_by_id("txtComments").send_keys("采购报价单添加Auto" + v_tim)
        driver.find_element_by_id("btnSave").click()
        time.sleep(5)
        driver.switch_to_default_content()
        ClasForm.form_top(self, 0)
        time.sleep(1)
        driver.switch_to_frame("frame_tab_PM000193")
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功" in i.text:
                print(i.text)
            elif "流程已触发" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_050502_01_Initiate.jpg")
                print(i.text)
                unittest.expectedFailure("test_050502_01_Initiate")

    # -----采购管理------采购订单
    def test_050503_01_Initiate(self):
        """采购管理-采购订单-新增单据功能检查"""
        driver = self.driver
        ClasMenu.menu_part_text(self, "采购管理", "采购订单")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000191")
        # 排除自定义字段遮挡干扰
        ClasForm.form_field_hide(self, driver)
        driver.find_element_by_xpath("//*[@id='CompositeField2_Container']/div/div/div/span").click()
        time.sleep(3)
        driver.switch_to_frame("winAdd_IFrame")     # 切换到业务伙伴选择窗体
        driver.find_element_by_id("gpSelect").click()
        time.sleep(1)
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        v_tim = time.strftime("%Y-%m-%d %H:%M:%S")
        driver.switch_to.parent_frame()
        driver.find_element_by_xpath("//*[@id='GridPanelItem']/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='GridPanelItem']/div/div/div/div/div[2]/div[2]/div/span").click()
        time.sleep(3)
        driver.switch_to_frame("winAdd_IFrame")     # 切换到物料选择窗体
        driver.find_element_by_id("txtSearchText").send_keys("A000")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(1)
        v_wlcode = driver.find_elements_by_class_name("x-grid3-row")
        v_total = 0
        while v_total <= 4:
            v_wlcode[v_total].click()
            v_total += 1
        time.sleep(1)
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        driver.switch_to.parent_frame()
        driver.find_element_by_id("txtComments").send_keys("采购订单添加Auto" + v_tim)
        driver.find_element_by_id("btnSave").click()
        time.sleep(5)
        driver.switch_to_default_content()
        ClasForm.form_top(self, 0)
        time.sleep(1)
        driver.switch_to_frame("frame_tab_PM000191")
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功，单号" in i.text:
                print(i.text)
            elif "流程已触发" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_050503_01_Initiate.jpg")
                print(i.text)
                unittest.expectedFailure("test_050503_01_Initiate")

    # -----采购管理------采购预付款申请
    def test_050505_01_Initiate(self):
        """采购管理-采购预付款申请-新增单据功能检查"""
        driver = self.driver
        ClasMenu.menu_part_text(self, "采购管理", "采购预付款申请")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000218")
        # 排除自定义字段遮挡干扰
        ClasForm.form_field_hide(self, driver)
        driver.find_element_by_xpath("//*[@id='CompositeField2_Container']/div/div/div/span").click()
        time.sleep(3)
        driver.switch_to_frame("winAdd_IFrame")     # 切换到业务伙伴选择窗体
        driver.find_element_by_id("gpSelect").click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        driver.switch_to.parent_frame()
        v_tim = time.strftime("%Y-%m-%d %H:%M:%S")
        # 有效期至
        ClasForm.form_today(self, "dfDocDueDate")
        driver.find_element_by_xpath("//*[@id='GridPanelItem']/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='GridPanelItem']/div/div/div/div/div[2]/div[2]/div/span").click()
        time.sleep(2)
        driver.switch_to_frame("winAdd_IFrame")     # 切换到物料选择窗体
        driver.find_element_by_id("txtSearchText").send_keys("A000")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(1)
        v_wlcode = driver.find_elements_by_class_name("x-grid3-row")
        v_total = 0
        while v_total <= 4:
            v_wlcode[v_total].click()
            v_total += 1
        time.sleep(1)
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        driver.switch_to.parent_frame()
        driver.find_element_by_id("txtComments").send_keys("采购预付款申请添加Auto" + v_tim)
        driver.find_element_by_id("btnSave").click()
        time.sleep(4)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功" in i.text:
                print(i.text)
            elif "流程已触发" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_050505_01_Initiate.jpg")
                print(i.text)
                unittest.expectedFailure("test_050505_01_Initiate")

    # -----采购管理------应付发票
    def test_050507_01_Initiate(self):
        """采购管理-应付发票-新增单据功能检查"""
        driver = self.driver
        ClasMenu.menu_part_text(self, "采购管理", "应付发票")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000215")
        # 排除自定义字段遮挡干扰
        ClasForm.form_field_hide(self, driver)
        driver.find_element_by_xpath("//*[@id='CompositeField2_Container']/div/div/div/span").click()
        time.sleep(3)
        driver.switch_to_frame("winAdd_IFrame")     # 切换到业务伙伴选择窗体
        driver.find_element_by_id("gpSelect").click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        v_tim = time.strftime("%Y-%m-%d %H:%M:%S")
        driver.switch_to.parent_frame()
        driver.find_element_by_xpath("//*[@id='GridPanelItem']/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='GridPanelItem']/div/div/div/div/div[2]/div[2]/div/span").click()
        time.sleep(2)
        driver.switch_to_frame("winAdd_IFrame")     # 切换到物料选择窗体
        driver.find_element_by_id("txtSearchText").send_keys("A000")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(1)
        v_wlcode = driver.find_elements_by_class_name("x-grid3-row")
        v_total = 0
        while v_total <= 4:
            v_wlcode[v_total].click()
            v_total += 1
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        driver.switch_to.parent_frame()
        driver.find_element_by_id("txtComments").send_keys("应付发票添加Auto" + v_tim)
        driver.find_element_by_id("btnSave").click()
        time.sleep(4)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功，单号" in i.text:
                print(i.text)
            elif "流程已触发" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_050507_01.jpg")
                print(i.text)
                unittest.expectedFailure("test_050507_01_Initiate")

    # -----采购管理------应付贷项凭证
    def test_050508_01_Initiate(self):
        """采购管理-应付贷项凭证-新增单据功能检查"""
        driver = self.driver
        ClasMenu.menu_part_text(self, "采购管理", "应付贷项凭证")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000219")
        # 排除自定义字段遮挡干扰
        ClasForm.form_field_hide(self, driver)
        driver.find_element_by_xpath("//*[@id='CompositeField2_Container']/div/div/div/span").click()
        time.sleep(3)
        driver.switch_to_frame("winAdd_IFrame")     # 切换到业务伙伴选择窗体
        driver.find_element_by_id("gpSelect").click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        v_tim = time.strftime("%Y-%m-%d %H:%M:%S")
        driver.switch_to.parent_frame()
        driver.find_element_by_xpath("//*[@id='GridPanelItem']/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='GridPanelItem']/div/div/div/div/div[2]/div[2]/div/span").click()
        time.sleep(2)
        driver.switch_to_frame("winAdd_IFrame")     # 切换到物料选择窗体
        driver.find_element_by_id("txtSearchText").send_keys("A000")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(1)
        v_wlcode = driver.find_elements_by_class_name("x-grid3-row")
        v_total = 0
        while v_total <= 4:
            v_wlcode[v_total].click()
            v_total += 1
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        driver.switch_to.parent_frame()
        driver.find_element_by_id("txtComments").send_keys("应付贷项凭证添加Auto" + v_tim)
        driver.find_element_by_id("btnSave").click()
        time.sleep(4)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功，单号" in i.text:
                print(i.text)
            elif "流程已触发" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_050508_01.jpg")
                print(i.text)
                unittest.expectedFailure("test_050508_01_Initiate")

    # -----采购管理------应付预留发票
    def test_050509_01_Initiate(self):
        """采购管理-应付预留发票-新增单据功能检查"""
        driver = self.driver
        ClasMenu.menu_part_text(self, "采购管理", "应付预留发票")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000221")
        # 排除自定义字段遮挡干扰
        ClasForm.form_field_hide(self, driver)
        driver.find_element_by_xpath("//*[@id='CompositeField2_Container']/div/div/div/span").click()
        time.sleep(3)
        driver.switch_to_frame("winAdd_IFrame")     # 切换到业务伙伴选择窗体
        driver.find_element_by_id("gpSelect").click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        v_tim = time.strftime("%Y-%m-%d %H:%M:%S")
        driver.switch_to.parent_frame()
        driver.find_element_by_xpath("//*[@id='GridPanelItem']/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='GridPanelItem']/div/div/div/div/div[2]/div[2]/div/span").click()
        time.sleep(2)
        driver.switch_to_frame("winAdd_IFrame")     # 切换到物料选择窗体
        driver.find_element_by_id("txtSearchText").send_keys("A000")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(1)
        v_wlcode = driver.find_elements_by_class_name("x-grid3-row")
        v_total = 0
        while v_total <= 4:
            v_wlcode[v_total].click()
            v_total += 1
        time.sleep(1)
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        driver.switch_to.parent_frame()
        driver.find_element_by_id("txtComments").send_keys("应付预留发票添加Auto" + v_tim)
        driver.find_element_by_id("btnSave").click()
        time.sleep(4)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if  "成功，单号" in i.text:
                print(i.text)
            elif "流程已触发" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_050509_01_Initiate.jpg")
                print(i.text)
                unittest.expectedFailure("test_050509_01_Initiate")

    # -----质检管理------送检单
    def test_050601_01_Initiate(self):
        """质检管理-送检单-新增单据功能检查"""
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "质检管理", "送检单")
        # 移动到页面底部，防止对象遮挡
        js_down = "window.scrollTo(0,0)"
        driver.execute_script(js_down)
        driver.switch_to_frame("frame_tab_PM000831")
        driver.find_element_by_id("BtnAdd").click()
        time.sleep(5)
        # 进入添加界面
        driver.switch_to_frame("winSendInspection_IFrame")
        driver.find_element_by_id("cbInspectionType").click()
        var_check = driver.find_elements_by_class_name("x-combo-list-item")
        var_check[0].click()
        time.sleep(1)
        driver.find_element_by_class_name("x-form-twin-triggers").find_element_by_id("ext-gen91").click()
        time.sleep(3)
        driver.switch_to_frame("winAdd_IFrame")     # 切换到订单信息选择窗体
        driver.find_element_by_id("gpSelect").click()
        driver.find_element_by_id("Button1").click()
        time.sleep(3)
        driver.switch_to.default_content()
        driver.switch_to_frame("frame_tab_PM000831")
        driver.switch_to_frame("winSendInspection_IFrame")
        driver.find_element_by_id("ext-comp-1014").click()
        time.sleep(2)
        driver.find_element_by_id("btnSave").click()
        time.sleep(5)
        driver.switch_to.parent_frame()
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "添加成功" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_050610_01_Initiate.jpg")
                print(i.text)
                unittest.expectedFailure("test_050610_01_Initiate")

    # -----库存管理------销售交货
    def test_050701_01_Initiate(self):
        """库存管理-销售交货-新增单据功能"""
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_part_text(self, "库存管理", "销售交货")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000194")
        # 排除自定义字段遮挡干扰
        ClasForm.form_field_hide(self, driver)
        driver.find_element_by_xpath("//*[@id='CompositeField2_Container']/div/div/div/span").click()
        time.sleep(3)
        driver.switch_to_frame("winAdd_IFrame")     # 切换到业务伙伴选择窗体
        driver.find_element_by_id("txtSearchText").send_keys("C")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(2)
        driver.find_elements_by_class_name("x-grid3-row")[1].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        v_tim = time.strftime("%Y-%m-%d %H:%M:%S")
        driver.switch_to_default_content()
        driver.switch_to_frame("frame_tab_PM000194")
        driver.find_element_by_xpath("//*[@id='GridPanelItem']/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='GridPanelItem']/div/div/div/div/div[2]/div[2]/div/span").click()
        time.sleep(2)
        driver.switch_to_frame("winAdd_IFrame")     # 切换到物料选择窗体
        driver.find_element_by_id("txtSearchText").send_keys("A000")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(1)
        v_wlcode = driver.find_elements_by_class_name("x-grid3-row")
        v_total = 0
        while v_total <= 4:
            v_wlcode[v_total].click()
            v_total += 1
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        driver.switch_to.parent_frame()
        driver.find_element_by_id("txtComments").send_keys("销售交货添加Auto" + v_tim)
        driver.find_element_by_id("btnSave").click()
        time.sleep(5)
        driver.switch_to_default_content()
        ClasForm.form_top(self, 0)
        time.sleep(1)
        driver.switch_to_frame("frame_tab_PM000194")
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功，单号" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_050701_01_Initiate.jpg")
                print(i.text)
                unittest.expectedFailure("test_050701_01_Initiate")

    # -----库存管理------销售退货
    def test_050702_01_Initiate(self):
        """库存管理-销售退货-新增单据功能"""
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_part_text(self, "库存管理", "销售退货")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000195")
        # 排除自定义字段遮挡干扰
        ClasForm.form_field_hide(self, driver)
        driver.find_element_by_xpath("//*[@id='CompositeField2_Container']/div/div/div/span").click()
        time.sleep(3)
        driver.switch_to_frame("winAdd_IFrame")     # 切换到业务伙伴选择窗体
        driver.find_element_by_id("txtSearchText").send_keys("C")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(2)
        driver.find_elements_by_class_name("x-grid3-row")[1].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        v_tim = time.strftime("%Y-%m-%d %H:%M:%S")
        driver.switch_to_default_content()
        driver.switch_to_frame("frame_tab_PM000195")
        driver.find_element_by_xpath("//*[@id='GridPanelItem']/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='GridPanelItem']/div/div/div/div/div[2]/div[2]/div/span").click()
        time.sleep(2)
        driver.switch_to_frame("winAdd_IFrame")     # 切换到物料选择窗体
        driver.find_element_by_id("txtSearchText").send_keys("A000")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(1)
        v_wlcode = driver.find_elements_by_class_name("x-grid3-row")
        v_total = 0
        while v_total <= 4:
            v_wlcode[v_total].click()
            v_total += 1
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        driver.switch_to.parent_frame()
        driver.find_element_by_id("txtComments").send_keys("销售退货添加Auto" + v_tim)
        driver.find_element_by_id("btnSave").click()
        time.sleep(5)
        driver.switch_to_default_content()
        ClasForm.form_top(self, 0)
        time.sleep(1)
        driver.switch_to_frame("frame_tab_PM000195")
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功，单号" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_050702_01_Initiate.jpg")
                print(i.text)
                unittest.expectedFailure("test_050702_01_Initiate")

    # -----库存管理------采购收货
    def test_050703_01_Initiate(self):
        """库存管理-采购收货-新增单据功能"""
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_part_text(self, "库存管理", "采购收货")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000197")
        # 排除自定义字段遮挡干扰
        ClasForm.form_field_hide(self, driver)
        driver.find_element_by_xpath("//*[@id='CompositeField2_Container']/div/div/div/span").click()
        time.sleep(3)
        driver.switch_to_frame("winAdd_IFrame")     # 切换到业务伙伴选择窗体
        driver.find_element_by_id("txtSearchText").send_keys("V")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(2)
        driver.find_elements_by_class_name("x-grid3-row")[1].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        v_tim = time.strftime("%Y-%m-%d %H:%M:%S")
        driver.switch_to_default_content()
        driver.switch_to_frame("frame_tab_PM000197")
        driver.find_element_by_xpath("//*[@id='GridPanelItem']/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='GridPanelItem']/div/div/div/div/div[2]/div[2]/div/span").click()
        time.sleep(2)
        driver.switch_to_frame("winAdd_IFrame")     # 切换到物料选择窗体
        driver.find_element_by_id("txtSearchText").send_keys("A000")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(1)
        v_wlcode = driver.find_elements_by_class_name("x-grid3-row")
        v_total = 0
        while v_total <= 4:
            v_wlcode[v_total].click()
            v_total += 1
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        driver.switch_to.parent_frame()
        # 有效期至
        driver.find_element_by_id("dfDocDueDate").click()
        for i in driver.find_elements_by_class_name("x-btn-mc"):
                if i.text == "今天":
                    i.click()
        time.sleep(1)
        driver.find_element_by_id("txtComments").send_keys("采购收货添加Auto" + v_tim)
        driver.find_element_by_id("btnSave").click()
        time.sleep(5)
        driver.switch_to_default_content()
        ClasForm.form_top(self, 0)
        time.sleep(1)
        driver.switch_to_frame("frame_tab_PM000197")
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功，单号" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_050703_01_Initiate.jpg")
                print(i.text)
                unittest.expectedFailure("test_050703_01_Initiate")

    # -----库存管理------采购退货
    def test_050704_01_Initiate(self):
        """库存管理-采购退货-新增单据功能"""
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_part_text(self, "库存管理", "采购退货")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000201")
        # 排除自定义字段遮挡干扰
        ClasForm.form_field_hide(self, driver)
        driver.find_element_by_xpath("//*[@id='CompositeField2_Container']/div/div/div/span").click()
        time.sleep(3)
        driver.switch_to_frame("winAdd_IFrame")     # 切换到业务伙伴选择窗体
        driver.find_element_by_id("txtSearchText").send_keys("V")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(2)
        driver.find_elements_by_class_name("x-grid3-row")[1].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        v_tim = time.strftime("%Y-%m-%d %H:%M:%S")
        driver.switch_to.parent_frame()
        driver.find_element_by_xpath("//*[@id='GridPanelItem']/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='GridPanelItem']/div/div/div/div/div[2]/div[2]/div/span").click()
        time.sleep(2)
        driver.switch_to_frame("winAdd_IFrame")     # 切换到物料选择窗体
        driver.find_element_by_id("txtSearchText").send_keys("A000")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(1)
        v_wlcode = driver.find_elements_by_class_name("x-grid3-row")
        v_total = 0
        while v_total <= 4:
            v_wlcode[v_total].click()
            v_total += 1
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        driver.switch_to.parent_frame()
        time.sleep(1)
        driver.find_element_by_id("txtComments").send_keys("采购退货添加Auto" + v_tim)
        driver.find_element_by_id("btnSave").click()
        time.sleep(5)
        driver.switch_to_default_content()
        ClasForm.form_top(self, 0)
        time.sleep(1)
        driver.switch_to_frame("frame_tab_PM000201")
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功，单号" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_050702_01_Initiate.jpg")
                print(i.text)
                unittest.expectedFailure("test_050702_01_Initiate")

    # -----库存管理------库存转储申请
    def test_05070501_01_Initiate(self):
        """库存管理-库存转储申请-新增单据功能"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "库存管理", "转储管理", "库存转储申请")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000736")
        # 排除自定义字段遮挡干扰
        ClasForm.form_field_hide(self, driver)
        driver.find_element_by_xpath("//*[@id='txtBuyer_Container']/div/span").click()
        time.sleep(3)
        driver.switch_to_frame("winAdd_IFrame")     # 切换到业务伙伴选择窗体
        driver.find_element_by_id("txtBPartners").send_keys("C")
        driver.find_element_by_id("Button6").click()
        time.sleep(2)
        driver.find_elements_by_class_name("x-grid3-row")[random.randint(0, 4)].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        v_tim = time.strftime("%Y-%m-%d %H:%M:%S")
        driver.switch_to.parent_frame()
        # 行物料选择
        driver.find_element_by_xpath("//*[@id='GridPanelNR']/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='GridPanelNR']/div/div/div/div/div[2]/div[2]/div/span").click()
        time.sleep(2)
        driver.switch_to_frame("winAdd_IFrame")     # 切换到物料选择窗体
        driver.find_element_by_id("txtItems").send_keys("A000")
        driver.find_element_by_id("btnItems").click()
        time.sleep(1)
        driver.find_elements_by_class_name("x-grid3-row")[0].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        driver.switch_to.parent_frame()
        time.sleep(1)
        # 到仓库
        v_dckcode = driver.find_elements_by_class_name("x-grid3-td-WarehouseCode")
        v_dckcode[1].click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='GridPanelNR']/div/div/div/div/div[2]/div[3]/div/span").click()
        time.sleep(3)
        driver.switch_to_frame("winAdd_IFrame")
        driver.find_elements_by_class_name("x-grid3-row")[3].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        driver.switch_to.parent_frame()
        driver.find_element_by_id("txtRemark").send_keys("库存转储申请添加Auto" + v_tim)
        driver.find_element_by_id("btnSave").click()
        time.sleep(4)
        ClasForm.form_top(self, 0)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功，单号" in i.text:
                print(i.text)
            elif "流程已触发" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_05070501_01_Initiate.jpg")
                print(i.text)
                unittest.expectedFailure("test_05070501_01_Initiate")

    # -----库存管理------库存转储
    def test_05070502_01_Initiate(self):
        """库存管理-库存转储-新增单据功能"""
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "库存管理", "转储管理", "库存转储")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000214")
        # 排除自定义字段遮挡干扰
        ClasForm.form_field_hide(self, driver)
        driver.find_element_by_xpath("//*[@id='txtBuyer_Container']/div/span").click()
        time.sleep(3)
        driver.switch_to_frame("winAdd_IFrame")     # 切换到业务伙伴选择窗体
        driver.find_element_by_id("txtBPartners").send_keys("C")
        driver.find_element_by_id("Button6").click()
        time.sleep(2)
        driver.find_elements_by_class_name("x-grid3-row")[random.randint(0, 4)].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        v_tim = time.strftime("%Y-%m-%d %H:%M:%S")
        driver.switch_to.parent_frame()
        # 到仓库
        driver.find_element_by_xpath("//*[@id='tfToWas_Container']/div/span").click()
        time.sleep(2)
        driver.switch_to_frame("winAdd_IFrame")
        driver.find_elements_by_class_name("x-grid3-row")[3].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        driver.switch_to.parent_frame()
        # 行物料选择
        driver.find_element_by_xpath("//*[@id='GridPanelNR']/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='GridPanelNR']/div/div/div/div/div[2]/div[2]/div/span").click()
        time.sleep(2)
        driver.switch_to_frame("winAdd_IFrame")     # 切换到物料选择窗体
        driver.find_element_by_id("txtItems").send_keys("A000")
        driver.find_element_by_id("btnItems").click()
        time.sleep(1)
        v_wlcode = driver.find_elements_by_class_name("x-grid3-row")
        v_total = 0
        while v_total <= 4:
            v_wlcode[v_total].click()
            v_total += 1
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        driver.switch_to.parent_frame()
        driver.find_element_by_id("txtRemark").send_keys("库存转储添加Auto" + v_tim)
        driver.find_element_by_id("btnSave").click()
        time.sleep(4)
        ClasForm.form_top(self, 0)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功" in i.text:
                print(i.text)
            elif "流程已触发" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_05070502_01_Initiate.jpg")
                print(i.text)
                unittest.expectedFailure("test_05070502_01_Initiate")

    # -----库存管理------其他入库
    def test_05070702_01_Initiate(self):
        """库存管理-其他入库-新增单据功能"""
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "库存管理", "其他出入库", "其他入库")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000207")
        # 排除自定义字段遮挡干扰
        ClasForm.form_field_hide(self, driver)
        driver.find_element_by_xpath("//*[@id='tfName_Container']/div/span").click()        # 库存收发货类型
        time.sleep(3)
        driver.switch_to_frame("winAdd_IFrame")
        driver.find_elements_by_class_name("x-grid3-row")[0].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(1)
        v_tim = time.strftime("%Y-%m-%d %H:%M:%S")
        driver.switch_to.parent_frame()
        # 行物料
        driver.find_element_by_xpath("//*[@id='GridPanelNR']/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='GridPanelNR']/div/div/div/div/div[2]/div[2]/div/span").click()
        time.sleep(2)
        driver.switch_to_frame("winAdd_IFrame")     # 切换到物料选择窗体
        driver.find_element_by_id("txtSearchText").send_keys("A000")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(1)
        v_wlcode = driver.find_elements_by_class_name("x-grid3-row")
        v_total = 0
        while v_total <= 4:
            v_wlcode[v_total].click()
            v_total += 1
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        driver.switch_to.parent_frame()
        driver.find_element_by_id("txtRemark").send_keys("其他入库添加Auto" + v_tim)
        driver.find_element_by_id("btnSave").click()
        time.sleep(4)
        ClasForm.form_top(self, 0)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功" in i.text:
                print(i.text)
            elif "流程已触发" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/test_05070702_01_Initiate.jpg")
                print(i.text)
                unittest.expectedFailure("test_05070702_01_Initiate")

    # -----库存管理------其他出库
    def test_05070701_01_Initiate(self):
        """库存管理-其他出库-新增单据功能"""
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "库存管理", "其他出入库", "其他出库")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000209")
        # 排除自定义字段遮挡干扰
        ClasForm.form_field_hide(self, driver)
        driver.find_element_by_xpath("//*[@id='tfName_Container']/div/span").click()        # 库存收发货类型
        time.sleep(3)
        driver.switch_to_frame("winAdd_IFrame")
        driver.find_elements_by_class_name("x-grid3-row")[0].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(1)
        v_tim = time.strftime("%Y-%m-%d %H:%M:%S")
        driver.switch_to.parent_frame()
        # 行物料
        driver.find_element_by_xpath("//*[@id='GridPanelNR']/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='GridPanelNR']/div/div/div/div/div[2]/div[2]/div/span").click()
        time.sleep(2)
        driver.switch_to_frame("winAdd_IFrame")     # 切换到物料选择窗体
        driver.find_element_by_id("txtSearchText").send_keys("A000")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(1)
        v_wlcode = driver.find_elements_by_class_name("x-grid3-row")
        v_total = 0
        while v_total <= 4:
            v_wlcode[v_total].click()
            v_total += 1
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        driver.switch_to.parent_frame()
        driver.find_element_by_id("txtRemark").send_keys("其他出库添加Auto" + v_tim)
        driver.find_element_by_id("btnSave").click()
        time.sleep(4)
        ClasForm.form_top(self, 0)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功" in i.text:
                print(i.text)
            elif "流程已触发" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/test_05070701_01_Initiate.jpg")
                print(i.text)
                unittest.expectedFailure("test_05070701_01_Initiate")

    # -----库存管理------借料申请单
    def test_05070601_01_Initiate(self):
        """库存管理-借料申请单-新增单据功能"""
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "库存管理", "借料还料", "借料申请单")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000871")
        # 排除自定义字段遮挡干扰
        ClasForm.form_field_hide(self, driver)
        driver.find_element_by_id("BtnAdd").click()
        time.sleep(3)
        driver.switch_to_frame("winSendInspection_IFrame")     # 切换到新增页面
        var_wlline = driver.find_element_by_xpath("//*[@id='gpBorrow']/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[2]")
        ActionChains(driver).double_click(var_wlline).perform()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='gpBorrow']/div/div/div/div/div[2]/div[2]/div/span").click()
        time.sleep(3)
        driver.switch_to_frame("winAdd_IFrame")     # 切换到物料选择窗体
        driver.find_element_by_id("txtSearchText").send_keys("A000")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(1)
        v_wlcode = driver.find_elements_by_class_name("x-grid3-row")
        v_total = 0
        while v_total <= 14:
            v_wlcode[v_total].click()
            v_total += 1
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        driver.switch_to.parent_frame()
        driver.find_element_by_id("btnSave").click()
        time.sleep(5)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "单据添加成功" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_05070601_01_Initiate.jpg")
                print(i.text)
                unittest.expectedFailure("test_05070601_01_Initiate")

    # -----库存管理------借料单
    def test_05070602_01_Initiate(self):
        """库存管理-借料申请单-新增单据功能"""
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "库存管理", "借料还料", "借料单")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000883")
        # 排除自定义字段遮挡干扰
        ClasForm.form_field_hide(self, driver)
        driver.find_element_by_id("btnAdd").click()
        time.sleep(3)
        driver.switch_to_frame("winSendInspection_IFrame")     # 切换到新增页面
        var_wlline = driver.find_element_by_xpath("//*[@id='gpBorrow']/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[2]")
        ActionChains(driver).double_click(var_wlline).perform()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='gpBorrow']/div/div/div/div/div[2]/div[2]/div/span").click()
        time.sleep(3)
        driver.switch_to_frame("winAdd_IFrame")     # 切换到物料选择窗体
        driver.find_element_by_id("txtSearchText").send_keys("A000")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(1)
        v_wlcode = driver.find_elements_by_class_name("x-grid3-row")
        v_total = 0
        while v_total <= 4:
            v_wlcode[v_total].click()
            v_total += 1
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        driver.switch_to.parent_frame()
        # 借出仓库
        driver.find_element_by_xpath("//*[@id='OutWarehouse_Container']/div/span").click()
        time.sleep(3)
        driver.switch_to_frame("winAdd_IFrame")
        driver.find_elements_by_class_name("x-grid3-row")[0].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(2)
        driver.switch_to.parent_frame()
        driver.find_element_by_id("btnSave").click()
        time.sleep(5)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "单据添加成功" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_05070602_01_Initiate.jpg")
                print(i.text)
                unittest.expectedFailure("test_05070602_01_Initiate")

    # -----订货管理------订货
    def test_050801_01_Initiate(self):
        """订货管理-订货-新增单据功能"""
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "订货管理", "订货")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM001043")
        driver.find_element_by_id("BtnAdd").click()
        time.sleep(3)
        driver.switch_to_frame("winSendInspection_IFrame")     # 切换到新增页面
        var_wlline = driver.find_element_by_xpath("//*[@id='gpBorrow']/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[2]")
        ActionChains(driver).double_click(var_wlline).perform()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='gpBorrow']/div/div/div/div/div[2]/div[2]/div/span").click()
        time.sleep(3)
        driver.switch_to_frame("winAdd_IFrame")     # 切换到物料选择窗体
        driver.find_element_by_id("txtItems").send_keys("A000")
        driver.find_element_by_id("btnItems").click()
        time.sleep(1)
        v_wlcode = driver.find_elements_by_class_name("x-grid3-row")
        v_total = 0
        while v_total <= 4:
            v_wlcode[v_total].click()
            v_total += 1
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        driver.switch_to.parent_frame()
        # 订货单位编号
        driver.find_element_by_xpath("//*[@id='PartnerNum_Container']/div/span").click()
        time.sleep(3)
        driver.switch_to_frame("winAdd_IFrame")
        driver.find_element_by_id("txtSearchText").send_keys("C2")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(1)
        driver.find_elements_by_class_name("x-grid3-row")[0].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(2)
        driver.switch_to.parent_frame()
        # 收货信息
        v_write_file = open(root_path() + '/PubliData/character5K.txt', 'r')
        v_lines = v_write_file.read()
        driver.find_element_by_id("txtTakeDeliverInfo").send_keys(v_lines[10:60])
        time.sleep(1)
        # 自由流审批人选择
        ClasFlow.flow_free(driver, "bear")
        driver.find_element_by_id("btnSave").click()
        time.sleep(5)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "流程已触发" in i.text:
                print(i.text)
            elif "成功" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_050801_01_Initiate.jpg")
                print(i.text)
                unittest.expectedFailure("test_050801_01_Initiate")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(FT01_FixedProcesses("test_050302_01_Initiate"))
    testsuit.addTest(FT01_FixedProcesses("test_050303_01_Initiate"))
    testsuit.addTest(FT01_FixedProcesses("test_050401_01_Initiate"))
    runner = unittest.TextTestRunner()
    runner.run(testsuit)