
from selenium.webdriver.common.action_chains import ActionChains
from PubliCode.onlineClass import *
from PubliCode.randData import *


class Circulate(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "库存管理", "借料还料", "借料")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000883")

    # 库存管理---借料单
    def test_0505_01_Add(self):
        """库存管理-借料申请-新增单据功能"""
        driver = self.driver
        driver.find_element_by_id("btnAdd").click()
        time.sleep(3)
        driver.switch_to_frame("winSendInspection_IFrame")     # 切换到新增页面
        v_list_wl = driver.find_element_by_xpath(
            "//*[@id='gpBorrow']/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[2]"
        )
        ActionChains(driver).double_click(v_list_wl).perform()
        time.sleep(1)
        driver.find_element_by_xpath(
            "//*[@id='gpBorrow']/div/div/div/div/div[2]/div[2]/div/span").click()
        time.sleep(3)
        driver.switch_to_frame("winAdd_IFrame")     # 切换到物料选择窗体
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
        # 借出仓库
        driver.find_element_by_xpath("//*[@id='OutWarehouse_Container']/div/span").click()
        time.sleep(3)
        driver.switch_to_frame("winAdd_IFrame")
        driver.find_elements_by_class_name("x-grid3-row")[0].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(2)
        driver.switch_to.parent_frame()
        driver.find_element_by_id("btnSave").click()
        time.sleep(5)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "单据添加成功" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_0505_01_Add.jpg")
                print(i.text)
                unittest.expectedFailure("test_0505_01_Add")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(Circulate("test_0505_01_Add"))

    runner = unittest.TextTestRunner()
    runner.run(testsuit)