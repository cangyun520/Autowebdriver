from PubliCode.config import *
from PubliCode.onlineClass import *
from PubliCode.randData import *
from selenium.webdriver.common.action_chains import ActionChains


class PurchReceive(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_part_text(self, "采购管理", "采购收货")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000197")
        # 排除自定义字段遮挡干扰
        ClasForm.form_field_hide(self)

    """库存管理-采购收货-新增单据功能"""
    def test_2106_01_add(self):
        """库存管理-采购收货-新增单据功能"""
        driver = self.driver
        driver.find_element_by_xpath("//*[@id='CompositeField2_Container']/div/div/div/span").click()
        time.sleep(3)
        # 切换到业务伙伴选择窗体
        driver.switch_to.frame("winAdd_IFrame")
        driver.find_element_by_id("txtSearchText").send_keys("V")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(2)
        driver.find_elements_by_class_name("x-grid3-row")[1].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        v_tim = time.strftime("%Y-%m-%d %H:%M:%S")
        driver.switch_to.default_content()
        driver.switch_to.frame("frame_tab_PM000197")
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
        driver.switch_to.default_content()
        ClasForm.form_top(self, 0)
        time.sleep(1)
        driver.switch_to.frame("frame_tab_PM000197")
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功" in i.text:
                print(i.text)
            elif "流程已触发" in i.text:
                    print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2106_01_add.jpg")
                print(i.text)
                unittest.expectedFailure("test_2106_01_add")

    """库存管理-采购收货-业务伙伴编号为空穿透提示检查"""
    def test_2106_02_client(self):
        """库存管理-采购收货-业务伙伴编号为空穿透提示检查"""
        driver = self.driver
        # 业务伙伴主数据穿透
        driver.find_element_by_id("btnGoOCRD").click()
        time.sleep(2)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "业务伙伴为空" in i.text:
                print("采购收货-业务伙伴编号为空穿透提示检查OK")
            else:
                print("BUG  采购收货-业务伙伴编号为空穿透提示检查异常")
                unittest.expectedFailure("test_2106_02_client")

    """库存管理-采购收货-业务伙伴主数据穿透功能"""
    def test_2106_03_First(self):
        """库存管理-采购收货-业务伙伴主数据穿透功能"""
        driver = self.driver
        driver.find_element_by_id("btnFirst").click()
        time.sleep(3)
        # 业务伙伴主数据穿透
        driver.find_element_by_id("btnGoOCRD").click()
        time.sleep(3)
        # 切换到业务伙伴主数据查看页面
        driver.switch_to.frame("winActivity_IFrame")
        v_general = driver.find_element_by_link_text("常规")
        try:
            v_general.is_displayed()
            print("库存管理-采购收货穿透到伙伴主数据页面显示OK")
        except ImportError:
            print("BUG 库存管理-采购收货穿透到伙伴主数据页面显示异常")
            unittest.expectedFailure("test_2106_03_First")

    """库存管理-采购收货-复制到-退货"""
    def test_2106_07_goto_return(self):
        """库存管理-采购收货-复制到-退货"""
        driver = self.driver
        driver.find_element_by_id("btnLast").click()
        time.sleep(3)
        v_tim = time.strftime("%Y-%m-%d")
        try:
            driver.find_element_by_id("btnCopyTo").is_displayed()
            driver.find_element_by_id("btnCopyTo").click()
            time.sleep(1)
            driver.find_element_by_link_text("退货").click()
            time.sleep(4)
            driver.switch_to.parent_frame()
            ClasForm.form_top(self, 0)
            driver.switch_to.frame("frame_tab_PM000201")
            # 排除自定义字段遮挡干扰
            ClasForm.form_field_hide(self)
            # 退货日期
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
                    driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2106_07_goto_return.jpg")
                    print(i.text)
                    unittest.expectedFailure("test_2106_07_goto_return")
        except ImportError:
            print("采购收货-单据已清，无复制到选项")

    """采购管理-采购收货-目标凭证查看"""
    def test_2106_05_target(self):
        """采购管理-采购收货-目标凭证查看"""
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
            
    """采购管理-采购收货-单据复制功能"""
    def test_2106_06_copy(self):
        """采购管理-采购收货-单据复制功能"""
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
        driver.find_element_by_xpath("//*[@id='CompositeField2_Container']/div/div/div/span").click()
        time.sleep(3)
        # 切换到业务伙伴选择窗体
        driver.switch_to.frame("winAdd_IFrame")
        driver.find_element_by_id("txtSearchText").send_keys("V")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(2)
        driver.find_elements_by_class_name("x-grid3-row")[1].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(2)
        driver.switch_to.default_content()
        driver.switch_to.frame("frame_tab_PM000197")
        # 是否依据新的业务伙伴数据更新凭证行
        ClasForm.form_button_yes(self, "是")
        ClasForm.form_today(self, "dfDocDueDate")
        # 备注
        driver.find_element_by_id("txtComments").send_keys("单据复制添加Auto" + v_tim)
        driver.find_element_by_id("btnSave").click()
        time.sleep(6)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功" in i.text:
                print(i.text)
            elif "流程已触发" in i.text:
                print(i.text)
            else:
                print(i.text)
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2106_06_copy.jpg")
                unittest.expectedFailure("test_2106_06_copy")

    """库存管理-采购收货-复制到-应付发票"""
    def test_2106_07_goto(self):
        """库存管理-采购收货-复制到-应付发票"""
        driver = self.driver
        driver.find_element_by_id("btnLast").click()
        time.sleep(3)
        try:
            driver.find_element_by_id("btnCopyTo").is_displayed()
            driver.find_element_by_id("btnCopyTo").click()
            time.sleep(1)
            driver.find_element_by_link_text("应付发票").click()
            time.sleep(4)
            driver.switch_to.parent_frame()
            ClasForm.form_top(self, 0)
            driver.switch_to.frame("frame_tab_PM000215")
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
                elif "行上数据不能为空" in i.text:
                    print(i.text)
                else:
                    driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2106_07_goto.jpg")
                    print(i.text)
                    unittest.expectedFailure("test_2106_07_goto")
        except ImportError:
            print("采购收货-单据已清，无复制到选项")

    """采购管理-采购收货-复制从-退货"""
    def test_2106_08_copyfrom(self):
        """采购管理-采购收货-复制从-退货"""
        driver = self.driver
        driver.find_element_by_xpath("//*[@id='CompositeField2_Container']/div/div/div/span").click()
        time.sleep(3)
        # 切换到业务伙伴选择窗体
        driver.switch_to.frame("winAdd_IFrame")
        driver.find_element_by_id("txtSearchText").send_keys("V")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(2)
        driver.find_elements_by_class_name("x-grid3-row")[1].click()
        driver.find_element_by_id("btnSelect").click()
        driver.switch_to.parent_frame()
        time.sleep(1)
        ClasForm.form_today(self, "dfDocDueDate")
        # 复制从
        driver.find_element_by_id("btnCopyFrom").click()
        driver.find_element_by_link_text("退货").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")
        v_list = driver.find_elements_by_class_name("x-grid3-row")
        if len(v_list) > 0:
            v_list[0].click()
            driver.find_element_by_id("btnSelect").click()
            time.sleep(3)
            driver.switch_to.parent_frame()
            ClasForm.form_button_yes(self, "否")
            time.sleep(3)
            driver.find_element_by_id("btnSave").click()
            time.sleep(5)
            v_tip = driver.find_elements_by_class_name("ext-mb-text")
            for i in v_tip:
                if "成功" in i.text:
                    print(i.text)
                elif "流程已触发" in i.text:
                    print(i.text)
                elif "数量降为负库存" in i.text:
                    print(i.text)
                else:
                    driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2106_08_copyfrom.jpg")
                    print(i.text)
                    unittest.expectedFailure("test_2106_08_copyfrom")
        else:
            # 检查窗体是否一直处于加载假死中
            ClasForm.form_loading(self, "test_2106_08_copyfrom")
            print("复制从单据数据为空")

    """采购管理-采购收货-复制从-采购报价单"""
    def test_2106_09_copyfrom(self):
        """采购管理-采购收货-复制从-采购报价单"""
        driver = self.driver
        driver.find_element_by_xpath("//*[@id='CompositeField2_Container']/div/div/div/span").click()
        time.sleep(3)
        # 切换到业务伙伴选择窗体
        driver.switch_to.frame("winAdd_IFrame")
        driver.find_element_by_id("txtSearchText").send_keys("V")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(2)
        driver.find_elements_by_class_name("x-grid3-row")[1].click()
        driver.find_element_by_id("btnSelect").click()
        driver.switch_to.parent_frame()
        time.sleep(1)
        ClasForm.form_today(self, "dfDocDueDate")
        time.sleep(1)
        # 复制从
        driver.find_element_by_id("btnCopyFrom").click()
        driver.find_element_by_link_text("采购报价单").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")
        v_list = driver.find_elements_by_class_name("x-grid3-row")
        if len(v_list) > 0:
            v_list[0].click()
            driver.find_element_by_id("btnSelect").click()
            time.sleep(3)
            driver.switch_to.parent_frame()
            ClasForm.form_button_yes(self, "否")
            time.sleep(3)
            driver.find_element_by_id("btnSave").click()
            time.sleep(5)
            v_tip = driver.find_elements_by_class_name("ext-mb-text")
            for i in v_tip:
                if "成功" in i.text:
                    print(i.text)
                elif "流程已触发" in i.text:
                    print(i.text)
                elif "数量降为负库存" in i.text:
                    print(i.text)
                else:
                    driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2106_09_copyfrom.jpg")
                    print(i.text)
                    unittest.expectedFailure("test_2106_09_copyfrom")
        else:
            # 检查窗体是否一直处于加载假死中
            ClasForm.form_loading(self, "test_2106_09_copyfrom")
            print("复制从单据数据为空")

    """采购管理-采购收货-复制从-采购订单"""
    def test_2106_10_copyfrom(self):
        """采购管理-采购收货-复制从-采购订单"""
        driver = self.driver
        driver.find_element_by_xpath("//*[@id='CompositeField2_Container']/div/div/div/span").click()
        time.sleep(3)
        # 切换到业务伙伴选择窗体
        driver.switch_to.frame("winAdd_IFrame")
        driver.find_element_by_id("txtSearchText").send_keys("V")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(2)
        driver.find_elements_by_class_name("x-grid3-row")[1].click()
        driver.find_element_by_id("btnSelect").click()
        driver.switch_to.parent_frame()
        time.sleep(1)
        ClasForm.form_today(self, "dfDocDueDate")
        time.sleep(1)
        # 复制从
        driver.find_element_by_id("btnCopyFrom").click()
        driver.find_element_by_link_text("采购订单").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")
        v_list = driver.find_elements_by_class_name("x-grid3-row")
        if len(v_list) > 0:
            v_list[0].click()
            driver.find_element_by_id("btnSelect").click()
            time.sleep(3)
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
                elif "数量降为负库存" in i.text:
                    print(i.text)
                else:
                    driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2106_10_copyfrom.jpg")
                    print(i.text)
                    unittest.expectedFailure("test_2106_10_copyfrom")
        else:
            # 检查窗体是否一直处于加载假死中
            ClasForm.form_loading(self, "test_2106_10_copyfrom")
            print("复制从单据数据为空")

    '''采购管理-采购收货-查询功能'''
    def test_2106_11_query(self):
        """采购管理-采购收货-查询功能"""
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
            unittest.expectedFailure("test_2106_11_query")
            print("BUG-单据查询数据不正常")
            driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2106_11_query.jpg")

    """采购管理-采购收货-复制从-预留发票"""
    def test_2106_12_copyfrom(self):
        """采购管理-采购收货-复制从-预留发票"""
        driver = self.driver
        driver.find_element_by_xpath("//*[@id='CompositeField2_Container']/div/div/div/span").click()
        time.sleep(3)
        # 切换到业务伙伴选择窗体
        driver.switch_to.frame("winAdd_IFrame")
        driver.find_element_by_id("txtSearchText").send_keys("V")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(2)
        driver.find_elements_by_class_name("x-grid3-row")[1].click()
        driver.find_element_by_id("btnSelect").click()
        driver.switch_to.parent_frame()
        time.sleep(1)
        ClasForm.form_today(self, "dfDocDueDate")
        time.sleep(1)
        # 复制从
        driver.find_element_by_id("btnCopyFrom").click()
        driver.find_element_by_link_text("预留发票").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")
        v_list = driver.find_elements_by_class_name("x-grid3-row")
        if len(v_list) > 0:
            v_list[0].click()
            driver.find_element_by_id("btnSelect").click()
            time.sleep(3)
            driver.switch_to.parent_frame()
            ClasForm.form_button_yes(self, "否")
            driver.find_element_by_id("btnSave").click()
            time.sleep(7)
            v_tip = driver.find_elements_by_class_name("ext-mb-text")
            for i in v_tip:
                if "成功" in i.text:
                    print(i.text)
                elif "流程已触发" in i.text:
                    print(i.text)
                elif "数量降为负库存" in i.text:
                    print(i.text)
                else:
                    driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2106_12_copyfrom.jpg")
                    print(i.text)
                    unittest.expectedFailure("test_2106_12_copyfrom")
        else:
            # 检查窗体是否一直处于加载假死中
            ClasForm.form_loading(self, "test_2106_12_copyfrom")
            print("复制从单据数据为空")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()