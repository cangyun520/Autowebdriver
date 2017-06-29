
from selenium.webdriver.common.action_chains import ActionChains
from PubliCode.onlineClass import *
from PubliCode.randData import *


class SalesOrder(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_part_text(self, "销售管理", "销售订单")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM001100")

    """销售管理-销售订单-新增单据功能"""
    def test_2003_01_Add(self):
        """销售管理-销售订单-新增单据功能"""
        driver = self.driver
        # 业务伙伴
        driver.find_element_by_id("btnAdd").click()
        time.sleep(5)
        # 进入到销售订单页面
        driver.switch_to.default_content()
        driver.switch_to.frame("frame_tab_PM000190")
        driver.find_element_by_xpath("//*[@id='bodyContent_ctl73_Container']/div/div/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")     # 切换到业务伙伴选择窗体
        driver.find_element_by_id("txtSearchText").send_keys("C")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(2)
        driver.find_elements_by_class_name("x-grid3-row")[1].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(4)
        driver.switch_to.parent_frame()
        v_tim = time.strftime("%Y-%m-%d %H:%M:%S")
        driver.find_element_by_xpath(
            "//*[@id='GridPanelItem']/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath(
            "//*[@id='GridPanelItem']/div/div/div/div/div[2]/div[2]/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")     # 切换到物料选择窗体
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

        # 收款阶段
        driver.find_element_by_link_text("收款阶段").click()
        time.sleep(1)
        # 收款阶段-行数据添加
        v_lines = driver.find_element_by_xpath(
            "//*[@id='gpBorrow']/div/div/div/div/div[2]")
        ActionChains(driver).context_click(v_lines).perform()
        driver.find_element_by_link_text("添加行").click()
        time.sleep(1)
        # 收款阶段-收款名称
        v_project = driver.find_element_by_xpath(
            "//*[@id='gpBorrow']/div/div/div/div/div[2]/div/div/table/tbody/tr/td[2]")
        ActionChains(driver).double_click(v_project).perform()
        driver.find_element_by_xpath(
            "//*[@id='gpBorrow']/div/div/div/div/div[2]/div[2]/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")
        driver.find_elements_by_class_name("x-grid3-row")[0].click()
        driver.find_element_by_id("Button1").click()
        time.sleep(2)
        driver.switch_to.parent_frame()

        driver.find_element_by_id("btnSave").click()
        time.sleep(5)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        if len(v_tip) == 0:
            print("没有获取到提示窗体")
            unittest.expectedFailure("test_2003_01_Add")
        else:
            for i in v_tip:
                if "成功" in i.text:
                    print(i.text)
                elif "流程已触发" in i.text:
                    print(i.text)
                else:
                    print(i.text)
                    unittest.expectedFailure("test_2003_01_Add")
                    driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2003_01_Add.jpg")

    """销售管理-销售订单-客户主数据穿透功能"""
    def test_2003_02_Penetrate(self):
        """销售管理-销售订单-客户主数据穿透功能"""
        driver = self.driver
        driver.find_element_by_id("select2-txtDataType-container").click()
        time.sleep(1)
        v_list_state = driver.find_elements_by_class_name("select2-results__option")
        for i in v_list_state:
            if i.text == "全部订单":
                i.click()
                time.sleep(1)
                break
        v_table = driver.find_element_by_id("gridList")
        v_rows = v_table.find_elements_by_tag_name("tr")
        if len(v_rows) > 1:
            v_cols = v_rows[1].find_elements_by_tag_name("td")
            v_cols[1].click()
            time.sleep(4)
        driver.switch_to.default_content()
        # 进入到销售订单页面
        driver.switch_to.frame("frame_tab_PM000190")
        driver.find_element_by_id("btnGoOCRD").click()      # 客户主数据穿透
        time.sleep(4)
        driver.switch_to.frame("winActivity_IFrame")     # 切换到业务伙伴主数据查看页面
        if driver.find_element_by_link_text("常规").is_displayed():
            print("销售管理-销售订单穿透到业务伙伴主数据页面显示OK")
        else:
            print("BUG 销售管理-销售订单穿透到业务伙伴主数据页面显示异常")
            unittest.expectedFailure("test_2003_02_Penetrate")
            driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2003_02_Penetrate.jpg")

    """销售管理-销售订单-客户编号为空穿透提示检查"""
    def test_2003_03_Client(self):
        """销售管理-销售订单-客户编号为空穿透提示检查"""
        driver = self.driver
        driver.find_element_by_id("btnAdd").click()
        time.sleep(4)
        # 进入到销售订单页面
        driver.switch_to.default_content()
        driver.switch_to.frame("frame_tab_PM000190")
        driver.find_element_by_id("btnGoOCRD").click()      # 客户主数据穿透
        time.sleep(2)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "业务伙伴为空" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2003_03_Client.jpg")
                print(i.text)
                unittest.expectedFailure("test_2003_03_Client")

    """销售管理-销售订单-单据复制到功能"""
    def test_2003_04_goto(self):
        """销售管理-销售订单-单据复制到功能"""
        driver = self.driver
        driver.find_element_by_id("select2-txtDataType-container").click()
        time.sleep(1)
        v_list_state = driver.find_elements_by_class_name("select2-results__option")
        for i in v_list_state:
            if i.text == "全部订单":
                i.click()
                time.sleep(1)
                break
        v_table = driver.find_element_by_id("gridList")
        v_rows = v_table.find_elements_by_tag_name("tr")
        if len(v_rows) > 1:
            v_cols = v_rows[1].find_elements_by_tag_name("td")
            v_cols[1].click()
            time.sleep(4)
        driver.switch_to.default_content()
        # 进入到销售订单页面
        driver.switch_to.frame("frame_tab_PM000190")
        if driver.find_element_by_id("btnCopyTo").is_displayed():
            driver.find_element_by_id("btnCopyTo").click()
            time.sleep(1)
            v_wlcode = ("交货", "应收发票")
            v_checked = v_wlcode[random.randint(0, 1)]
            driver.find_element_by_link_text(v_checked).click()
            time.sleep(4)
            driver.switch_to.parent_frame()
            if v_checked == "交货":
                ClasForm.form_top(self, 0)
                driver.switch_to.frame("frame_tab_PM000194")
                # 排除自定义字段遮挡干扰
                ClasForm.form_field_hide(self)
                ClasForm.form_today(self, "dfDocDueDate")
            elif v_checked == "应收发票":
                ClasForm.form_top(self, 0)
                driver.switch_to.frame("frame_tab_PM000200")
                # 排除自定义字段遮挡干扰
                ClasForm.form_field_hide(self)
                ClasForm.form_today(self, "dfDocDueDate")
            driver.find_element_by_id("btnSave").click()
            time.sleep(4)
            v_tip = driver.find_elements_by_class_name("ext-mb-text")
            for i in v_tip:
                if "成功，单号" in i.text:
                    print(i.text + v_checked)
                elif "流程已触发" in i.text:
                    print(i.text + v_checked)
                else:
                    print(i.text + v_checked)
                    unittest.expectedFailure("test_2003_04_goto")
                    driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2003_04_goto.jpg")
        else:
            print("单据已清，不能复制到")

    """销售管理-销售订单-目标凭证查看"""
    def test_2003_05_target(self):
        """销售管理-销售订单-目标凭证查看"""
        driver = self.driver
        driver.find_element_by_id("select2-txtDataType-container").click()
        time.sleep(1)
        v_list_state = driver.find_elements_by_class_name("select2-results__option")
        for i in v_list_state:
            if i.text == "全部订单":
                i.click()
                time.sleep(1)
                break
        driver.find_element_by_id("btnSuperSearch").click()
        time.sleep(1)
        driver.find_element_by_id("select2-CustomerType-container").click()
        time.sleep(1)
        v_list_state = driver.find_elements_by_class_name("select2-results__option")
        for i in v_list_state:
            # print(i.text)
            if "已清" in i.text:
                i.click()
                time.sleep(1)
                break
        driver.find_element_by_id("btnDataSearch").click()
        time.sleep(1)
        v_table = driver.find_element_by_id("gridList")
        v_rows = v_table.find_elements_by_tag_name("tr")
        if len(v_rows) > 1:
            v_cols = v_rows[1].find_elements_by_tag_name("td")
            v_cols[1].click()
            time.sleep(5)
        # 进入到销售订单页面
        driver.switch_to.default_content()
        driver.switch_to.frame("frame_tab_PM000190")
        if driver.find_element_by_id("btnTarget").is_displayed():
            driver.find_element_by_id("btnTarget").click()
            time.sleep(3)
            driver.switch_to.default_content()
            # 获取tab对象
            v_active = driver.find_elements_by_class_name("active")
            for i in v_active:
                v_active_id = i.get_attribute("id")       # 获取对象ID
                if 0 < len(v_active_id) < 14:
                    v_menu_id = "frame_" + v_active_id
                    break
            # v_menu_id = v_active_id[3:]       # 截取第3个字符到结尾
            driver.switch_to.frame(v_menu_id)
            if driver.find_element_by_id("btnBase").is_displayed():
                print("目标凭证点击穿透查看OK")
        else:
            print("当前单据状态未清")

    """销售管理-销售订单-服务-新增功能"""
    def test_2003_06_serve(self):
        """销售管理-销售订单-服务-新增功能"""
        driver = self.driver
        driver.find_element_by_id("btnAdd").click()
        time.sleep(4)
        # 进入到销售订单页面
        driver.switch_to.default_content()
        driver.switch_to.frame("frame_tab_PM000190")
        # 业务伙伴
        driver.find_element_by_xpath("//*[@id='bodyContent_ctl73_Container']/div/div/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")     # 切换到业务伙伴选择窗体
        driver.find_element_by_id("txtSearchText").send_keys("C")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(2)
        driver.find_elements_by_class_name("x-grid3-row")[1].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        driver.switch_to.parent_frame()
        v_tim = time.strftime("%Y-%m-%d %H:%M:%S")
        # 服务类型
        driver.find_element_by_id("cbxDocType").click()
        for i in driver.find_elements_by_class_name("x-combo-list-item"):
            if i.text == "服务":
                i.click()
                break
        time.sleep(2)
        driver.find_element_by_xpath(
            "//*[@id='GridPaneServer']/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[2]").click()
        time.sleep(1)
        driver.switch_to.active_element.send_keys(v_tim + "Auto这是一次常规的体验式服务")
        # 总账科目
        driver.find_element_by_xpath(
            "//*[@id='GridPaneServer']/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[3]").click()
        time.sleep(1)
        driver.find_element_by_xpath(
            "//*[@id='GridPaneServer']/div/div/div/div/div[2]/div[3]/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")
        driver.find_element_by_id("txtAccount").send_keys("人民")
        driver.find_element_by_id("btnAccount").click()
        time.sleep(1)
        driver.find_elements_by_class_name("x-grid3-row")[0].click()
        driver.find_element_by_id("Button13").click()
        time.sleep(1)
        driver.switch_to.parent_frame()
        # 总计
        driver.find_element_by_xpath(
            "//*[@id='GridPaneServer']/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[6]").click()
        time.sleep(1)
        driver.switch_to.active_element.send_keys(random.randint(100, 9999))
        # 表头备注
        driver.find_element_by_id("txtComments").send_keys("Auto服务订单" + v_tim)
        driver.find_element_by_id("btnSave").click()
        time.sleep(4)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功" in i.text:
                print(i.text)
            elif "流程已触发" in i.text:
                print(i.text)
            else:
                print(i.text)
                unittest.expectedFailure("test_2003_06_serve")

    """销售管理-销售订单-复制从销售报价单功能"""
    def test_2003_07_copyfrom(self):
        """销售管理-销售订单-复制从销售报价单功能"""
        driver = self.driver
        driver.find_element_by_id("btnAdd").click()
        time.sleep(4)
        # 进入到销售订单页面
        driver.switch_to.default_content()
        driver.switch_to.frame("frame_tab_PM000190")
        # 业务伙伴
        driver.find_element_by_xpath("//*[@id='bodyContent_ctl73_Container']/div/div/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")     # 切换到业务伙伴选择窗体
        driver.find_element_by_id("txtSearchText").send_keys("C")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(2)
        driver.find_elements_by_class_name("x-grid3-row")[1].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(4)
        driver.switch_to.parent_frame()
        driver.find_element_by_id("btnCopyFrom").click()
        driver.find_element_by_link_text("销售报价单").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")
        v_list = driver.find_elements_by_class_name("x-grid3-row")
        if len(v_list) > 0:
            v_list[0].click()
            driver.find_element_by_id("btnSelect").click()
            time.sleep(1)
            driver.switch_to.parent_frame()
            ClasForm.form_button_yes(self, "否")
            driver.find_element_by_id("btnSave").click()
            time.sleep(5)
            v_tip = driver.find_elements_by_class_name("ext-mb-text")
            for i in v_tip:
                if "成功" in i.text:
                    print(i.text)
                elif "流程已触发" in i.text:
                    print(i.text)
                else:
                    print(i.text)
                    unittest.expectedFailure("test_2003_07_copyfrom")
                    driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2003_07_copyfrom.jpg")
        else:
            # 检查窗体是否一直处于加载假死中
            ClasForm.form_loading(self, "test_2003_07_copyfrom")
            print("复制从单据数据为空")

    """销售管理-销售订单-分配销售员"""
    def test_2003_08_seller(self):
        """销售管理-销售订单-复制从销售报价单功能"""
        driver = self.driver
        driver.find_element_by_id("select2-txtDataType-container").click()
        time.sleep(1)
        v_list_state = driver.find_elements_by_class_name("select2-results__option")
        for i in v_list_state:
            if i.text == "全部订单":
                i.click()
                time.sleep(2)
                break
        driver.find_element_by_id("ckAll").click()
        driver.find_element_by_id("btnBatchFormal").click()
        time.sleep(1)
        driver.find_element_by_id("tableOSLP").click()
        driver.find_element_by_id("btnOSLPOK").click()
        time.sleep(5)
        v_tip = driver.find_elements_by_class_name("toast")
        for i in v_tip:
            if "成功" in i.text:
                print(i.text)
            else:
                print(i.text)
                unittest.expectedFailure("test_2003_07_copyfrom")
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2003_07_copyfrom.jpg")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    unittest.main()