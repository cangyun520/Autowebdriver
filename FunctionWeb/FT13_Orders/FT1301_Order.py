
from selenium.webdriver.common.action_chains import ActionChains

from PubliCode.webClass import *


class Order(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "订货管理", "订货")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM001043")

    '''订货管理-订货-新增单据'''
    def test_1301_01_Add(self):
        """订货管理-订货-新增单据功能"""
        driver = self.driver
        driver.find_element_by_id("BtnAdd").click()
        time.sleep(3)
        driver.switch_to.frame("winSendInspection_IFrame")     # 切换到新增页面
        v_wlline = driver.find_element_by_xpath(
            "//*[@id='gpBorrow']/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[2]")
        ActionChains(driver).double_click(v_wlline).perform()
        time.sleep(1)
        driver.find_element_by_xpath(
            "//*[@id='gpBorrow']/div/div/div/div/div[2]/div[2]/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")     # 切换到物料选择窗体
        driver.find_element_by_id("txtItems").send_keys("A000")
        driver.find_element_by_id("btnItems").click()
        time.sleep(1)
        v_wlcode = driver.find_elements_by_class_name("x-grid3-row")
        v_total = 0
        while v_total <= 4:
            v_wlcode[v_total].click()
            v_total += 1
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        driver.switch_to.parent_frame()
        # 订货单位编号
        driver.find_element_by_xpath("//*[@id='PartnerNum_Container']/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")
        driver.find_element_by_id("txtSearchText").send_keys("C2")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(1)
        driver.find_elements_by_class_name("x-grid3-row")[0].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(2)
        driver.switch_to.parent_frame()
        # 收货信息
        v_write_file = open(root_path() + '/PubliData/character5K.txt', 'r')
        v_lines = v_write_file.read()
        driver.find_element_by_id("txtTakeDeliverInfo").send_keys(v_lines[10:60])
        time.sleep(1)
        # 自由流审批人选择
        ClasFlow.flow_free(self, "bear")
        driver.find_element_by_id("btnSave").click()
        time.sleep(5)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "流程已触发" in i.text:
                print(i.text)
            elif "成功" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_1301_01_Add.jpg")
                print(i.text)
                unittest.expectedFailure("test_1301_01_Add")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(Order("test_1301_01_Add"))
    runner = unittest.TextTestRunner()
    runner.run(testsuit)