
from selenium.webdriver.common.action_chains import ActionChains
from PubliCode.onlineClass import *
from PubliCode.randData import *
import win32api
import win32con


class Reimbursement(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "费用管理", "差旅费报销")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000782")

    """费用管理-差旅费报销-单据添加功能"""
    def test_0605_01_add(self):
        """费用管理-差旅费报销-单据添加功能"""
        driver = self.driver
        driver.find_element_by_id("btnAdd").click()
        time.sleep(3)
        driver.switch_to.frame("winActivity_IFrame")        # 切换到新增页面
        v_tim = time.strftime("%Y%m%d %H:%M")
        # 报销部门
        driver.find_element_by_xpath("//*[@id='OrgName_Container']/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")
        driver.find_element_by_id("txtBPartners").send_keys("总经办")
        driver.find_element_by_id("btnBPartners").click()
        time.sleep(1)
        driver.find_elements_by_class_name("x-grid3-row")[0].click()        # 选择总经办
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
        # 报销事由
        driver.find_element_by_id("Remark").send_keys(v_tim + fun_data_character(100, 500))
        # 报销明细页签数据添加
        v_lines = driver.find_element_by_xpath("//*[@id='gpExpensesReimbursemen']/div/div/div/div/div[2]")
        ActionChains(driver).context_click(v_lines).perform()
        driver.find_element_by_link_text("添加行").click()
        time.sleep(1)
        # 出发日期
        v_date_start = driver.find_element_by_xpath(
            "//*[@id='gpExpensesReimbursemen']/div/div/div/div/div[2]/div/div/table/tbody/tr/td[2]"
        )
        ActionChains(driver).double_click(v_date_start).perform()
        driver.find_element_by_xpath(
            "//*[@id='gpExpensesReimbursemen']/div/div/div/div/div[2]/div[2]/div/img"
        ).click()
        for i in driver.find_elements_by_class_name("x-btn-mc"):
            if i.text == "今天":
                i.click()
                time.sleep(1)
        # 到达日期
        v_date_end = driver.find_element_by_xpath(
            "//*[@id='gpExpensesReimbursemen']/div/div/div/div/div[2]/div/div/table/tbody/tr/td[3]"
        )
        ActionChains(driver).double_click(v_date_end).perform()
        time.sleep(1)
        win32api.keybd_event(9, 0, 0, 0)
        win32api.keybd_event(9, 0, win32con.KEYEVENTfun_KEYUP, 0)     # 释放指令
        win32api.keybd_event(65, 0, 0, 0)
        time.sleep(20)

        driver.find_element_by_xpath(
            "//*[@id='gpExpensesReimbursemen']/div/div/div/div/div[2]/div[3]/div/img"
        ).click()
        for i in driver.find_elements_by_class_name("x-btn-mc"):
            if i.text == "今天":
                i.click()
                time.sleep(3)
        ActionChains(driver).double_click(v_date_end).perform()
        time.sleep(1)
        win32api.keybd_event(9, 0, 0, 0)
        win32api.keybd_event(65, 0, 0, 0)

        # 出发地点

        # 到达地点

        # 摘要

        # 金额

        # 附件张数

        # 备注

        # 自由流审批人选择函数
        ClasFlow.flow_free(driver, "bear")
        driver.find_element_by_id("btnWorkflow").click()
        time.sleep(3)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "流程已触发" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/oa/test_0605_01_add.jpg")
                print(i.text)
                unittest.expectedFailure("test_0605_01_add")

    """费用管理-报销管理-差旅费报销界面关闭功能"""
    def test_0605_02(self):
        """费用管理-报销管理-差旅费报销界面关闭功能"""
        driver = self.driver
        v_list = driver.find_elements_by_class_name("x-grid3-row")
        # 如果行列表无数据时则通过点击添加进入到页面
        if len(v_list) == 0:
            driver.find_element_by_id("btnAdd").click()
        else:
            ActionChains(driver).double_click(v_list[random.randint(0, len(v_list)-1)].click()).perform()
        time.sleep(3)
        driver.switch_to.frame("winActivity_IFrame")        # 切换到新增页面
        # 取消关闭页面
        driver.find_element_by_id("btnCancel").click()
        time.sleep(2)
        for i in driver.find_elements_by_tag_name("button"):
            if i.text == "是":
                i.click()
                break
        time.sleep(2)
        driver.switch_to.parent_frame()
        try:
            driver.find_element_by_id("btnAdd").is_displayed()
            print("费用管理-费用申请-查看界面关闭功能OK")
        except ImportError:
            unittest.expectedFailure("test_0605_02")
            
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(Reimbursement("test_0904_01_add"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)