
from selenium.webdriver.common.action_chains import ActionChains
from PubliCode.onlineClass import *
from PubliCode.randData import *


class SalesQuotation(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_part_text(self, "销售管理", "销售报价单")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000192")
        # 排除自定义字段遮挡干扰
        ClasForm.form_field_hide(self)

    '''销售管理-销售报价单-新增'''
    def test_2002_01_Add(self):
        """销售管理-销售报价单-新增"""
        driver = self.driver
        driver.find_element_by_xpath("//*[@id='CompositeField2_Container']/div/div/div/span").click()
        time.sleep(3)
        # 切换到业务伙伴选择窗体
        driver.switch_to.frame("winAdd_IFrame")
        driver.find_element_by_id("txtSearchText").send_keys("C")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(2)
        driver.find_elements_by_class_name("x-grid3-row")[1].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        v_tim = time.strftime("%Y-%m-%d %H:%M:%S")
        driver.switch_to.default_content()
        driver.switch_to.frame("frame_tab_PM000192")
        driver.find_element_by_xpath(
            "//*[@id='GridPanelItem']/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath(
            "//*[@id='GridPanelItem']/div/div/div/div/div[2]/div[2]/div/span").click()
        time.sleep(2)
        # 切换到物料选择窗体
        driver.switch_to.frame("winAdd_IFrame")
        driver.find_element_by_id("txtSearchText").send_keys("A000")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(1)
        v_wlcode = driver.find_elements_by_class_name("x-grid3-row")
        if len(v_wlcode) > 5:
            v_total = 0
            while v_total <= 4:
                v_wlcode[v_total].click()
                v_total += 1
        else:
            v_wlcode[0].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        driver.switch_to.parent_frame()
        driver.find_element_by_id("txtComments").send_keys("销售报价单添加Auto" + v_tim)
        driver.find_element_by_id("btnSave").click()
        time.sleep(5)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if u"成功" in i.text:
                print(i.text)
                result = True
            elif u"流程已触发" in i.text:
                print(i.text)
                result = True
            else:
                result = False
        if result:
            pass
        else:
            unittest.expectedFailure("test_2002_01_Add")
            driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2002_01_Add.jpg")

    '''销售管理-销售报价单-客户编号为空穿透提示检查'''
    def test_2002_02_Client(self):
        """销售管理-销售报价单-客户编号为空穿透提示检查"""
        driver = self.driver
        driver.find_element_by_id("btnGoOCRD").click()      # 客户主数据穿透
        time.sleep(2)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if u"业务伙伴为空" in i.text:
                print(i.text)
            else:
                print(i.text)
                unittest.expectedFailure("test_2002_02_Client")
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2002_02_Client.jpg")

    '''销售管理-销售报价单-客户主数据穿透功能'''
    def test_2002_03_btnFirst(self):
        """销售管理-销售报价单-客户主数据穿透功能"""
        driver = self.driver
        driver.find_element_by_id("btnFirst").click()
        time.sleep(3)
        # 客户主数据穿透
        driver.find_element_by_id("btnGoOCRD").click()
        time.sleep(3)
        # 切换到业务伙伴主数据查看页面
        driver.switch_to.frame("winActivity_IFrame")
        if driver.find_element_by_link_text("常规").is_displayed():
            print("销售管理-销售报价单穿透到业务伙伴主数据页面显示OK")
        else:
            driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2002_03_last.jpg")
            unittest.expectedFailure("test_2002_03_last")

    '''销售管理-销售报价单-复制到-销售订单'''
    def test_2002_04_goto_order(self):
        """销售管理-销售报价单-新增单据功能"""
        driver = self.driver
        driver.find_element_by_id("btnLast").click()
        time.sleep(3)
        if driver.find_element_by_id("btnCopyTo").is_displayed():
            driver.find_element_by_id("btnCopyTo").click()
            time.sleep(1)
            driver.find_element_by_link_text("销售订单").click()
            time.sleep(4)
            driver.switch_to.parent_frame()
            driver.switch_to.frame("frame_tab_PM000190")
            driver.find_element_by_id("btnSave").click()
            time.sleep(4)
            v_tip = driver.find_elements_by_class_name("ext-mb-text")
            for i in v_tip:
                if u"成功" in i.text:
                    print(i.text)
                elif u"流程已触发" in i.text:
                    print(i.text)
                else:
                    print(i.text)
                    unittest.expectedFailure("test_2002_04_goto_order")
                    driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2002_04_goto_order.jpg")
        else:
            print("单据已清，不能复制到")

    '''销售管理-销售报价单-目标凭证查看'''
    def test_2002_05_target(self):
        """销售管理-销售报价单-目标凭证查看功能"""
        driver = self.driver
        driver.find_element_by_id("btnLast").click()
        time.sleep(3)
        if driver.find_element_by_id("btnTarget").is_displayed():
            driver.find_element_by_id("btnTarget").click()
            time.sleep(3)
            driver.switch_to.default_content()
            v_active = driver.find_elements_by_class_name("active")        # 获取tab对象
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

    '''销售管理-销售报价单-单据复制功能'''
    def test_2002_06_copy(self):
        """销售管理-销售报价单-单据复制功能"""
        driver = self.driver
        driver.find_element_by_id("btnPrevious").click()
        time.sleep(3)
        v_object = driver.find_element_by_id("tfCardCode")
        ActionChains(driver).context_click(v_object).perform()
        time.sleep(1)
        driver.find_element_by_id("MenuCopy").click()
        time.sleep(3)
        v_tim = time.strftime("%Y-%m-%d %H:%M:%S")
        # 选择客户
        driver.find_element_by_xpath(
            "//*[@id='CompositeField2_Container']/div/div/div/span").click()
        time.sleep(4)
        driver.switch_to.frame("winAdd_IFrame")     # 切换到业务伙伴选择窗体
        driver.find_element_by_id("txtSearchText").send_keys("C")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(2)
        driver.find_elements_by_class_name("x-grid3-row")[1].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(2)
        driver.switch_to.parent_frame()
        # 是否依据新的业务伙伴数据更新凭证行
        ClasForm.form_button_yes(self, "是")
        # 备注
        driver.find_element_by_id("txtComments").send_keys("单据复制添加Auto" + v_tim)
        time.sleep(1)
        driver.find_element_by_id("btnSave").click()
        time.sleep(6)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if u"成功" in i.text:
                print(i.text)
            elif u"流程已触发" in i.text:
                print(i.text)
            else:
                print(i.text)
                unittest.expectedFailure("test_2002_06_copy")
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2002_06_copy.jpg")

    '''销售管理-销售报价单-复制到-交货'''
    def test_2002_07_goto_delivery(self):
        """销售管理-销售报价单-复制到-交货"""
        driver = self.driver
        driver.find_element_by_id("btnLast").click()
        time.sleep(3)
        if driver.find_element_by_id("btnCopyTo").is_displayed():
            driver.find_element_by_id("btnCopyTo").click()
            time.sleep(1)
            driver.find_element_by_link_text("交货").click()
            time.sleep(4)
            driver.switch_to.parent_frame()
            ClasForm.form_top(self, 0)
            driver.switch_to.frame("frame_tab_PM000194")
            # 排除自定义字段遮挡干扰
            ClasForm.form_field_hide(self)
            # 交货日期
            ClasForm.form_today(self, "dfDocDueDate")
            # 行数据列表
            v_lines = driver.find_element_by_xpath(
                "//*[@id='GridPanelItem']/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[3]"
            ).click()
            time.sleep(1)
            ActionChains(driver).context_click(v_lines).perform()
            time.sleep(1)
            driver.find_element_by_link_text("删除行").click()
            driver.find_element_by_id("btnSave").click()
            time.sleep(4)
            v_tip = driver.find_elements_by_class_name("ext-mb-text")
            for i in v_tip:
                if u"成功" in i.text:
                    print(i.text)
                elif u"流程已触发" in i.text:
                    print(i.text)
                elif "凭证中物料不能为空" in i.text:
                    print(i.text)
                elif "行上数据不能为空" in i.text:
                    print(i.text)
                else:
                    print(i.text)
                    unittest.expectedFailure("test_2002_07_goto_delivery")
                    driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2002_07_goto_delivery.jpg")
        else:
            print("单据已清，不能复制到")

    '''销售管理-销售报价单-复制到-应收发票'''
    def test_2002_08_goto_accounts(self):
        """销售管理-销售报价单-新增单据功能"""
        driver = self.driver
        driver.find_element_by_id("btnLast").click()
        time.sleep(3)
        if driver.find_element_by_id("btnCopyTo").is_displayed():
            driver.find_element_by_id("btnCopyTo").click()
            time.sleep(1)
            driver.find_element_by_link_text("应收发票").click()
            time.sleep(5)
            driver.switch_to.parent_frame()
            driver.switch_to.frame("frame_tab_PM000200")
            # 排除自定义字段遮挡干扰
            ClasForm.form_field_hide(self)
            # 交货日期
            ClasForm.form_today(self, "dfDocDueDate")
            # 行数据列表
            v_lines = driver.find_element_by_xpath(
                "//*[@id='GridPanelItem']/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[3]"
            ).click()
            time.sleep(1)
            ActionChains(driver).context_click(v_lines).perform()
            time.sleep(1)
            driver.find_element_by_link_text("删除行").click()
            driver.find_element_by_id("btnSave").click()
            time.sleep(4)
            v_tip = driver.find_elements_by_class_name("ext-mb-text")
            for i in v_tip:
                if "成功，单号" in i.text:
                    print(i.text)
                elif "流程已触发" in i.text:
                    print(i.text)
                elif "行上数据不能为空" in i.text:
                    print(i.text)
                else:
                    print(i.text)
                    unittest.expectedFailure("test_2002_08_goto_accounts")
                    driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2002_08_goto_accounts.jpg")
        else:
            print("单据已清，不能复制到")

    '''销售管理-销售报价单-复制到-预留发票'''
    def test_2002_09_goto_reserved(self):
        """销售管理-销售报价单-新增单据功能"""
        driver = self.driver
        driver.find_element_by_id("btnLast").click()
        time.sleep(3)
        if driver.find_element_by_id("btnCopyTo").is_displayed():
            driver.find_element_by_id("btnCopyTo").click()
            time.sleep(1)
            driver.find_element_by_link_text("预留发票").click()
            time.sleep(4)
            driver.switch_to.parent_frame()
            driver.switch_to.frame("frame_tab_PM000223")
            # 排除自定义字段遮挡干扰
            ClasForm.form_field_hide(self)
            # 交货日期
            ClasForm.form_today(self, "dfDocDueDate")
            # 行数据列表
            v_lines = driver.find_element_by_xpath(
                "//*[@id='GridPanelItem']/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[3]"
            ).click()
            time.sleep(1)
            ActionChains(driver).context_click(v_lines).perform()
            time.sleep(1)
            driver.find_element_by_link_text("删除行").click()
            driver.find_element_by_id("btnSave").click()
            time.sleep(4)
            v_tip = driver.find_elements_by_class_name("ext-mb-text")
            for i in v_tip:
                if "成功，单号" in i.text:
                    print(i.text)
                elif "流程已触发" in i.text:
                    print(i.text)
                elif "凭证中物料不能为空" in i.text:
                    print(i.text)
                elif "行上数据不能为空" in i.text:
                    print(i.text)
                else:
                    print(i.text)
                    unittest.expectedFailure("test_2009_04_goto_reserved")
                    driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2009_04_goto_reserved.jpg")
        else:
            print("单据已清，不能复制到")

    '''销售管理-销售报价单-查询功能'''
    def test_2002_10_query(self):
        """销售管理-销售报价单-查询功能"""
        driver = self.driver
        driver.find_element_by_id("btnSearch").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")
        driver.find_element_by_id("gpSelect").click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(2)
        driver.switch_to.parent_frame()
        v_list = driver.find_elements_by_class_name("x-grid3-row")
        if len(v_list) > 0:
            print("单据查询数据正常显示")
        else:
            unittest.expectedFailure("test_2002_10_query")
            print("BUG-单据查询数据不正常")
            driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2002_10_query.jpg")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    unittest.main()