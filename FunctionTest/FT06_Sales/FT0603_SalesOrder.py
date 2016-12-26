
from PubliCode.onlineClass import *
from PubliCode.randData import *


class SalesOrder(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_part_text(self, "销售管理", "销售订单")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000190")
        # 排除自定义字段遮挡干扰
        ClasForm.form_field_hide(self, driver)

    # --销售管理---销售订单
    def test_0603_01_Add(self):
        """销售管理-销售订单-新增单据功能"""
        driver = self.driver
        # 业务伙伴
        driver.find_element_by_xpath("//*[@id='bodyContent_ctl72_Container']/div/div/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")     # 切换到业务伙伴选择窗体
        driver.find_element_by_id("txtSearchText").send_keys("C")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(2)
        driver.find_elements_by_class_name("x-grid3-row")[1].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        driver.switch_to.parent_frame()
        v_tim = time.strftime("%Y%m%d %H:%M:%S")
        # 行-物料号
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
        # 行-备注
        driver.find_element_by_xpath(
            "//*[@id='GridPanelItem']/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[4]").click()
        time.sleep(1)
        driver.switch_to.active_element.send_keys(v_tim + "Auto")
        # 行-数量
        driver.find_element_by_xpath(
            "//*[@id='GridPanelItem']/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[5]").click()
        time.sleep(1)
        driver.switch_to.active_element.send_keys(random.randint(1, 8))
        # 备注
        driver.find_element_by_id("txtComments").send_keys("销售订单添加Auto" + v_tim)
        driver.find_element_by_id("btnSave").click()
        time.sleep(4)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功，单号" in i.text:
                print(i.text)
            elif "流程已触发" in i.text:
                print(i.text)
            else:
                print(i.text)
                unittest.expectedFailure("test_0603_01_Add")

    # 销售管理-销售订单-客户编号为空穿透提示检查
    def test_0603_02_Client(self):
        """销售管理-销售订单-客户编号为空穿透提示检查"""
        driver = self.driver
        driver.find_element_by_id("btnGoOCRD").click()      # 客户主数据穿透
        time.sleep(2)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "业务伙伴为空" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_0603_02_Client.jpg")
                print(i.text)
                unittest.expectedFailure("test_0603_02_Client")

    # 销售管理-销售订单-客户主数据穿透功能
    def test_0603_03_First(self):
        """销售管理-销售订单-客户主数据穿透功能"""
        driver = self.driver
        driver.find_element_by_id("btnFirst").click()
        time.sleep(3)
        driver.find_element_by_id("btnGoOCRD").click()      # 客户主数据穿透
        time.sleep(3)
        driver.switch_to.frame("winActivity_IFrame")     # 切换到业务伙伴主数据查看页面
        v_general = driver.find_element_by_link_text("常规")
        try:
            v_general.is_displayed()
            print("销售管理-销售订单穿透到业务伙伴主数据页面显示OK")
        except ImportError:
            print("BUG 销售管理-销售订单穿透到业务伙伴主数据页面显示异常")
            unittest.expectedFailure("test_0603_03_First")

    # 销售管理-销售订单-单据复制到功能
    def test_0603_04_goto(self):
        """销售管理-销售订单-单据复制到功能"""
        driver = self.driver
        driver.find_element_by_id("btnLast").click()
        time.sleep(4)
        if driver.find_element_by_id("btnCopyTo").is_displayed():
            driver.find_element_by_id("btnCopyTo").click()
            time.sleep(1)
            v_wlcode = ("交货", "应收发票", "预留发票")
            v_checked = v_wlcode[random.randint(0, 2)]
            driver.find_element_by_link_text(v_checked).click()
            time.sleep(4)
            v_tim = time.strftime("%Y-%m-%d")
            driver.switch_to.parent_frame()
            # print(v_checked)
            if v_checked == "交货":
                ClasForm.form_top(self, 0)
                driver.switch_to.frame("frame_tab_PM000194")
                # 排除自定义字段遮挡干扰
                ClasForm.form_field_hide(self, driver)
                ClasForm.form_today(self, "dfDocDueDate")
            elif v_checked == "应收发票":
                ClasForm.form_top(self, 0)
                driver.switch_to.frame("frame_tab_PM000200")
                # 排除自定义字段遮挡干扰
                ClasForm.form_field_hide(self, driver)
                ClasForm.form_today(self, "dfDocDueDate")
            else:
                ClasForm.form_top(self, 0)
                driver.switch_to.frame("frame_tab_PM000223")
                # 排除自定义字段遮挡干扰
                ClasForm.form_field_hide(self, driver)
                ClasForm.form_today(self, "dfDocDueDate")
            driver.find_element_by_id("btnSave").click()
            time.sleep(4)
            v_tip = driver.find_elements_by_class_name("ext-mb-text")
            for i in v_tip:
                if "成功，单号" in i.text:
                    print(i.text + v_checked)
                elif "流程已触发" in i.text:
                    print(i.text + v_checked)
                else:
                    print(i.text + v_checked)
                    unittest.expectedFailure("test_0603_04_goto")
        else:
            print("单据已清，不能复制到")

    # 销售管理-销售订单-目标凭证查看
    def test_0603_05_target(self):
        """销售管理-销售订单-目标凭证查看"""
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

    # 销售管理-销售订单-单据复制从
    def test_0603_06_CopyFrom(self):
        """销售管理-销售订单-新增单据功能"""
        driver = self.driver
        # 业务伙伴
        driver.find_element_by_xpath("//*[@id='bodyContent_ctl72_Container']/div/div/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")     # 切换到业务伙伴选择窗体
        driver.find_element_by_id("txtSearchText").send_keys("C")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(2)
        driver.find_elements_by_class_name("x-grid3-row")[1].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        driver.switch_to.parent_frame()
        v_tim = time.strftime("%Y-%m-%d %H:%M:%S")
        # 复制从
        driver.find_element_by_id("btnCopyFrom").click()
        # 复制从-销售报价单
        driver.find_element_by_id("MenuItemCopyFromQuotations").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")
        v_l_copy = driver.find_elements_by_class_name("x-grid3-row")
        if len(v_l_copy) > 0:
            v_l_copy[0].click()
        driver.find_element_by_id("btnSelect").click()
        driver.switch_to.parent_frame()
        time.sleep(2)
        ClasForm.form_button_yes(self, "否")
        time.sleep(2)
        driver.find_element_by_id("btnSave").click()
        time.sleep(3)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功" in i.text:
                print(i.text)
            elif "流程已触发" in i.text:
                print(i.text)
            else:
                print(i.text)
                unittest.expectedFailure("test_0603_06_CopyFrom")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(SalesOrder("test_0603_01_Add"))

    runner = unittest.TextTestRunner()
    runner.run(testsuit)