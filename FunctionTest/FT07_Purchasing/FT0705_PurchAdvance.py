
from PubliCode.onlineClass import *
from PubliCode.randData import *
from selenium.webdriver.common.action_chains import ActionChains
import win32api


class PurchAdvance(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_part_text(self, "采购管理", "采购预付款申请")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000218")
        # 排除自定义字段遮挡干扰
        ClasForm.form_field_hide(self, driver)

    # 采购管理---采购预付款申请
    def test_0705_01_Add(self):
        """采购管理-采购预付款申请-新增单据功能检查"""
        driver = self.driver
        driver.find_element_by_xpath("//*[@id='CompositeField2_Container']/div/div/div/span").click()
        time.sleep(3)
        driver.switch_to_frame("winAdd_IFrame")     # 切换到业务伙伴选择窗体
        driver.find_element_by_id("gpSelect").click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        driver.switch_to.parent_frame()
        v_tim = time.strftime("%Y-%m-%d %H:%M:%S")
        # 有效期至
        ClasForm.form_today(self, "dfDocDueDate")
        driver.find_element_by_xpath(
            "//*[@id='GridPanelItem']/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath(
            "//*[@id='GridPanelItem']/div/div/div/div/div[2]/div[2]/div/span").click()
        time.sleep(2)
        driver.switch_to_frame("winAdd_IFrame")     # 切换到物料选择窗体
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
        driver.find_element_by_id("txtComments").send_keys("采购预付款申请添加Auto" + v_tim)
        driver.find_element_by_id("btnSave").click()
        time.sleep(4)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功" in i.text:
                print(i.text)
            elif "流程已触发" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_0705_01_Add.jpg")
                print(i.text)
                unittest.expectedFailure("test_0705_01_Add")

    # 采购管理-采购预付款申请-业务伙伴编号为空穿透提示检查
    def test_0705_02_Client(self):
        """采购管理-采购预付款申请-业务伙伴编号为空穿透提示检查"""
        driver = self.driver
        driver.find_element_by_id("btnGoOCRD").click()      # 业务伙伴主数据穿透
        time.sleep(2)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "业务伙伴为空" in i.text:
                print(i.text)
            else:
                print(i.text)
                unittest.expectedFailure("test_0705_02_Client")

    # 采购管理-采购预付款申请-伙伴主数据穿透功能检查
    def test_0705_03_First(self):
        """采购管理-采购预付款申请-业务伙伴主数据穿透功能检查"""
        driver = self.driver
        driver.find_element_by_id("btnFirst").click()
        time.sleep(3)
        driver.find_element_by_id("btnGoOCRD").click()      # 业务伙伴主数据穿透
        time.sleep(3)
        driver.switch_to_frame("winActivity_IFrame")     # 切换到业务伙伴主数据查看页面
        v_general = driver.find_element_by_link_text("常规")
        try:
            v_general.is_displayed()
            print("采购管理-采购预付款申请穿透到伙伴主数据页面显示OK")
        except ImportError:
            print("BUG 采购管理-采购预付款申请穿透到伙伴主数据页面显示异常")
            unittest.expectedFailure("test_0705_03_First")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(PurchAdvance("test_0705_01_Add"))

    runner = unittest.TextTestRunner()
    runner.run(testsuit)