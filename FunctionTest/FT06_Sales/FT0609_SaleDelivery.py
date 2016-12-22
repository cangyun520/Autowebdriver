
from PubliCode.onlineClass import *
from PubliCode.randData import *
from selenium.webdriver.common.action_chains import ActionChains
import win32api


class SaleDelivery(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        ClasLogin.login_setup(self)
        # 打开菜单
        ClasMenu.menu_part_text(self, "销售管理", "销售交货")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000194")
        # 排除自定义字段遮挡干扰
        ClasForm.form_field_hide(self, driver)

    # 销售管理-库存管理---销售交货
    def test_0609_01_Add(self):
        """销售管理-销售交货-新增单据功能"""
        driver = self.driver
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
        driver.find_element_by_xpath(
            "//*[@id='GridPanelItem']/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath(
            "//*[@id='GridPanelItem']/div/div/div/div/div[2]/div[2]/div/span").click()
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
            if "成功" in i.text:
                print(i.text)
            elif "流程已触发" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_0609_01_Add.jpg")
                print(i.text)
                unittest.expectedFailure("test_0609_01_Add")

    # 销售交货-业务伙伴编号为空穿透提示检查
    def test_0609_02_Client(self):
        """销售管理-销售交货-业务伙伴编号为空穿透提示检查"""
        driver = self.driver
        driver.find_element_by_id("btnGoOCRD").click()      # 业务伙伴主数据穿透
        time.sleep(2)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "业务伙伴为空" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_0609_02_Client.jpg")
                print(i.text)
                unittest.expectedFailure("test_0609_02_Client")

    # 销售交货-伙伴主数据穿透功能
    def test_0609_03_First(self):
        """销售管理-销售交货-业务伙伴主数据穿透功能"""
        driver = self.driver
        driver.find_element_by_id("btnFirst").click()
        time.sleep(3)
        driver.find_element_by_id("btnGoOCRD").click()      # 业务伙伴主数据穿透
        time.sleep(3)
        driver.switch_to_frame("winActivity_IFrame")     # 切换到业务伙伴主数据查看页面
        v_general = driver.find_element_by_link_text("常规")
        try:
            v_general.is_displayed()
            print("库存管理-销售交货穿透到伙伴主数据页面显示OK")
        except ImportError:
            driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_0609_03_First.jpg")
            unittest.expectedFailure("test_0609_03_First")

    # 销售交货-单据复制到功能
    def test_0609_04_goto(self):
        """销售管理-销售交货-单据复制到功能"""
        driver = self.driver
        driver.find_element_by_id("btnLast").click()
        time.sleep(3)
        v_tim = time.strftime("%Y-%m-%d")
        try:
            driver.find_element_by_id("btnCopyTo").is_displayed()
            driver.find_element_by_id("btnCopyTo").click()
            time.sleep(1)
            v_wlcode = ("退货", "应收发票")
            v_checked = v_wlcode[random.randint(0, 1)]
            driver.find_element_by_link_text(v_checked).click()
            time.sleep(4)
            driver.switch_to.parent_frame()
            # print(v_checked)
            if v_checked == "退货":
                ClasForm.form_top(self, 0)
                driver.switch_to_frame("frame_tab_PM000195")
                # 排除自定义字段遮挡干扰
                ClasForm.form_field_hide(self, driver)
                # 有效期至
                ClasForm.form_today(self, "dfDocDueDate")
            else:
                ClasForm.form_top(self, 0)
                driver.switch_to_frame("frame_tab_PM000200")
                # 排除自定义字段遮挡干扰
                ClasForm.form_field_hide(self, driver)
                # 有效期至
                ClasForm.form_today(self, "dfDocDueDate")
            driver.find_element_by_id("btnSave").click()
            time.sleep(5)
            v_tip = driver.find_elements_by_class_name("ext-mb-text")
            for i in v_tip:
                if "成功，单号" in i.text:
                    print(i.text + v_checked)
                elif "流程已触发" in i.text:
                    print(i.text + v_checked)
                else:
                    driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_0609_04_goto.jpg")
                    print(i.text)
                    unittest.expectedFailure("test_0609_04_goto")
        except ImportError:
            print("销售交货-单据已清，无复制到选项")

    # 销售管理-销售交货-目标凭证查看
    def test_0609_05_target(self):
        """销售管理-销售交货-目标凭证查看"""
        driver = self.driver
        driver.find_element_by_id("btnLast").click()
        time.sleep(4)
        if driver.find_element_by_id("btnTarget").is_displayed():
            driver.find_element_by_id("btnTarget").click()
            time.sleep(3)
            driver.switch_to_default_content()
            v_active = driver.find_element_by_class_name("active")        # 获取对象
            # print(v_active.text)
            v_active_id = v_active.get_attribute("id")       # 获取对象ID
            v_menu_id = v_active_id[3:]       # 截取第3个字符到结尾
            driver.switch_to_frame("frame" + v_menu_id)
            if driver.find_element_by_id("btnBase").is_displayed():
                print("目标凭证点击穿透查看OK")
        else:
            print("当前单据状态未清")

    # 销售管理-销售交货-单据复制功能
    def test_0609_06_copy(self):
        """销售管理-销售交货-单据复制功能"""
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
        driver.switch_to_frame("winAdd_IFrame")     # 切换到业务伙伴选择窗体
        driver.find_element_by_id("txtSearchText").send_keys("C")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(2)
        driver.find_elements_by_class_name("x-grid3-row")[1].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(2)
        driver.switch_to.parent_frame()
        # 是否依据新的业务伙伴数据更新凭证行
        for i in driver.find_elements_by_tag_name("button"):
            if i.text == "是":
                i.click()
                break
        # 备注
        driver.find_element_by_id("txtComments").send_keys("单据复制添加Auto" + v_tim)
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
                print(i.text)
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_0609_06_copy.jpg")
                unittest.expectedFailure("test_0609_06_copy")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(SaleDelivery("test_0609_01_Add"))

    runner = unittest.TextTestRunner()
    runner.run(testsuit)