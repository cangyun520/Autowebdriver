
from PubliCode.onlineClass import *
from PubliCode.randData import *


class SalesReceive(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_part_text(self, "销售管理", "预收款申请")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000198")
        # 排除自定义字段遮挡干扰
        ClasForm.form_field_hide(self)

    """销售管理-预收款申请-新增单据功能"""
    def test_2004_01_Add(self):
        """销售管理-预收款申请-新增单据功能"""
        driver = self.driver
        driver.find_element_by_xpath("//*[@id='CompositeField2_Container']/div/div/div/span").click()
        time.sleep(4)
        driver.switch_to.frame("winAdd_IFrame")     # 切换到业务伙伴选择窗体
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
        driver.find_element_by_id("txtComments").send_keys("预收款申请添加Auto" + v_tim)
        # 付款方式
        driver.find_element_by_id("btnPayments").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='tfTrsfrAcct_Container']/div/span").click()
        time.sleep(2)
        driver.find_element_by_id("txtAccount").send_keys("人民币")
        driver.find_element_by_id("btnAccount").click()
        time.sleep(2)
        driver.find_elements_by_class_name("x-grid3-row")[-1].click()
        driver.find_element_by_id("Button13").click()
        time.sleep(2)
        driver.find_element_by_id("Button11111").click()
        time.sleep(2)
        driver.find_element_by_id("btnPaySave").click()
        time.sleep(2)
        driver.find_element_by_id("btnSave").click()
        time.sleep(5)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功" in i.text:
                print(i.text)
            elif "流程已触发" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2004_01_Add.jpg")
                print(i.text)
                unittest.expectedFailure("test_2004_01_Add")

    '''销售管理-预收款申请-客户编号为空穿透提示检查'''
    def test_2004_02_Client(self):
        """销售管理-预收款申请-客户编号为空穿透提示检查"""
        driver = self.driver
        driver.find_element_by_id("btnGoOCRD").click()      # 客户主数据穿透
        time.sleep(2)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "业务伙伴为空" in i.text:
                print("预收款申请-客户编号为空穿透提示检查OK")
            else:
                print("BUG  预收款申请-客户编号为空穿透提示检查OK异常")
                unittest.expectedFailure("test_2004_02_Client")
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2004_02_Client.jpg")

    '''销售管理-预收款申请-客户主数据穿透功能'''
    def test_2004_03_last(self):
        """销售管理-预收款申请-客户主数据穿透功能"""
        driver = self.driver
        driver.find_element_by_id("btnLast").click()
        time.sleep(3)
        driver.find_element_by_id("btnGoOCRD").click()      # 客户主数据穿透
        time.sleep(4)
        driver.switch_to.frame("winActivity_IFrame")     # 切换到业务伙伴主数据查看页面
        if driver.find_element_by_link_text("常规").is_displayed():
            print("销售管理-预收款申请穿透到业务伙伴主数据页面显示OK")
        else:
            print("BUG 销售管理-预收款申请穿透到业务伙伴主数据页面显示异常")
            unittest.expectedFailure("test_2004_03_last")
            driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2004_03_last.jpg")

    """销售管理-预收款申请-复制从-销售订单"""
    def test_2004_06_copyfrom(self):
        """销售管理---预收款申请-复制从-销售订单"""
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
        driver.switch_to.parent_frame()
        # 有效期至
        ClasForm.form_today(self, "dfDocDueDate")
        driver.find_element_by_id("btnCopyFrom").click()
        driver.find_element_by_link_text("销售订单").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")
        v_list = driver.find_elements_by_class_name("x-grid3-row")
        if len(v_list) > 0:
            v_list[0].click()
            driver.find_element_by_id("btnSelect").click()
            time.sleep(2)
            driver.switch_to.parent_frame()
            ClasForm.form_button_yes(self, "否")
            # 付款方式
            time.sleep(2)
            driver.switch_to.default_content()
            ClasForm.form_top(self, 0)
            driver.switch_to.frame("frame_tab_PM000198")
            driver.find_element_by_id("btnPayments").click()
            time.sleep(2)
            driver.find_element_by_xpath("//*[@id='tfTrsfrAcct_Container']/div/span").click()
            time.sleep(2)
            driver.find_element_by_id("txtAccount").send_keys("人民币")
            driver.find_element_by_id("btnAccount").click()
            time.sleep(2)
            driver.find_elements_by_class_name("x-grid3-row")[-1].click()
            driver.find_element_by_id("Button13").click()
            time.sleep(2)
            driver.find_element_by_id("Button11111").click()
            time.sleep(2)
            driver.find_element_by_id("btnPaySave").click()
            time.sleep(2)
            driver.find_element_by_id("btnSave").click()
            time.sleep(4)
            v_tip = driver.find_elements_by_class_name("ext-mb-text")
            for i in v_tip:
                if "成功" in i.text:
                    print(i.text)
                elif "流程已触发" in i.text:
                    print(i.text)
                else:
                    driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2004_01_Add.jpg")
                    print(i.text)
                    unittest.expectedFailure("test_2004_06_copyfrom")
        else:
            # 检查窗体是否一直处于加载假死中
            ClasForm.form_loading(self, "test_2004_06_copyfrom")
            print("复制从单据数据为空")

    """销售管理-预收款申请-复制从-销售报价单"""
    def test_2004_07_copyfrom(self):
        """销售管理-预收款申请-复制从-预收款申请"""
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
        driver.switch_to.parent_frame()
        # 有效期至
        ClasForm.form_today(self, "dfDocDueDate")
        driver.find_element_by_id("btnCopyFrom").click()
        driver.find_element_by_link_text("销售报价单").click()
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
                    driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2004_01_Add.jpg")
                    print(i.text)
                    unittest.expectedFailure("test_2004_07_copyfrom")
        else:
            # 检查窗体是否一直处于加载假死中
            ClasForm.form_loading(self, "test_2004_07_copyfrom")
            print("复制从单据数据为空")

    """销售管理-预收款申请-复制从-交货"""
    def test_2004_08_copyfrom(self):
        """销售管理-预收款申请-复制从-交货"""
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
        # 复制从
        driver.find_element_by_id("btnCopyFrom").click()
        driver.find_element_by_link_text("预收款申请").click()
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
                    driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2004_01_Add.jpg")
                    print(i.text)
                    unittest.expectedFailure("test_2004_08_copyfrom")
        else:
            # 检查窗体是否一直处于加载假死中
            ClasForm.form_loading(self, "test_2004_08_copyfrom")
            print("复制从单据数据为空")

    '''销售管理-预收款申请-查询功能'''
    def test_2004_09_query(self):
        """销售管理-预收款申请-查询功能"""
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
            unittest.expectedFailure("test_2004_09_query")
            print("BUG-单据查询数据不正常")
            driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2004_09_query.jpg")

    '''销售管理-预收款申请-点击【付款方式】'''
    def test_2004_10_clickPayment(self):
        """销售管理-预收款申请-点击【付款方式】"""
        driver = self.driver
        driver.find_element_by_id("btnPayments").click()
        time.sleep(2)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            try:
                "请选择客户" in i.text
            except Exception as err:
                print(err)
                unittest.expectedFailure("test_2004_10_clickPayment")
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2004_10_clickPayment.jpg")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    unittest.main()