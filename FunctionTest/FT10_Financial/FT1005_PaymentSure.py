
from PubliCode.randData import *
from PubliCode.onlineClass import *
from selenium.webdriver.common.action_chains import ActionChains
import win32api


class PaymentSure(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "财务管理", "收款确认")
        driver.switch_to.frame("frame_tab_PM001101")

    '''财务管理-收款确认-新增功能'''
    def test_1005_01_addDT(self):
        """财务管理-收款确认-单据新增"""
        driver = self.driver
        v_total = driver.find_element_by_id("gridList_info").text
        # 截取字符串，并输出统计数字
        if v_total == "没有数据":
            v_num = 0
        else:
            v_num = v_total.split()[-2]
        driver.find_element_by_id("btnAdd").click()
        time.sleep(3)
        # 切换到新增页面
        driver.switch_to.default_content()
        driver.switch_to.frame("frame_tab_PM001102")
        v_list = driver.find_elements_by_class_name("x-grid3-row")
        if len(v_list) > 0:
            driver.find_elements_by_class_name("x-grid3-row-checker")[0].click()
            driver.find_element_by_xpath("//*[@id='tfReceiptAccount_Container']/div/span").click()
            time.sleep(3)
            # 切换到付款科目选择窗体
            driver.switch_to.frame("winAdd_IFrame")
            driver.find_element_by_id("txtCondition").send_keys("人民币")
            driver.find_element_by_id("btnConditionSarch").click()
            time.sleep(2)
            driver.find_elements_by_class_name("x-grid3-row")[1].click()
            driver.find_element_by_id("Button13").click()
            time.sleep(1)
            driver.switch_to.parent_frame()
            # 备注页签
            driver.find_element_by_id("TabPanel1__Panelbz").click()
            time.sleep(1)
            driver.find_element_by_id("txtRemark").send_keys(fun_data_character(500, 800))
            time.sleep(1)
            driver.find_element_by_id("btnSave").click()
            time.sleep(4)
            # 返回到列表页面，通过对比总条数判断是否添加成功
            driver.switch_to.default_content()
            driver.switch_to.frame("frame_tab_PM001101")
            time.sleep(1)
            v_tota2 = driver.find_element_by_id("gridList_info").text
            # 截取字符串，并输出统计数字
            v_tota2 = v_tota2.split()[-2]
            print(v_tota2)
            if int(v_tota2) > int(v_num):
                print("单据添加成功，页面多1条数据")
            else:
                print(v_tota2)
                unittest.expectedFailure("test_1004_03_add")
        else:
            print("DT付款列表为空，不用付款")

    '''财务管理-收款确认-新增应收发票功能'''
    def test_1005_02_addIN(self):
        """财务管理-收款确认-单据新增"""
        driver = self.driver
        v_total = driver.find_element_by_id("gridList_info").text
        # 截取字符串，并输出统计数字
        if v_total == "没有数据":
            v_num = 0
        else:
            v_num = v_total.split()[-2]
        driver.find_element_by_id("btnAdd").click()
        time.sleep(3)
        # 切换到新增页面
        driver.switch_to.default_content()
        driver.switch_to.frame("frame_tab_PM001102")
        # 切换达到应收发票
        driver.find_element_by_id("cmbType").click()
        v_check = driver.find_elements_by_class_name("x-combo-list-item")
        for i in v_check:
            if i.text == "IN-应收发票":
                i.click()
                break
            time.sleep(1)
        v_list = driver.find_elements_by_class_name("x-grid3-row")
        if len(v_list) > 0:
            driver.find_elements_by_class_name("x-grid3-row-checker")[0].click()
            driver.find_element_by_xpath("//*[@id='tfReceiptAccount_Container']/div/span").click()
            time.sleep(3)
            # 切换到付款科目选择窗体
            driver.switch_to.frame("winAdd_IFrame")
            driver.find_element_by_id("txtCondition").send_keys("人民币")
            driver.find_element_by_id("btnConditionSarch").click()
            time.sleep(2)
            driver.find_elements_by_class_name("x-grid3-row")[1].click()
            driver.find_element_by_id("Button13").click()
            time.sleep(1)
            driver.switch_to.parent_frame()
            # 备注页签
            driver.find_element_by_id("TabPanel1__Panelbz").click()
            time.sleep(1)
            driver.find_element_by_id("txtRemark").send_keys(fun_data_character(500, 800))
            time.sleep(1)
            driver.find_element_by_id("btnSave").click()
            time.sleep(4)
            # 返回到列表页面，通过对比总条数判断是否添加成功
            driver.switch_to.default_content()
            driver.switch_to.frame("frame_tab_PM001101")
            time.sleep(1)
            v_tota2 = driver.find_element_by_id("gridList_info").text
            # 截取字符串，并输出统计数字
            v_tota2 = v_tota2.split()[-2]
            print(v_tota2)
            if int(v_tota2) > int(v_num):
                print("单据添加成功，页面多1条数据")
            else:
                print(v_tota2)
                unittest.expectedFailure("test_1004_03_add")
        else:
            print("IN付款列表为空，不用付款")

    """财务管理-收款确认-添加界面关闭功能"""
    def test_1004_03_look(self):
        """财务管理-还款-添加界面关闭功能"""
        driver = self.driver
        # 随机双击行数据进入到查看界面
        v_list = driver.find_elements_by_link_text("详细")
        # 如果行列表无数据时则通过点击添加进入到页面
        if len(v_list) == 0:
            driver.find_element_by_id("btnAdd").click()
        else:
            ActionChains(driver).double_click(v_list[random.randint(0, len(v_list)-1)]).perform()
        time.sleep(3)
        # 切换到新增页面
        driver.switch_to.default_content()
        driver.switch_to.frame("frame_tab_PM001102")
        driver.find_element_by_id("btnCancel").click()
        time.sleep(2)
        ClasForm.form_button_yes(self, "是")
        time.sleep(1)
        driver.switch_to.default_content()
        driver.switch_to.frame("frame_tab_PM001101")
        if driver.find_element_by_name("gridList_length").is_displayed():
            print("财务管理-还款-查看界面关闭功能OK")
        else:
            unittest.expectedFailure("test_1004_03")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(PaymentSure("test_050509_01_Add"))
    runner = unittest.TextTestRunner()
    runner.run(testsuit)