
from selenium.webdriver.common.action_chains import ActionChains
from PubliCode.onlineClass import *
from PubliCode.randData import *


class Reimbursement(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "费用管理", "差旅费报销")
        driver.switch_to.frame("frame_tab_PM000782")

    """费用管理-差旅费报销-单据添加功能"""
    def test_0606_01_add(self):
        """费用管理-差旅费报销-单据添加功能"""
        driver = self.driver
        driver.find_element_by_id("btnAdd").click()
        time.sleep(4)
        # 切换到新增页面
        driver.switch_to.default_content()
        driver.switch_to.frame("frame_tab_PM000783")
        v_tim = time.strftime("%Y%m%d %H:%M")
        # 报销部门
        driver.find_element_by_xpath("//*[@id='OrgName_Container']/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")
        driver.find_element_by_id("txtBPartners").send_keys("总经办")
        driver.find_element_by_id("btnBPartners").click()
        time.sleep(2)
        # 报销部门-选择总经办
        driver.find_elements_by_class_name("x-grid3-row")[0].click()
        driver.find_element_by_id("Button1").click()
        time.sleep(2)
        driver.switch_to.parent_frame()
        # 报销人
        driver.find_element_by_xpath("//*[@id='PersonName_Container']/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")
        for i in driver.find_elements_by_class_name("x-grid3-row"):
            i.click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(2)
        driver.switch_to.parent_frame()
        # 出差申请单
        driver.find_element_by_xpath("//*[@id='CompositeField6_Container']/div/div/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")
        v_trip = driver.find_elements_by_class_name("x-grid3-row")
        if len(v_trip) > 0:
            v_trip[0].click()
            driver.find_element_by_id("btnSelect").click()
        else:
            driver.find_element_by_id("Button2").click()
        time.sleep(2)
        driver.switch_to.parent_frame()
        # 开户银行
        driver.find_element_by_id("AccountBank").send_keys(fun_data_bank())
        # 银行账号
        driver.find_element_by_id("Account").send_keys(fun_idcard())
        # 开户姓名
        driver.find_element_by_id("AccountName").send_keys(fun_data_name())
        # 报销事由
        driver.find_element_by_id("Remark").send_keys(v_tim + fun_data_character(100, 500))
        # 报销明细页签数据添加
        v_lines = driver.find_element_by_xpath("//*[@id='gpExpensesReimbursemen']")
        ActionChains(driver).context_click(v_lines).perform()
        driver.find_element_by_link_text("添加行").click()
        time.sleep(1)
        # ------报销明细页签------
        # 报销明细-出发日期
        v_date_start = driver.find_element_by_xpath(
            "//*[@id='gpExpensesReimbursemen']/div/div/div/div/div[2]/div/div/table/tbody/tr/td[2]"
        )
        ActionChains(driver).double_click(v_date_start).perform()
        time.sleep(1)
        ClasForm.form_today(self, "DateField1")
        time.sleep(1)
        # 报销明细-到达日期
        v_date_end = driver.find_element_by_xpath(
            "//*[@id='gpExpensesReimbursemen']/div/div/div/div/div[2]/div/div/table/tbody/tr/td[3]"
        )
        ActionChains(driver).double_click(v_date_end).perform()
        time.sleep(1)
        ClasForm.form_today_line(self, "DateField4")
        time.sleep(1)
        # 出发地点
        v_add_start = driver.find_element_by_xpath(
            "//*[@id='gpExpensesReimbursemen']/div/div/div/div/div[2]/div/div/table/tbody/tr/td[4]"
        )
        ActionChains(driver).double_click(v_add_start).perform()
        time.sleep(1)
        driver.switch_to.active_element.send_keys(fun_data_city())
        # 到达地点
        v_add_end = driver.find_element_by_xpath(
            "//*[@id='gpExpensesReimbursemen']/div/div/div/div/div[2]/div/div/table/tbody/tr/td[5]"
        )
        ActionChains(driver).double_click(v_add_end).perform()
        time.sleep(1)
        driver.switch_to.active_element.send_keys(fun_data_city())
        # 报销项目
        v_add_end = driver.find_element_by_xpath(
            "//*[@id='gpExpensesReimbursemen']/div/div/div/div/div[2]/div/div/table/tbody/tr/td[6]"
        )
        ActionChains(driver).double_click(v_add_end).perform()
        time.sleep(1)
        driver.find_element_by_xpath(
            "//*[@id='ext-comp-1006']/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")
        v_type = driver.find_elements_by_class_name("x-grid3-row")
        v_type[random.randint(0, len(v_type)-1)].click()
        driver.find_element_by_id("Button1").click()
        time.sleep(1)
        driver.switch_to.parent_frame()
        # 金额
        v_money = driver.find_element_by_xpath(
            "//*[@id='gpExpensesReimbursemen']/div/div/div/div/div[2]/div/div/table/tbody/tr/td[8]"
        )
        ActionChains(driver).double_click(v_money).perform()
        time.sleep(1)
        driver.switch_to.active_element.send_keys(random.randint(100, 9999))
        # ------补贴明细页签------
        driver.find_element_by_link_text("补贴明细").click()
        time.sleep(1)
        v_lines = driver.find_element_by_xpath("//*[@id='gpSubsidies']/div/div/div/div/div[2]")
        ActionChains(driver).context_click(v_lines).perform()
        driver.find_element_by_link_text("复制从报销明细").click()
        time.sleep(1)
        # 人数
        v_users = driver.find_element_by_xpath(
            "//*[@id='gpSubsidies']/div/div/div/div/div[2]/div/div/table/tbody/tr/td[7]"
        )
        ActionChains(driver).double_click(v_users).perform()
        time.sleep(1)
        driver.switch_to.active_element.send_keys(random.randint(1, 10))
        # 天数
        v_days = driver.find_element_by_xpath(
            "//*[@id='gpSubsidies']/div/div/div/div/div[2]/div/div/table/tbody/tr/td[8]"
        )
        ActionChains(driver).double_click(v_days).perform()
        time.sleep(1)
        driver.switch_to.active_element.send_keys(random.randint(2, 20))
        time.sleep(1)
        # 自由流审批人选择函数
        ClasFlow.flow_free(self, "bear")
        driver.find_element_by_id("btnWorkflow").click()
        time.sleep(3)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "流程已触发" in i.text:
                print(i.text)
            elif "保存成功" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/oa/test_0606_01_add.jpg")
                print(i.text)
                unittest.expectedFailure("test_0606_01_add")

    """费用管理-差旅费报销-添加页面取消"""
    def test_0606_02_close(self):
        """费用管理-差旅费报销-添加页面取消"""
        driver = self.driver
        v_table = driver.find_element_by_id("gridList")
        v_rows = v_table.find_elements_by_tag_name("tr")
        if len(v_rows) > 1:
            v_cols = v_rows[1].find_elements_by_tag_name("td")
            v_cols[0].click()
            time.sleep(4)

        driver.switch_to.default_content()
        driver.switch_to.frame("frame_tab_PM000783")

        # 取消关闭页面
        driver.find_element_by_id("btnCancel").click()
        time.sleep(2)
        ClasForm.form_button_yes(self, "是")

        driver.switch_to.default_content()
        driver.switch_to.frame("frame_tab_PM000782")

        try:
            driver.find_element_by_id("btnAdd").is_displayed()
            print("费用管理-差旅费报销-查看界面取消功能OK")
        except ImportError:
            unittest.expectedFailure("test_0604_02_close")

    """费用管理-差旅费报销-添加草稿"""
    def test_0606_03_draft(self):
        """费用管理-差旅费报销-添加草稿"""
        driver = self.driver
        driver.find_element_by_id("btnAdd").click()
        time.sleep(4)
        # 切换到新增页面
        driver.switch_to.default_content()
        driver.switch_to.frame("frame_tab_PM000783")
        v_tim = time.strftime("%Y%m%d %H:%M")
        # 报销部门
        driver.find_element_by_xpath("//*[@id='OrgName_Container']/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")
        driver.find_element_by_id("txtBPartners").send_keys("总经办")
        driver.find_element_by_id("btnBPartners").click()
        time.sleep(2)
        # 报销部门-选择总经办
        driver.find_elements_by_class_name("x-grid3-row")[0].click()
        driver.find_element_by_id("Button1").click()
        time.sleep(2)
        driver.switch_to.parent_frame()
        # 报销人
        driver.find_element_by_xpath("//*[@id='PersonName_Container']/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")
        for i in driver.find_elements_by_class_name("x-grid3-row"):
            i.click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(2)
        driver.switch_to.parent_frame()
        # 报销事由
        driver.find_element_by_id("Remark").send_keys(v_tim + "被用作草稿-删除测试数据")
        # 报销明细页签数据添加
        v_lines = driver.find_element_by_xpath("//*[@id='gpExpensesReimbursemen']/div/div/div/div/div[2]")
        ActionChains(driver).context_click(v_lines).perform()
        driver.find_element_by_link_text("添加行").click()
        time.sleep(1)

        # ------报销明细页签------
        # 报销明细-出发日期
        v_date_start = driver.find_element_by_xpath(
            "//*[@id='gpExpensesReimbursemen']/div/div/div/div/div[2]/div/div/table/tbody/tr/td[2]"
        )
        ActionChains(driver).double_click(v_date_start).perform()
        time.sleep(1)
        ClasForm.form_today(self, "DateField1")
        time.sleep(1)
        # 报销明细-到达日期
        v_date_end = driver.find_element_by_xpath(
            "//*[@id='gpExpensesReimbursemen']/div/div/div/div/div[2]/div/div/table/tbody/tr/td[3]"
        )
        ActionChains(driver).double_click(v_date_end).perform()
        time.sleep(1)
        ClasForm.form_today_line(self, "DateField4")
        time.sleep(1)
        # 出发地点
        v_add_start = driver.find_element_by_xpath(
            "//*[@id='gpExpensesReimbursemen']/div/div/div/div/div[2]/div/div/table/tbody/tr/td[4]"
        )
        ActionChains(driver).double_click(v_add_start).perform()
        time.sleep(1)
        driver.switch_to.active_element.send_keys(fun_data_city())
        # 到达地点
        v_add_end = driver.find_element_by_xpath(
            "//*[@id='gpExpensesReimbursemen']/div/div/div/div/div[2]/div/div/table/tbody/tr/td[5]"
        )
        ActionChains(driver).double_click(v_add_end).perform()
        time.sleep(1)
        driver.switch_to.active_element.send_keys(fun_data_city())
        # 报销项目
        v_add_end = driver.find_element_by_xpath(
            "//*[@id='gpExpensesReimbursemen']/div/div/div/div/div[2]/div/div/table/tbody/tr/td[6]"
        )
        ActionChains(driver).double_click(v_add_end).perform()
        time.sleep(1)
        driver.find_element_by_xpath(
            "//*[@id='ext-comp-1006']/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")
        v_type = driver.find_elements_by_class_name("x-grid3-row")
        v_type[random.randint(0, len(v_type)-1)].click()
        driver.find_element_by_id("Button1").click()
        time.sleep(1)
        driver.switch_to.parent_frame()
        # 金额
        v_money = driver.find_element_by_xpath(
            "//*[@id='gpExpensesReimbursemen']/div/div/div/div/div[2]/div/div/table/tbody/tr/td[8]"
        )
        ActionChains(driver).double_click(v_money).perform()
        time.sleep(1)
        driver.switch_to.active_element.send_keys(random.randint(100, 9999))

        driver.find_element_by_id("btnSave").click()
        time.sleep(2)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "保存草稿成功" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/oa/test_0606_03_draft.jpg")
                unittest.expectedFailure("test_0606_03_draft")

    """费用管理-差旅费报销-草稿单据删除"""
    def test_0606_04_delete(self):
        """费用管理-差旅费报销-草稿单据删除"""
        driver = self.driver
        v_table = driver.find_element_by_id("gridList")
        v_rows = v_table.find_elements_by_tag_name("tr")
        if len(v_rows) > 1:
            v_cols = v_rows[1].find_elements_by_tag_name("td")
            v_cols[0].click()
            time.sleep(4)

        driver.switch_to.default_content()
        driver.switch_to.frame("frame_tab_PM000783")

        # 取消关闭页面
        v_delete = driver.find_element_by_id("btnDelete")
        if v_delete.is_displayed():
            v_delete.click()
            v_tip = driver.find_elements_by_class_name("ext-mb-text")
            for i in v_tip:
                if "删除成功" in i.text:
                    print(i.text)
                else:
                    unittest.expectedFailure("test_0606_04_delete")
        else:
            print("页面没有删除按钮，PASS")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    unittest.main()
