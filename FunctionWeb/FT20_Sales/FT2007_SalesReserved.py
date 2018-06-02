
from PubliCode.webClass import *


class SalesReserved(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_part_text(self, "销售管理", "应收预留发票")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000223")
        # 排除自定义字段遮挡干扰
        ClasForm.form_field_hide(self)

    '''销售管理-应收预留发票'''
    def test_2007_01_Add(self):
        """销售管理-应收预留发票-新增单据功能"""
        driver = self.driver
        driver.find_element_by_xpath("//*[@id='CompositeField2_Container']/div/div/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")     # 切换到业务伙伴选择窗体
        driver.find_element_by_id("txtBPartners").send_keys("C")
        driver.find_element_by_id("Button6").click()
        time.sleep(2)
        driver.find_elements_by_class_name("x-grid3-row")[1].click()
        time.sleep(1)
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
        driver.find_element_by_id("txtComments").send_keys("应收预留发票添加Auto" + v_tim)
        driver.find_element_by_id("btnSave").click()
        time.sleep(4)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功" in i.text:
                print(i.text)
            elif "流程已触发" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2007_01_Add.jpg")
                print(i.text)
                unittest.expectedFailure("test_2007_01_Add")

    '''销售管理-应收预留发票-客户编号为空穿透提示检查'''
    def test_2007_02_Client(self):
        """销售管理-应收预留发票-客户编号为空穿透提示检查"""
        driver = self.driver
        driver.find_element_by_id("btnGoOCRD").click()      # 客户主数据穿透
        time.sleep(2)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "业务伙伴为空" in i.text:
                print(i.text)
            else:
                print(i.text)
                unittest.expectedFailure("test_2007_02_Client")
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2007_02_Client.jpg")

    '''销售管理-应收预留发票-客户主数据穿透功能'''
    def test_2007_03_First(self):
        """销售管理-应收预留发票-客户主数据穿透功能"""
        driver = self.driver
        driver.find_element_by_id("btnFirst").click()
        time.sleep(4)
        # 客户主数据穿透
        driver.find_element_by_id("btnGoOCRD").click()
        time.sleep(5)
        # 切换到业务伙伴主数据查看页面
        driver.switch_to.frame("winActivity_IFrame")
        v_general = driver.find_element_by_link_text("常规")
        try:
            v_general.is_displayed()
            print("销售管理-应收预留发票穿透到业务伙伴主数据页面显示OK")
        except ImportError:
            print("BUG 销售管理-应收预留发票穿透到业务伙伴主数据页面显示异常")
            unittest.expectedFailure("test_2007_03_First")

    '''销售管理-应收预留发票-单据复制到功能'''

    def test_2007_04_goto(self):
        """销售管理-应收预留发票-单据复制到功能"""
        driver = self.driver
        driver.find_element_by_id("btnLast").click()
        time.sleep(3)
        if driver.find_element_by_id("btnCopyTo").is_displayed():
            driver.find_element_by_id("btnCopyTo").click()
            time.sleep(1)
            v_wlcode = ("交货", "应收贷项凭证")
            v_checked = v_wlcode[random.randint(0, 1)]
            driver.find_element_by_link_text(v_checked).click()
            time.sleep(4)
            v_tim = time.strftime("%Y-%m-%d")
            driver.switch_to.parent_frame()
            if v_checked == "交货":
                ClasForm.form_top(self, 0)
                driver.switch_to.frame("frame_tab_PM000194")
                # 排除自定义字段遮挡干扰
                ClasForm.form_field_hide(self)
                # 交货日期
                ClasForm.form_today(self, "dfDocDueDate")
            else:
                ClasForm.form_top(self, 0)
                driver.switch_to.frame("frame_tab_PM000196")
                # 排除自定义字段遮挡干扰
                ClasForm.form_field_hide(self)
                # 有效期至
                ClasForm.form_today(self, "dfDocDueDate")
            driver.find_element_by_id("btnSave").click()
            time.sleep(4)
            v_tip = driver.find_elements_by_class_name("ext-mb-text")
            for i in v_tip:
                if "成功" in i.text:
                    print(i.text)
                elif "流程已触发" in i.text:
                    print(i.text)
                else:
                    driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2007_04_goto.jpg")
                    print(i.text)
                    unittest.expectedFailure("test_2007_04_goto")
        else:
            print("单据已请，无法复制到")

    '''销售管理-应收预留发票-目标凭证查看'''
    def test_2007_05_target(self):
        """销售管理-应收预留发票-目标凭证查看"""
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

    '''销售管理-应收预留发票-查询功能'''
    def test_2007_06_query(self):
        """销售管理-应收预留发票-查询功能"""
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