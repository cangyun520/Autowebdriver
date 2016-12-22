
from PubliCode.onlineClass import *
from PubliCode.randData import *
from selenium.webdriver.common.action_chains import ActionChains


class PurchApplication(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "采购管理", "采购申请单")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000294")
        # 排除自定义字段遮挡干扰
        ClasForm.form_field_hide(self, driver)

    # 采购管理---采购申请
    def test_0701_01_Add(self):
        """采购管理-采购申请-新增单据功能检查"""
        driver = self.driver
        ClasForm.form_today(self, "dfReqDate")
        ClasForm.form_today(self, "dfDocDueDate")
        v_tim = time.strftime("%Y-%m-%d %H:%M:%S")
        # 行列表区域添加行
        v_line_add = driver.find_element_by_id("GridPanelItem")
        ActionChains(driver).context_click(v_line_add).perform()
        driver.find_element_by_id("AddRecord").click()
        time.sleep(1)
        # 操作行物料
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
        driver.find_element_by_id("txtComments").send_keys("采购申请添加Auto" + v_tim)
        driver.find_element_by_id("btnSave").click()
        time.sleep(4)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功" in i.text:
                print(i.text)
            elif "流程已触发" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_0701_01_Add.jpg")
                print(i.text)
                unittest.expectedFailure("test_0701_01_Add")

    # 采购管理-采购申请-单据最后一条
    def test_0701_02_last(self):
        """采购管理-采购申请-单据最后一条"""
        driver = self.driver
        driver.find_element_by_id("btnLast").click()
        time.sleep(3)
        driver.find_element_by_id("btnSave").click()
        time.sleep(3)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功，单号" in i.text:
                print("采购申请-单据更新OK")
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_0701_02_last.jpg")
                unittest.expectedFailure("test_0701_02_last")

    # 采购管理-采购申请-单据复制到功能
    def test_0701_03_goto(self):
        """采购管理-采购申请-单据复制到功能"""
        driver = self.driver
        driver.find_element_by_id("btnLast").click()
        time.sleep(3)
        if driver.find_element_by_id("btnCopyTo").is_displayed():
            driver.find_element_by_id("btnCopyTo").click()
            time.sleep(1)
            v_wlcode = ("采购报价单", "采购订单")
            v_checked = v_wlcode[random.randint(0, 1)]
            driver.find_element_by_link_text(v_checked).click()
            time.sleep(4)
            v_tim = time.strftime("%Y-%m-%d")
            driver.switch_to.parent_frame()
            if v_checked == "采购报价单":
                ClasForm.form_top(self, 0)
                driver.switch_to.frame("frame_tab_PM000193")
                # 排除自定义字段遮挡干扰
                ClasForm.form_field_hide(self, driver)
                # 选择供应商
                driver.find_element_by_xpath("//*[@id='CompositeField2_Container']/div/div/div/span").click()
                time.sleep(3)
                driver.switch_to.frame("winAdd_IFrame")     # 切换到业务伙伴选择窗体
                driver.find_element_by_id("gpSelect").click()
                driver.find_element_by_id("btnSelect").click()
                time.sleep(3)
                driver.switch_to.parent_frame()
                driver.find_element_by_id("ext-comp-1060").click()
                # 要求日期
                ClasForm.form_today(self, "dfReqDate")
            else:
                ClasForm.form_top(self, 0)
                driver.switch_to.frame("frame_tab_PM000191")
                # 排除自定义字段遮挡干扰
                ClasForm.form_field_hide(self, driver)
                # 选择供应商
                driver.find_element_by_xpath("//*[@id='CompositeField2_Container']/div/div/div/span").click()
                time.sleep(3)
                driver.switch_to.frame("winAdd_IFrame")     # 切换到业务伙伴选择窗体
                driver.find_element_by_id("gpSelect").click()
                driver.find_element_by_id("btnSelect").click()
                time.sleep(3)
                driver.switch_to.parent_frame()
                driver.find_element_by_id("ext-comp-1073").click()
                # 交货日期
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
                    driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_0701_03_goto.jpg")
                    print(i.text)
                    unittest.expectedFailure("test_0701_03_goto")
        else:
            print("单据已清，无法复制到")

    # 采购管理-采购申请-单据复制功能
    def test_0701_04_copy(self):
        """采购管理-采购申请-单据复制功能"""
        driver = self.driver
        driver.find_element_by_id("btnPrevious").click()
        time.sleep(3)
        v_object = driver.find_element_by_id("txtState")
        ActionChains(driver).context_click(v_object).perform()
        time.sleep(1)
        driver.find_element_by_id("MenuCopy").click()
        time.sleep(3)
        v_tim = time.strftime("%Y-%m-%d %H:%M:%S")
        # 有效期至
        ClasForm.form_today(self, "dfDocDueDate")
        # 备注
        driver.find_element_by_id("txtComments").send_keys(v_tim + "单据复制添加Auto")
        time.sleep(1)
        driver.find_element_by_id("btnSave").click()
        time.sleep(4)
        ClasForm.form_top(self, 0)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功" in i.text:
                print(i.text)
            elif "流程已触发" in i.text:
                print(i.text)
            else:
                print(i.text)
                unittest.expectedFailure("test_0701_04_copy")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(PurchApplication("test_0701_01_Add"))

    runner = unittest.TextTestRunner()
    runner.run(testsuit)