from PubliCode.config import *
from selenium.webdriver.common.action_chains import ActionChains
from PubliCode.onlineClass import *
from PubliCode.randData import *


class Reimbursement(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "费用管理", "费用报销")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000784")

    """费用管理-费用报销-单据添加功能"""
    def test_0604_01_add(self):
        """费用管理-费用报销-单据添加功能"""
        driver = self.driver
        driver.find_element_by_id("btnAdd").click()
        time.sleep(3)
        # 切换到新增页面
        driver.switch_to.frame("winActivity_IFrame")
        v_tim = time.strftime("%Y%m%d %H:%M")
        # 报销部门
        driver.find_element_by_xpath("//*[@id='OrgName_Container']/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")
        driver.find_element_by_id("txtBPartners").send_keys("总经办")
        driver.find_element_by_id("btnBPartners").click()
        time.sleep(1)
        # 选择总经办
        driver.find_elements_by_class_name("x-grid3-row")[0].click()
        driver.find_element_by_id("Button1").click()
        time.sleep(2)
        driver.switch_to.parent_frame()
        # 报销人
        driver.find_element_by_xpath("//*[@id='PersonName_Container']/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")
        for i in driver.find_elements_by_class_name("x-grid3-row"):
            i.click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(2)
        driver.switch_to.parent_frame()
        # 冲抵借支
        driver.find_element_by_id("OffsetCash").click()
        v_list_offset = driver.find_elements_by_class_name("x-combo-list-item")
        v_offset_check = random.choice(["是", "否"])
        for ii in v_list_offset:
            if v_offset_check in ii.text:
                ii.click()
                break
        # 开户银行
        driver.find_element_by_id("AccountBank").send_keys(fun_data_bank())
        # 银行账号
        driver.find_element_by_id("Account").send_keys(fun_idcard())
        # 开户姓名
        driver.find_element_by_id("AccountName").send_keys(fun_data_name())
        # 报销事由
        driver.find_element_by_id("Remark").send_keys("这是一张合伙报销单Auto，这是测试说的Auto。申请日期：" + v_tim)
        # 行数据添加
        v_lines = driver.find_element_by_xpath(
            "//*[@id='gpExpensesReimbursemen']/div/div/div/div/div[2]")
        ActionChains(driver).context_click(v_lines).perform()
        driver.find_element_by_link_text("添加行").click()
        time.sleep(1)
        # 行数据添加-报销项目
        v_project = driver.find_element_by_xpath(
            "//*[@id='gpExpensesReimbursemen']/div/div/div/div/div[2]/div/div/table/tbody/tr/td[2]")
        ActionChains(driver).double_click(v_project).perform()
        driver.find_element_by_xpath(
            "//*[@id='gpExpensesReimbursemen']/div/div/div/div/div[2]/div[2]/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")
        driver.find_elements_by_class_name("x-grid3-row")[0].click()
        driver.find_element_by_id("Button1").click()
        time.sleep(2)
        driver.switch_to.parent_frame()
        # 行数据添加-摘要
        v_abstract = driver.find_element_by_xpath(
            "//*[@id='gpExpensesReimbursemen']/div/div/div/div/div[2]/div/div/table/tbody/tr/td[3]")
        ActionChains(driver).double_click(v_abstract).perform()
        driver.find_element_by_id("TextField1").send_keys("合伙报销一笔费用Auto。测试说的")
        # 行数据添加-金额
        v_amount = driver.find_element_by_xpath(
            "//*[@id='gpExpensesReimbursemen']/div/div/div/div/div[2]/div/div/table/tbody/tr/td[4]")
        ActionChains(driver).double_click(v_amount).perform()
        driver.find_element_by_id("NumberField1").send_keys(random.randint(500, 5000))
        time.sleep(1)
        # 调用自由流审批人选择函数
        ClasFlow.flow_free(self, "bear")
        driver.find_element_by_id("btnWorkflow").click()
        time.sleep(3)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "流程已触发" in i.text:
                print(i.text)
            elif "成功" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/oa/test_0604_01_add.jpg")
                print(i.text)
                unittest.expectedFailure("test_0604_01_add")

    """费用管理-报销管理-费用报销界面关闭功能"""
    def test_0604_02(self):
        """费用管理-报销管理-费用报销界面关闭功能"""
        driver = self.driver
        # 随机双击行数据进入到查看界面
        v_list = driver.find_elements_by_class_name("x-grid3-row")
        # 如果行列表无数据时则通过点击添加进入到页面
        if len(v_list) == 0:
            driver.find_element_by_id("btnAdd").click()
        else:
            ActionChains(driver).double_click(v_list[random.randint(0, len(v_list)-1)].click()).perform()
        time.sleep(3)
        # 切换到新增页面
        driver.switch_to.frame("winActivity_IFrame")

        # 取消关闭页面
        driver.find_element_by_id("btnCancel").click()
        time.sleep(2)
        ClasForm.form_button_yes(self, "是")
        driver.switch_to.parent_frame()
        try:
            driver.find_element_by_id("btnAdd").is_displayed()
            print("费用管理-报销管理-查看界面关闭功能OK")
        except ImportError:
            unittest.expectedFailure("test_0604_02")

    """费用管理-报销管理-添加草稿功能"""
    def test_0604_03_draft(self):
        """费用管理-报销管理-添加草稿功能"""
        driver = self.driver
        driver.find_element_by_id("btnAdd").click()
        time.sleep(3)
        # 切换到新增页面
        driver.switch_to.frame("winActivity_IFrame")
        v_tim = time.strftime("%Y%m%d %H:%M")
        # 报销部门
        driver.find_element_by_xpath("//*[@id='OrgName_Container']/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")
        driver.find_element_by_id("txtBPartners").send_keys("总经办")
        driver.find_element_by_id("btnBPartners").click()
        time.sleep(1)
        # 选择总经办
        driver.find_elements_by_class_name("x-grid3-row")[0].click()
        driver.find_element_by_id("Button1").click()
        time.sleep(2)
        driver.switch_to.parent_frame()
        # 报销人
        driver.find_element_by_xpath("//*[@id='PersonName_Container']/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")
        for i in driver.find_elements_by_class_name("x-grid3-row"):
            i.click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(2)
        driver.switch_to.parent_frame()
        # 冲抵借支
        driver.find_element_by_id("OffsetCash").click()
        v_list_offset = driver.find_elements_by_class_name("x-combo-list-item")
        v_offset_check = random.choice(["是", "否"])
        for ii in v_list_offset:
            if v_offset_check in ii.text:
                ii.click()
                break
        # 报销事由
        driver.find_element_by_id("Remark").send_keys("被用作草稿-删除测试数据：" + v_tim)
        # 行数据添加
        v_lines = driver.find_element_by_xpath(
            "//*[@id='gpExpensesReimbursemen']/div/div/div/div/div[2]")
        ActionChains(driver).context_click(v_lines).perform()
        driver.find_element_by_link_text("添加行").click()
        time.sleep(1)
        # 行数据添加-报销项目
        v_project = driver.find_element_by_xpath(
            "//*[@id='gpExpensesReimbursemen']/div/div/div/div/div[2]/div/div/table/tbody/tr/td[2]")
        ActionChains(driver).double_click(v_project).perform()
        driver.find_element_by_xpath(
            "//*[@id='gpExpensesReimbursemen']/div/div/div/div/div[2]/div[2]/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")
        driver.find_elements_by_class_name("x-grid3-row")[0].click()
        driver.find_element_by_id("Button1").click()
        time.sleep(2)
        driver.switch_to.parent_frame()

        # 行数据添加-金额
        v_amount = driver.find_element_by_xpath(
            "//*[@id='gpExpensesReimbursemen']/div/div/div/div/div[2]/div/div/table/tbody/tr/td[4]")
        ActionChains(driver).double_click(v_amount).perform()
        driver.find_element_by_id("NumberField1").send_keys(random.randint(500, 5000))
        time.sleep(1)

        driver.find_element_by_id("btnSave").click()
        time.sleep(2)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "保存草稿成功" in i.text:
                print(i.text)
            else:

                driver.get_screenshot_as_file(root_path() + "TestPicture/Erp/test_0604_03_draft.jpg")
                unittest.expectedFailure("test_0604_03_draft")

    """费用管理-报销管理-草稿删除功能"""
    def test_0604_04_delete(self):
        """费用管理-报销管理-草稿删除功能"""
        driver = self.driver
        # 随机双击行数据进入到查看界面
        v_list = driver.find_elements_by_class_name("x-grid3-row")
        # 如果行列表无数据时则通过点击添加进入到页面
        if len(v_list) == 0:
            driver.find_element_by_id("btnAdd").click()
        else:
            ActionChains(driver).double_click(v_list[0].click()).perform()
        time.sleep(3)

        # 切换到新增页面
        driver.switch_to.frame("winActivity_IFrame")
        v_delete = driver.find_element_by_id("btnDelete")
        if v_delete.is_displayed():
            v_delete.click()
            v_tip = driver.find_elements_by_class_name("ext-mb-text")
            for i in v_tip:
                if "删除成功" in i.text:
                    print(i.text)
                else:
                    unittest.expectedFailure("test_0604_04_delete")
        else:
            print("页面没有删除按钮，PASS")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(Reimbursement("test_0604_01_add"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)