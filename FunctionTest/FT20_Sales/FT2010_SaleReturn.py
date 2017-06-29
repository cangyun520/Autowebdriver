
from PubliCode.onlineClass import *
from PubliCode.randData import *
from selenium.webdriver.common.action_chains import ActionChains


class SaleReturn(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_part_text(self, "销售管理", "销售退货")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000195")
        # 排除自定义字段遮挡干扰
        ClasForm.form_field_hide(self)

    '''销售管理-销售退货-新增单据功能'''
    def test_2010_01_add(self):
        """销售管理-销售退货-新增单据功能"""
        driver = self.driver
        driver.find_element_by_xpath("//*[@id='CompositeField2_Container']/div/div/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")     # 切换到业务伙伴选择窗体
        driver.find_element_by_id("txtSearchText").send_keys("C")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(2)
        driver.find_elements_by_class_name("x-grid3-row")[1].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        v_tim = time.strftime("%Y-%m-%d %H:%M:%S")
        driver.switch_to.default_content()
        driver.switch_to.frame("frame_tab_PM000195")
        driver.find_element_by_xpath(
            "//*[@id='GridPanelItem']/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath(
            "//*[@id='GridPanelItem']/div/div/div/div/div[2]/div[2]/div/span").click()
        time.sleep(2)
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
        driver.find_element_by_id("txtComments").send_keys("销售退货添加Auto" + v_tim)
        driver.find_element_by_id("btnSave").click()
        time.sleep(5)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2010_01_add.jpg")
                print(i.text)
                unittest.expectedFailure("test_2010_01_add")

    '''销售退货-业务伙伴编号为空穿透提示检查'''
    def test_2010_02_client(self):
        """销售退货-业务伙伴编号为空穿透提示检查"""
        driver = self.driver
        driver.find_element_by_id("btnGoOCRD").click()      # 业务伙伴主数据穿透
        time.sleep(2)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "业务伙伴为空" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2010_02_client.jpg")
                print(i.text)
                unittest.expectedFailure("test_2010_02_client")

    '''销售退货-伙伴主数据穿透功能'''
    def test_2010_03_First(self):
        """销售退货-业务伙伴主数据穿透功能"""
        driver = self.driver
        driver.find_element_by_id("btnFirst").click()
        time.sleep(3)
        driver.find_element_by_id("btnGoOCRD").click()      # 业务伙伴主数据穿透
        time.sleep(3)
        driver.switch_to.frame("winActivity_IFrame")     # 切换到业务伙伴主数据查看页面
        v_general = driver.find_element_by_link_text("常规")
        try:
            v_general.is_displayed()
            print("销售退货穿透到伙伴主数据页面显示OK")
        except ImportError:
            driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2010_03_First.jpg")
            unittest.expectedFailure("test_2010_03_First")

    '''销售退货-复制到-交货'''
    def test_2010_04_goto_delivery(self):
        """销售退货-复制到-交货"""
        driver = self.driver
        driver.find_element_by_id("btnLast").click()
        time.sleep(3)
        try:
            driver.find_element_by_id("btnCopyTo").is_displayed()
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
            driver.find_element_by_id("btnSave").click()
            time.sleep(5)
            v_tip = driver.find_elements_by_class_name("ext-mb-text")
            for i in v_tip:
                if "成功，单号" in i.text:
                    print(i.text)
                elif "流程已触发" in i.text:
                    print(i.text)
                else:
                    driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2010_04_goto_delivery.jpg")
                    print(i.text)
                    unittest.expectedFailure("test_2010_04_goto_delivery")
        except ImportError:
            print("销售退货-单据已清，无复制到选项")

    '''销售管理-销售退货-目标凭证查看'''
    def test_2010_05_target(self):
        """销售管理-销售退货-目标凭证查看"""
        driver = self.driver
        driver.find_element_by_id("btnLast").click()
        time.sleep(4)
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

    '''销售管理-销售退货-复制'''
    def test_2010_06_copy(self):
        """销售管理-销售退货-单据复制功能"""
        driver = self.driver
        driver.find_element_by_id("btnPrevious").click()
        time.sleep(3)
        v_object = driver.find_element_by_id("btnGoOCRD")
        ActionChains(driver).context_click(v_object).perform()
        time.sleep(1)
        driver.find_element_by_id("MenuCopy").click()
        time.sleep(3)
        v_tim = time.strftime("%Y-%m-%d %H:%M:%S")
        # 选择客户
        driver.find_element_by_xpath("//*[@id='CompositeField2_Container']/div/div/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")     # 切换到业务伙伴选择窗体
        driver.find_element_by_id("txtSearchText").send_keys("C")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(2)
        driver.find_elements_by_class_name("x-grid3-row")[1].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(2)
        driver.switch_to.default_content()
        driver.switch_to.frame("frame_tab_PM000195")
        # 是否依据新的业务伙伴数据更新凭证行
        ClasForm.form_button_yes(self, "是")
        # 备注
        driver.find_element_by_id("txtComments").send_keys("单据复制添加Auto" + v_tim)
        time.sleep(1)
        driver.find_element_by_id("btnSave").click()
        time.sleep(7)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功" in i.text:
                print(i.text)
            elif "流程已触发" in i.text:
                print(i.text)
            else:
                print(i.text)
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2010_06_copy.jpg")
                unittest.expectedFailure("test_2010_06_copy")

    '''销售退货-复制到-应收贷项凭证'''
    def test_2010_07_goto_credit(self):
        """销售退货-复制到-应收贷项凭证"""
        driver = self.driver
        driver.find_element_by_id("btnLast").click()
        time.sleep(3)
        if driver.find_element_by_id("btnCopyTo").is_displayed():
            driver.find_element_by_id("btnCopyTo").click()
            time.sleep(1)
            driver.find_element_by_link_text("应收贷项凭证").click()
            time.sleep(4)
            driver.switch_to.parent_frame()
            ClasForm.form_top(self, 0)
            driver.switch_to.frame("frame_tab_PM000196")
            # 排除自定义字段遮挡干扰
            ClasForm.form_field_hide(self)
            # 有效期至
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
            time.sleep(5)
            v_tip = driver.find_elements_by_class_name("ext-mb-text")
            for i in v_tip:
                if "成功，单号" in i.text:
                    print(i.text)
                elif "流程已触发" in i.text:
                    print(i.text)
                else:
                    driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2010_07_goto_credit.jpg")
                    print(i.text)
                    unittest.expectedFailure("test_2010_07_goto_credit")
        else:
            print("销售退货-单据已清，无复制到选项")

    """销售管理-销售退货-复制从-交货"""
    def test_2010_08_copyfrom(self):
        """销售管理-销售退货-复制从-交货"""
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
        driver.switch_to.parent_frame()
        # 有效期至
        ClasForm.form_today(self, "dfDocDueDate")
        driver.find_element_by_id("btnCopyFrom").click()
        driver.find_element_by_link_text("交货").click()
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
            time.sleep(6)
            v_tip = driver.find_elements_by_class_name("ext-mb-text")
            for i in v_tip:
                if "成功" in i.text:
                    print(i.text)
                elif "流程已触发" in i.text:
                    print(i.text)
                elif "数量降为负库存" in i.text:
                    print(i.text)
                else:
                    driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2004_01_Add.jpg")
                    print(i.text)
                    unittest.expectedFailure("test_2010_08_copyfrom")
        else:
            # 检查窗体是否一直处于加载假死中
            ClasForm.form_loading(self, "test_2010_08_copyfrom")
            print("复制从单据数据为空")

    '''销售管理-销售退货-查询功能'''
    def test_2010_09_query(self):
        """销售管理-销售退货-查询功能"""
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
            unittest.expectedFailure("test_2010_09_query")
            print("BUG-单据查询数据不正常")
            driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2010_09_query.jpg")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()