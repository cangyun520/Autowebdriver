
from PubliCode.onlineClass import *
from PubliCode.randData import *


class SalesARI_Pay(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "销售管理", "应收发票+付款")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000202")
        # 排除自定义字段遮挡干扰
        ClasForm.form_field_hide(self, driver)

    # --销售管理---应收发票+付款
    def test_0605_01_Add(self):
        """销售管理-应收发票+付款-新增单据功能"""
        driver = self.driver
        v_tim = time.strftime("%Y-%m-%d %H:%M:%S")
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
        driver.find_element_by_id("btnPayments").click()
        time.sleep(3)
        driver.find_element_by_id("tfTrsfrAcct").send_keys("100101")
        driver.find_element_by_id("Button11111").click()
        time.sleep(1)
        driver.find_element_by_id("btnPaySave").click()
        time.sleep(1)
        driver.find_element_by_id("txtComments").send_keys("应收发票+付款添加Auto" + v_tim)
        driver.find_element_by_id("btnSave").click()
        time.sleep(5)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功" in i.text:
                print(i.text)
            elif "流程已触发" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_0605_01_Add.jpg")
                # print(i.text)
                unittest.expectedFailure("test_0605_01_Add")

    def test_0605_03_last(self):
        """销售管理-应收发票+付款-客户主数据穿透功能"""
        driver = self.driver

        driver.find_element_by_id("btnLast").click()
        time.sleep(3)
        driver.find_element_by_id("btnGoOCRD").click()      # 客户主数据穿透
        time.sleep(3)
        driver.switch_to.frame("winActivity_IFrame")     # 切换到业务伙伴主数据查看页面
        v_general = driver.find_element_by_link_text("常规")
        try:
            v_general.is_displayed()
            print("销售管理-应收发票+付款穿透到业务伙伴主数据页面显示OK")
        except ImportError:
            print("BUG 销售管理-应收发票+付款穿透到业务伙伴主数据页面显示异常")
            unittest.expectedFailure("test_0605_03_last")
            
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(SalesARI_Pay("test_0605_01_Add"))

    runner = unittest.TextTestRunner()
    runner.run(testsuit)