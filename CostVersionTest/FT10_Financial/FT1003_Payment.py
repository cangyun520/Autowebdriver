
from selenium.webdriver.common.action_chains import ActionChains
from PubliCode.onlineClass import *
from PubliCode.randData import *
import sys


class Payment(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "财务管理", "费用付款")
        driver.switch_to.frame("frame_tab_PM000786")
        v_tim = time.strftime("%y%m%d%H%M")

    """财务管理-费用付款-单据添加"""
    def test_1003_01_add(self):
        """财务管理-费用付款-单据添加功能"""
        driver = self.driver
        driver.find_element_by_id("btnAdd").click()
        time.sleep(3)
        # 切换到新增页面
        driver.switch_to.frame("winActivity_IFrame")
        # 费用明细信息（借）页签
        v_object = driver.find_element_by_id("gpPaymentCost")
        ActionChains(driver).context_click(v_object).perform()
        driver.find_element_by_link_text("添加行").click()
        time.sleep(1)
        # 选择借款单号
        v_num = driver.find_element_by_xpath(
            "//*[@id='gpPaymentCost']/div/div/div/div/div[2]/div/div/table/tbody/tr/td[4]")
        ActionChains(driver).double_click(v_num).perform()
        driver.find_element_by_xpath(
            "//*[@id='gpPaymentCost']/div/div/div/div/div[2]/div[2]/div/span").click()
        time.sleep(2)
        # 进入源单据选择窗体
        driver.switch_to.frame("winAdd_IFrame")
        v_list_borrow = driver.find_elements_by_class_name("x-grid3-row")
        if len(v_list_borrow) > 0:
            v_list_borrow[0].click()
            driver.find_element_by_id("btnSelect").click()
            time.sleep(1)
            driver.switch_to.parent_frame()
            # 付款方式页（贷）签
            driver.find_element_by_id("TabPanel1__gpPaymentListLines").click()
            time.sleep(1)
            v_object = driver.find_element_by_id("gpPaymentListLines")
            ActionChains(driver).context_click(v_object).perform()
            driver.find_element_by_link_text("添加行").click()
            time.sleep(1)
            # 选择科目
            v_course = driver.find_element_by_xpath(
                "//*[@id='gpPaymentListLines']/div/div/div/div/div[2]/div/div/table/tbody/tr/td[3]")
            ActionChains(driver).double_click(v_course).perform()
            driver.find_element_by_xpath(
                "//*[@id='gpPaymentListLines']/div/div/div/div/div[2]/div[2]/div/span").click()
            time.sleep(2)
            # 进入科目选择窗体
            driver.switch_to.frame("winAdd_IFrame")
            driver.find_element_by_id("txtBPartners").send_keys("人民币")
            driver.find_element_by_id("btnBPartners").click()
            time.sleep(1)
            driver.find_elements_by_class_name("x-grid3-row")[0].click()
            driver.find_element_by_id("Button1").click()
            time.sleep(1)
            driver.switch_to.parent_frame()
            # 调用自由流审批人选择函数
            ClasFlow.flow_free(self, "bear")
            driver.find_element_by_id("btnWorkflow").click()
            time.sleep(4)
            v_tip = driver.find_elements_by_class_name("ext-mb-text")
            for i in v_tip:
                if "流程已触发" in i.text:
                    print(i.text)
                elif "成功" in i.text:
                    print(i.text)
                else:
                    driver.get_screenshot_as_file(root_path() + "TestPicture/test_1003_01_add.jpg")
                    print(i.text)
                    unittest.expectedFailure("test_1003_01_add")
        else:
            print("借款单无，不能费用付款")

    """财务管理-费用付款-添加界面关闭功能"""
    def test_1003_02_look(self):
        """财务管理-费用付款-添加界面关闭功能"""
        driver = self.driver
        # 随机双击行数据进入到查看界面
        v_list = driver.find_elements_by_class_name("x-grid3-row")
        # 如果行列表无数据时则通过点击添加进入到页面
        if len(v_list) == 0:
            driver.find_element_by_id("BtnAdd").click()
        else:
            ActionChains(driver).double_click(v_list[random.randint(0, len(v_list)-1)]).perform()
        time.sleep(3)
        # 切换到新增页面
        driver.switch_to.frame("winActivity_IFrame")
        driver.find_element_by_id("btnCancel").click()
        time.sleep(2)
        ClasForm.form_button_yes(self, "是")
        time.sleep(1)
        driver.switch_to.parent_frame()
        if driver.find_element_by_id("ComboBox5").is_displayed():
            print("财务管理-费用付款-查看界面关闭功能OK")
        else:
            unittest.expectedFailure("test_1003_02")

    """财务管理-费用付款-源单据为空查看"""
    def test_1003_03_noSource(self):
        """财务管理-费用付款-单据添加功能"""
        driver = self.driver
        driver.find_element_by_id("btnAdd").click()
        time.sleep(3)
        # 切换到新增页面
        driver.switch_to.frame("winActivity_IFrame")
        # 费用明细信息（借）页签
        v_object = driver.find_element_by_id("gpPaymentCost")
        ActionChains(driver).context_click(v_object).perform()
        driver.find_element_by_link_text("添加行").click()
        time.sleep(1)
        v_button = driver.find_elements_by_tag_name("button")
        for i in v_button:
            if i.text == "查看源单据":
                i.click()
                break
            time.sleep(1)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "找不到对应的源单据" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/1003_03_noSource.jpg")
                print(i.text)
                unittest.expectedFailure("1003_03_noSource")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(Payment("test_0604_01_add"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)