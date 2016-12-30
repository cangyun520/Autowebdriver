
from PubliCode.onlineClass import *
from PubliCode.randData import *
from selenium.webdriver.common.action_chains import ActionChains
import win32api


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
        ClasForm.form_field_hide(self, driver)

    # 库存管理---采购收货
    def test_0706_01_add(self):
        """库存管理-采购收货-新增单据功能"""
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
        driver.switch_to.default_content()
        driver.switch_to.frame("frame_tab_PM000197")
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
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_0706_01_add.jpg")
                print(i.text)
                unittest.expectedFailure("test_0706_01_add")

    # 库存管理-采购收货-业务伙伴编号为空穿透提示检查
    def test_0706_02_client(self):
        """库存管理-采购收货-业务伙伴编号为空穿透提示检查"""
        driver = self.driver
        driver.find_element_by_id("btnGoOCRD").click()      # 业务伙伴主数据穿透
        time.sleep(2)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "业务伙伴为空" in i.text:
                print("采购收货-业务伙伴编号为空穿透提示检查OK")
            else:
                print("BUG  采购收货-业务伙伴编号为空穿透提示检查异常")
                unittest.expectedFailure("test_0706_02_client")

    # 库存管理-采购收货-业务伙伴主数据穿透功能
    def test_0706_03_First(self):
        """库存管理-采购收货-业务伙伴主数据穿透功能"""
        driver = self.driver
        driver.find_element_by_id("btnFirst").click()
        time.sleep(3)
        driver.find_element_by_id("btnGoOCRD").click()      # 业务伙伴主数据穿透
        time.sleep(3)
        driver.switch_to.frame("winActivity_IFrame")     # 切换到业务伙伴主数据查看页面
        v_general = driver.find_element_by_link_text("常规")
        try:
            v_general.is_displayed()
            print("库存管理-采购收货穿透到伙伴主数据页面显示OK")
        except ImportError:
            print("BUG 库存管理-采购收货穿透到伙伴主数据页面显示异常")
            unittest.expectedFailure("test_0706_03_First")

    # 库存管理-采购收货-单据复制到功能
    def test_0706_04_goto(self):
        """库存管理-采购收货-单据复制到功能"""
        driver = self.driver
        driver.find_element_by_id("btnLast").click()
        time.sleep(3)
        v_tim = time.strftime("%Y-%m-%d")
        try:
            driver.find_element_by_id("btnCopyTo").is_displayed()
            driver.find_element_by_id("btnCopyTo").click()
            time.sleep(1)
            v_tocheck = ("退货", "应付发票")
            v_checked = v_tocheck[random.randint(0, 1)]
            driver.find_element_by_link_text(v_checked).click()
            time.sleep(4)
            driver.switch_to.parent_frame()
            # print(v_checked)
            if v_checked == "退货":
                ClasForm.form_top(self, 0)
                driver.switch_to.frame("frame_tab_PM000201")
                # 排除自定义字段遮挡干扰
                ClasForm.form_field_hide(self, driver)
                # 退货日期
                ClasForm.form_today(self, "dfDocDueDate")
            else:
                ClasForm.form_top(self, 0)
                driver.switch_to.frame("frame_tab_PM000215")
                # 排除自定义字段遮挡干扰
                ClasForm.form_field_hide(self, driver)
                # 有效期至
                ClasForm.form_today(self, "dfDocDueDate")
            driver.find_element_by_id("btnSave").click()
            time.sleep(5)
            v_tip = driver.find_elements_by_class_name("ext-mb-text")
            for i in v_tip:
                if "成功，单号" in i.text:
                    print("采购收货-复制到保存OK-" + v_checked)
                elif "流程已触发" in i.text:
                    print("采购收货-复制到发起审批流程OK-" + v_checked)
                else:
                    driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_0706_04_goto.jpg")
                    print(i.text)
                    unittest.expectedFailure("test_0706_04_goto")
        except ImportError:
            print("采购收货-单据已清，无复制到选项")

    # 采购管理-采购收货-目标凭证查看
    def test_0706_05_target(self):
        """采购管理-采购收货-目标凭证查看"""
        driver = self.driver
        driver.find_element_by_id("btnLast").click()
        time.sleep(4)
        if driver.find_element_by_id("btnTarget").is_displayed():
            driver.find_element_by_id("btnTarget").click()
            time.sleep(3)
            driver.switch_to.default_content()
            v_active = driver.find_element_by_class_name("active")        # 获取对象
            # print(v_active.text)
            v_active_id = v_active.get_attribute("id")       # 获取对象ID
            v_menu_id = v_active_id[3:]       # 截取第3个字符到结尾
            driver.switch_to.frame("frame" + v_menu_id)
            if driver.find_element_by_id("btnBase").is_displayed():
                print("目标凭证点击穿透查看OK")
        else:
            print("当前单据状态未清")
            
    # 销售管理-采购收货-单据复制功能
    def test_0706_06_copy(self):
        """销售管理-采购收货-单据复制功能"""
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
        for i in driver.find_elements_by_tag_name("button"):
            if i.text == "是":
                i.click()
                break
        ClasForm.form_today(self, "dfDocDueDate")
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
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_0706_06_copy.jpg")
                unittest.expectedFailure("test_0706_06_copy")
            
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(PurchReceive("test_0706_01_add"))

    runner = unittest.TextTestRunner()
    runner.run(testsuit)