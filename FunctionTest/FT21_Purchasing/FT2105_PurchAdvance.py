from PubliCode.config import *
from PubliCode.onlineClass import *
from PubliCode.randData import *


class PurchAdvance(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_part_text(self, "采购管理", "采购预付款申请")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000218")
        # 排除自定义字段遮挡干扰
        ClasForm.form_field_hide(self)

    """采购管理-采购预付款申请-新增单据功能检查"""
    def test_2105_01_Add(self):
        """采购管理-采购预付款申请-新增单据功能检查"""
        driver = self.driver
        driver.find_element_by_xpath("//*[@id='CompositeField2_Container']/div/div/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")
        # 切换到业务伙伴选择窗体
        driver.find_element_by_id("gpSelect").click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        driver.switch_to.parent_frame()
        v_tim = time.strftime("%Y-%m-%d %H:%M:%S")
        # 有效期至
        ClasForm.form_today(self, "dfDocDueDate")
        driver.find_element_by_xpath(
            "//*[@id='GridPanelItem']/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath(
            "//*[@id='GridPanelItem']/div/div/div/div/div[2]/div[2]/div/span").click()
        time.sleep(2)
        driver.switch_to.frame("winAdd_IFrame")
        # 切换到物料选择窗体
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
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2105_01_Add.jpg")
                print(i.text)
                unittest.expectedFailure("test_2105_01_Add")

    """采购管理-采购预付款申请-业务伙伴编号为空穿透提示检查"""
    def test_2105_02_Client(self):
        """采购管理-采购预付款申请-业务伙伴编号为空穿透提示检查"""
        driver = self.driver
        driver.find_element_by_id("btnGoOCRD").click()
        # 业务伙伴主数据穿透
        time.sleep(2)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "业务伙伴为空" in i.text:
                print(i.text)
            else:
                print(i.text)
                unittest.expectedFailure("test_2105_02_Client")

    """采购管理-采购预付款申请-业务伙伴主数据穿透功能检查"""
    def test_2105_03_First(self):
        """采购管理-采购预付款申请-业务伙伴主数据穿透功能检查"""
        driver = self.driver
        driver.find_element_by_id("btnFirst").click()
        time.sleep(4)
        driver.find_element_by_id("btnGoOCRD").click()
        # 业务伙伴主数据穿透
        time.sleep(3)
        driver.switch_to.frame("winActivity_IFrame")
        # 切换到业务伙伴主数据查看页面
        v_general = driver.find_element_by_link_text("常规")
        try:
            v_general.is_displayed()
            print("采购管理-采购预付款申请穿透到伙伴主数据页面显示OK")
        except ImportError:
            print("BUG 采购管理-采购预付款申请穿透到伙伴主数据页面显示异常")
            unittest.expectedFailure("test_2105_03_First")

    """采购管理-采购预付款申请-复制从-采购报价单"""
    def test_2105_04_copyfrom(self):
        """采购管理-采购预付款申请-复制从-采购报价单"""
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
            driver.switch_to.parent_frame()
            time.sleep(1)
            ClasForm.form_button_yes(self, "否")
            time.sleep(4)
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
                    driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2105_04_copyfrom.jpg")
                    print(i.text)
                    unittest.expectedFailure("test_2105_04_copyfrom")
        else:
            # 检查窗体是否一直处于加载假死中
            ClasForm.form_loading(self, "test_2105_04_copyfrom")
            print("复制从单据数据为空")

    """采购管理-采购预付款申请-复制从-采购订单"""
    def test_2105_05_copyfrom(self):
        """采购管理-采购预付款申请-复制从-采购订单"""
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
            driver.switch_to.parent_frame()
            time.sleep(1)
            ClasForm.form_button_yes(self, "否")
            time.sleep(4)
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
                    driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2105_05_copyfrom.jpg")
                    print(i.text)
                    unittest.expectedFailure("test_2105_05_copyfrom")
        else:
            # 检查窗体是否一直处于加载假死中
            ClasForm.form_loading(self, "test_2105_05_copyfrom")
            print("复制从单据数据为空")

    """采购管理-采购预付款申请-复制从-收货采购订单"""
    def test_2105_06_copyfrom(self):
        """采购管理-采购预付款申请-复制从-收货采购订单"""
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
        driver.find_element_by_link_text("收货采购订单").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")
        v_list = driver.find_elements_by_class_name("x-grid3-row")
        if len(v_list) > 0:
            v_list[0].click()
            driver.find_element_by_id("btnSelect").click()
            driver.switch_to.parent_frame()
            time.sleep(1)
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
                    driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2105_06_copyfrom.jpg")
                    print(i.text)
                    unittest.expectedFailure("test_2105_06_copyfrom")
        else:
            # 检查窗体是否一直处于加载假死中
            ClasForm.form_loading(self, "test_2105_06_copyfrom")
            print("复制从单据数据为空")

    '''采购管理-采购预付款申请-查询功能'''
    def test_2105_07_query(self):
        """采购管理-采购预付款申请-查询功能"""
        driver = self.driver
        driver.find_element_by_id("btnSearch").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")
        v_list = driver.find_elements_by_class_name("x-grid3-row")
        if len(v_list) > 0:
            v_list[0].click()
            driver.find_element_by_id("btnSelect").click()
            time.sleep(2)
            driver.switch_to.parent_frame()
            v_list = driver.find_elements_by_class_name("x-grid3-row")
            if len(v_list) > 0:
                print("单据查询数据正常显示")
            else:
                unittest.expectedFailure("test_2007_06_query")
                print("BUG-单据查询数据不正常")
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2007_06_query.jpg")
        else:
            print("查询弹出窗体数据为空")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    unittest.main()