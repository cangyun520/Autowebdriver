
from selenium.webdriver.common.action_chains import ActionChains
from PubliCode.onlineClass import *
from PubliCode.randData import *


class PaymentApply(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "费用管理", "付款申请")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM001083")

    """费用管理-付款申请-单据添加功能"""
    def test_0905_01_add(self):
        """费用管理-付款申请-单据添加功能"""
        driver = self.driver
        driver.find_element_by_id("BtnAdd").click()
        time.sleep(3)
        driver.switch_to_frame("winSendInspection_IFrame")        # 切换到新增页面
        v_tim = time.strftime("%y%m%d%H%M")
        driver.find_element_by_xpath("//*[@id='PartnerNum_Container']/div/span/img[2]").click()        # 收款单位
        time.sleep(3)
        driver.switch_to_frame("winAdd_IFrame")         # 切换到收款单位选择窗体
        driver.find_element_by_id("txtSearchText").send_keys("v1")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(1)
        v_typelist = driver.find_elements_by_class_name("x-grid3-row")
        v_typelist[random.randint(0, (len(v_typelist)-1))].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(1)
        driver.switch_to.parent_frame()
        # 开户银行
        driver.find_element_by_id("txtBank").send_keys(fun_data_bank())
        # 银行账号
        driver.find_element_by_id("txtBankNumber").send_keys(fun_idcard())
        # 开户姓名
        driver.find_element_by_id("txtBankName").send_keys(fun_data_name())
        # 申请事由
        driver.find_element_by_id("Remark").send_keys(
            "这是一张付款申请单Auto，这是测试说的Auto。申请日期：" + v_tim)
        # 用款类型选择
        driver.find_element_by_id("cbxDocType_Container").click()
        for i in driver.find_elements_by_class_name("x-combo-list-item"):
            if i.text == "采购业务款项申请":
                i.click()
                break
        time.sleep(2)
        # 行数据选择
        v_object = driver.find_element_by_xpath(
            "//*[@id='GridPanel1']/div/div/div/div/div[2]/div/div/table/tbody/tr[1]/td[3]").click()
        ActionChains(driver).double_click(v_object).perform()
        time.sleep(1)
        driver.find_element_by_xpath(
            "//*[@id='GridPanel1']/div/div/div/div/div[2]/div[2]/div/span").click()
        time.sleep(2)
        driver.switch_to_frame("winAdd_IFrame")     # 切换到物料选择窗体
        v_wlcode = driver.find_elements_by_class_name("x-grid3-row")
        if len(v_wlcode) > 5:
            v_total = 0
            while v_total <= 4:
                v_wlcode[v_total].click()
                v_total += 1
        else:
            v_wlcode[0].click()
        driver.find_element_by_id("Button1").click()
        time.sleep(2)
        driver.switch_to.parent_frame()
        # 提交单据
        driver.find_element_by_id("btnSave").click()
        time.sleep(4)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "流程已触发" in i.text:
                print(i.text)
            elif "单据添加成功" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/test_0905_01_add.jpg")
                print(i.text)
                unittest.expectedFailure("test_0905_01_add")

    """费用管理-付款申请-添加界面关闭功能"""
    def test_0905_02(self):
        """费用管理-付款申请-添加界面关闭功能"""
        driver = self.driver
        # 随机双击行数据进入到查看界面
        v_list = driver.find_elements_by_class_name("x-grid3-row")
        # 如果行列表无数据时则通过点击添加进入到页面
        if len(v_list) == 0:
            driver.find_element_by_id("BtnAdd").click()
        else:
            ActionChains(driver).double_click(v_list[random.randint(0, len(v_list)-1)].click()).perform()
        time.sleep(3)
        driver.switch_to_frame("winSendInspection_IFrame")        # 切换到新增页面
        driver.find_element_by_id("btnCancel").click()
        time.sleep(2)
        ClasForm.form_button_yes(self, "是")
        driver.switch_to.parent_frame()
        try:
            driver.find_element_by_id("BtnAdd").is_displayed()
            print("费用管理-付款申请-查看界面关闭功能OK")
        except ImportError:
            unittest.expectedFailure("test_0905_02")

    """费用管理-付款申请-单据保存草稿功能"""
    def test_0905_03_draft(self):
        """费用管理-付款申请-单据添加功能"""
        driver = self.driver
        driver.find_element_by_id("BtnAdd").click()
        time.sleep(3)
        driver.switch_to_frame("winSendInspection_IFrame")        # 切换到新增页面
        v_tim = time.strftime("%y%m%d%H%M")
        driver.find_element_by_xpath("//*[@id='PartnerNum_Container']/div/span/img[2]").click()        # 收款单位
        time.sleep(3)
        driver.switch_to_frame("winAdd_IFrame")         # 切换到收款单位选择窗体
        driver.find_element_by_id("txtSearchText").send_keys("v1")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(1)
        v_typelist = driver.find_elements_by_class_name("x-grid3-row")
        v_typelist[random.randint(0, (len(v_typelist)-1))].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(1)
        driver.switch_to.parent_frame()
        # 开户银行
        driver.find_element_by_id("txtBank").send_keys(fun_data_bank())
        # 银行账号
        driver.find_element_by_id("txtBankNumber").send_keys(fun_idcard())
        # 开户姓名
        driver.find_element_by_id("txtBankName").send_keys(fun_data_name())
        # 申请事由
        driver.find_element_by_id("Remark").send_keys(
            "这是一张付款申请单Auto，这是测试说的Auto。申请日期：" + v_tim)
        # 用款类型选择
        driver.find_element_by_id("cbxDocType_Container").click()
        for i in driver.find_elements_by_class_name("x-combo-list-item"):
            if i.text == "采购业务款项申请":
                i.click()
                break
        time.sleep(2)
        # 行数据选择
        v_object = driver.find_element_by_xpath(
            "//*[@id='GridPanel1']/div/div/div/div/div[2]/div/div/table/tbody/tr[1]/td[3]").click()
        ActionChains(driver).double_click(v_object).perform()
        time.sleep(1)
        driver.find_element_by_xpath(
            "//*[@id='GridPanel1']/div/div/div/div/div[2]/div[2]/div/span").click()
        time.sleep(2)
        driver.switch_to_frame("winAdd_IFrame")     # 切换到物料选择窗体
        driver.find_elements_by_class_name("x-grid3-row")[0].click()
        driver.find_element_by_id("Button1").click()
        time.sleep(2)
        driver.switch_to.parent_frame()
        # 提交草稿单据
        driver.find_element_by_id("btnSaveDraft").click()
        time.sleep(4)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "保存草稿成功" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/test_0905_01_add.jpg")
                print(i.text)
                unittest.expectedFailure("test_0905_03_draft")

    """费用管理-付款申请-普通款项申请添加功能"""
    def test_0905_04_addNormal(self):
        """费用管理-付款申请-普通款项申请添加功能"""
        driver = self.driver
        driver.find_element_by_id("BtnAdd").click()
        time.sleep(3)
        driver.switch_to_frame("winSendInspection_IFrame")        # 切换到新增页面
        v_tim = time.strftime("%y%m%d%H%M")
        driver.find_element_by_xpath("//*[@id='PartnerNum_Container']/div/span/img[2]").click()        # 收款单位
        time.sleep(3)
        driver.switch_to_frame("winAdd_IFrame")         # 切换到收款单位选择窗体
        driver.find_element_by_id("txtSearchText").send_keys("v1")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(1)
        v_typelist = driver.find_elements_by_class_name("x-grid3-row")
        v_typelist[random.randint(0, (len(v_typelist)-1))].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(1)
        driver.switch_to.parent_frame()
        # 开户银行
        driver.find_element_by_id("txtBank").send_keys(fun_data_bank())
        # 银行账号
        driver.find_element_by_id("txtBankNumber").send_keys(fun_idcard())
        # 开户姓名
        driver.find_element_by_id("txtBankName").send_keys(fun_data_name())
        # 申请事由
        driver.find_element_by_id("Remark").send_keys(
            "这是一张付款申请单Auto，这是测试说的Auto。申请日期：" + v_tim)
        # 用款类型选择
        driver.find_element_by_id("cbxDocType_Container").click()
        for i in driver.find_elements_by_class_name("x-combo-list-item"):
            if i.text == "采购业务款项申请":
                i.click()
                break
        time.sleep(2)
        # 行数据选择
        v_object = driver.find_element_by_xpath(
            "//*[@id='GridPanel1']/div/div/div/div/div[2]/div/div/table/tbody/tr[1]/td[3]").click()
        ActionChains(driver).double_click(v_object).perform()
        time.sleep(1)
        driver.find_element_by_xpath(
            "//*[@id='GridPanel1']/div/div/div/div/div[2]/div[2]/div/span").click()
        time.sleep(2)
        driver.switch_to_frame("winAdd_IFrame")     # 切换到物料选择窗体
        v_wlcode = driver.find_elements_by_class_name("x-grid3-row")
        if len(v_wlcode) > 5:
            v_total = 0
            while v_total <= 4:
                v_wlcode[v_total].click()
                v_total += 1
        else:
            v_wlcode[0].click()
        driver.find_element_by_id("Button1").click()
        time.sleep(2)
        driver.switch_to.parent_frame()
        # 提交单据
        driver.find_element_by_id("btnSave").click()
        time.sleep(4)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "流程已触发" in i.text:
                print(i.text)
            elif "单据添加成功" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/test_0905_01_add.jpg")
                print(i.text)
                unittest.expectedFailure("test_0905_01_addNormal")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(PaymentApply("test_0904_01_add"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)