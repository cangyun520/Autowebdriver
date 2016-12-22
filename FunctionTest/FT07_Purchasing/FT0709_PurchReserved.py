
from PubliCode.randData import *
from PubliCode.onlineClass import *
from selenium.webdriver.common.action_chains import ActionChains


class PurchReserved(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_part_text(self, "采购管理", "应付预留发票")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000221")
        # 排除自定义字段遮挡干扰
        ClasForm.form_field_hide(self, driver)

    # 采购管理---应付预留发票
    def test_0709_01_Add(self):
        """采购管理-应付预留发票-新增单据功能检查"""
        driver = self.driver
        driver.find_element_by_xpath("//*[@id='CompositeField2_Container']/div/div/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")     # 切换到业务伙伴选择窗体
        driver.find_element_by_id("gpSelect").click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        v_tim = time.strftime("%Y-%m-%d %H:%M:%S")
        driver.switch_to.parent_frame()
        # # 有效期至
        # ClasForm.form_today(self, "dfDocDueDate")
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
        time.sleep(1)
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        driver.switch_to.parent_frame()
        driver.find_element_by_id("txtComments").send_keys("应付预留发票添加Auto" + v_tim)
        driver.find_element_by_id("btnSave").click()
        time.sleep(4)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功" in i.text:
                print(i.text)
            elif "流程已触发" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_0709_01_Add.jpg")
                print(i.text)
                unittest.expectedFailure("test_0709_01_Add")

    # 采购管理-应付预留发票-业务伙伴编号为空穿透提示检查
    def test_0709_02_Client(self):
        """采购管理-应付预留发票-业务伙伴编号为空穿透提示检查"""
        driver = self.driver
        driver.find_element_by_id("btnGoOCRD").click()      # 业务伙伴主数据穿透
        time.sleep(2)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "业务伙伴为空" in i.text:
                print("应付预留发票-业务伙伴编号为空穿透提示检查OK")
            else:
                print("BUG  应付预留发票-业务伙伴编号为空穿透提示检查异常")
                unittest.expectedFailure("test_0709_02_Client")

    # 采购管理-应付预留发票-伙伴主数据穿透功能检查
    def test_0709_03_last(self):
        """采购管理-应付预留发票-业务伙伴主数据穿透功能检查"""
        driver = self.driver
        driver.find_element_by_id("btnLast").click()
        time.sleep(3)
        driver.find_element_by_id("btnGoOCRD").click()      # 业务伙伴主数据穿透
        time.sleep(3)
        driver.switch_to.frame("winActivity_IFrame")     # 切换到业务伙伴主数据查看页面
        v_general = driver.find_element_by_link_text("常规")
        try:
            v_general.is_displayed()
            print("采购管理-应付预留发票穿透到伙伴主数据页面显示OK")
        except ImportError:
            print("BUG 采购管理-应付预留发票穿透到伙伴主数据页面显示异常")
            unittest.expectedFailure("test_0709_03_last")

    # 采购管理-应付预留发票-单据复制到功能
    def test_0709_04_goto(self):
        """采购管理-应付预留发票-单据复制到功能"""
        driver = self.driver
        driver.find_element_by_id("btnLast").click()
        time.sleep(3)
        if driver.find_element_by_id("btnCopyTo").is_displayed():
            driver.find_element_by_id("btnCopyTo").click()
            time.sleep(1)
            # v_wlcode = ("收货采购订单", "应付贷项凭证")
            # v_checked = v_wlcode[random.randint(0, 1)]
            v_checked = "收货采购订单"
            driver.find_element_by_link_text(v_checked).click()
            time.sleep(4)
            driver.switch_to.parent_frame()
            if v_checked == "收货采购订单":
                ClasForm.form_top(self, 0)
                driver.switch_to.frame("frame_tab_PM000197")
                # 排除自定义字段遮挡干扰
                ClasForm.form_field_hide(self, driver)
                # 有效期至
                ClasForm.form_today(self, "dfDocDueDate")
            else:
                ClasForm.form_top(self, 0)
                driver.switch_to.frame("frame_tab_PM000219")
                # 排除自定义字段遮挡干扰
                ClasForm.form_field_hide(self, driver)
                # 有效期至
                ClasForm.form_today(self, "dfDocDueDate")
            driver.find_element_by_id("btnSave").click()
            time.sleep(5)
            v_tip = driver.find_elements_by_class_name("ext-mb-text")
            for i in v_tip:
                if "成功" in i.text:
                    print(i.text + v_checked)
                elif "流程已触发" in i.text:
                    print(i.text + v_checked)
                else:
                    driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_0709_04_goto.jpg")
                    print(i.text)
                    unittest.expectedFailure("test_0709_04_goto")
        else:
            print("应付预留发票-单据已清，无复制到选项")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(PurchReserved("test_0709_01_Add"))
    runner = unittest.TextTestRunner()
    runner.run(testsuit)