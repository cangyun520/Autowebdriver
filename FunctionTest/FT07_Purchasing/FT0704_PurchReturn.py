
from PubliCode.onlineClass import *
from PubliCode.randData import *
from selenium.webdriver.common.action_chains import ActionChains
import win32api


class PurchReturn(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_part_text(self, "采购管理", "采购退货")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000201")
        # 排除自定义字段遮挡干扰
        ClasForm.form_field_hide(self, driver)

    # 库存管理---采购退货
    def test_0704_01_add(self):
        """库存管理-采购退货-新增单据功能"""
        driver = self.driver
        driver.find_element_by_xpath("//*[@id='CompositeField2_Container']/div/div/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")     # 切换到业务伙伴选择窗体
        driver.find_element_by_id("txtSearchText").send_keys("V")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(2)
        driver.find_elements_by_class_name("x-grid3-row")[1].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        v_tim = time.strftime("%Y-%m-%d %H:%M:%S")
        driver.switch_to.parent_frame()
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
        time.sleep(1)
        driver.find_element_by_id("txtComments").send_keys("采购退货添加Auto" + v_tim)
        driver.find_element_by_id("btnSave").click()
        time.sleep(5)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功" in i.text:
                print(i.text)
            elif "流程已触发" in i.text:
                    print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_0702_01_Add.jpg")
                print(i.text)
                unittest.expectedFailure("test_0702_01_Add")

    # 库存管理-采购退货-业务伙伴编号为空穿透提示检查
    def test_0704_02_Client(self):
        """库存管理-采购退货-业务伙伴编号为空穿透提示检查"""
        driver = self.driver
        driver.find_element_by_id("btnGoOCRD").click()      # 业务伙伴主数据穿透
        time.sleep(2)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "业务伙伴为空" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_0704_02_Client.jpg")
                print(i.text)
                unittest.expectedFailure("test_0704_02_Client")

    # 库存管理-采购退货-业务伙伴主数据穿透功能
    def test_0704_03_last(self):
        """库存管理-采购退货-业务伙伴主数据穿透功能"""
        driver = self.driver
        driver.find_element_by_id("btnLast").click()
        time.sleep(3)
        driver.find_element_by_id("btnGoOCRD").click()      # 业务伙伴主数据穿透
        time.sleep(3)
        driver.switch_to.frame("winActivity_IFrame")     # 切换到业务伙伴主数据查看页面
        v_general = driver.find_element_by_link_text("常规")
        try:
            v_general.is_displayed()
            print("库存管理-采购退货穿透到伙伴主数据页面显示OK")
        except ImportError:
            driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_0704_03_last.jpg")
            unittest.expectedFailure("test_0704_03_last")

    # 库存管理-采购退货-单据复制到功能
    def test_0704_04_goto(self):
        """库存管理-采购退货-单据复制到功能"""
        driver = self.driver
        driver.find_element_by_id("btnLast").click()
        time.sleep(3)
        v_tim = time.strftime("%Y-%m-%d")
        try:
            driver.find_element_by_id("btnCopyTo").is_displayed()
            driver.find_element_by_id("btnCopyTo").click()
            time.sleep(1)
            driver.find_element_by_link_text("应付贷项凭证").click()
            time.sleep(4)
            driver.switch_to.default_content()
            ClasForm.form_top(self, 0)
            driver.switch_to.frame("frame_tab_PM000219")
            # 排除自定义字段遮挡干扰
            ClasForm.form_field_hide(self, driver)
            # 到期日
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
                    driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_0704_04_goto.jpg")
                    print(i.text)
                    unittest.expectedFailure("test_0704_04_goto")
        except ImportError:
            print("采购退货-单据已清，无复制到选项")

    # 采购管理-采购退货-单据复制功能
    def test_0704_06_copy(self):
        """采购管理-采购退货-单据复制功能"""
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
        driver.switch_to.frame("winAdd_IFrame")     # 切换到业务伙伴选择窗体
        driver.find_element_by_id("txtSearchText").send_keys("V")
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
                print(i.text)
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_0704_06_copy.jpg")
                unittest.expectedFailure("test_0704_06_copy")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(PurchReturn("test_0702_01_Add"))
    runner = unittest.TextTestRunner()
    runner.run(testsuit)