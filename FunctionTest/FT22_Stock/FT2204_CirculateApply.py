
from selenium.webdriver.common.action_chains import ActionChains
from PubliCode.onlineClass import *
from PubliCode.randData import *


class CirculateApply(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "库存管理", "借料还料", "借料申请")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000871")

    '''库存管理-借料申请单'''
    def test_2204_01_Add(self):
        """库存管理-借料申请单-新增单据功能"""
        driver = self.driver
        driver.find_element_by_id("BtnAdd").click()
        time.sleep(3)
        driver.switch_to.frame("winSendInspection_IFrame")     # 切换到新增页面
        # 項目
        driver.find_element_by_xpath("//*[@id='Project_Container']/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")
        driver.find_element_by_id("txtProtect").send_keys("PRJ")
        driver.find_element_by_id("btnProtect").click()
        time.sleep(2)
        v_list_prj = driver.find_elements_by_class_name("x-grid3-row")
        if len(v_list_prj) != 0:
            v_list_prj[0].click()
            driver.find_element_by_id("Button11").click()
        else:
            driver.find_element_by_id("Button12").click()
        time.sleep(1)
        driver.switch_to.parent_frame()
        # 类型
        driver.find_element_by_id("Type").click()
        time.sleep(1)
        v_list_type = driver.find_elements_by_class_name("x-combo-list-item")
        v_list_type[random.randint(0, len(v_list_type) - 1)].click()
        time.sleep(1)
        # 业务伙伴编号
        driver.find_element_by_xpath("//*[@id='PartnerNum_Container']/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")
        driver.find_element_by_id("txtSearchText").send_keys("C")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(2)
        v_list_wl = driver.find_elements_by_class_name("x-grid3-row")
        v_list_wl[random.randint(0, len(v_list_wl) - 1)].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(1)
        driver.switch_to.parent_frame()
        # 物料信息页签
        v_wlline = driver.find_element_by_xpath(
            "//*[@id='gpBorrow']/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[2]"
        )
        ActionChains(driver).double_click(v_wlline).perform()
        time.sleep(1)
        driver.find_element_by_xpath(
            "//*[@id='gpBorrow']/div/div/div/div/div[2]/div[2]/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")     # 切换到物料选择窗体
        driver.find_element_by_id("txtSearchText").send_keys("I0000")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(1)
        for i in driver.find_elements_by_class_name("x-grid3-row"):
            i.click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        driver.switch_to.parent_frame()
        # 备注页签
        driver.find_element_by_link_text("备注").click()
        time.sleep(2)
        driver.find_element_by_id("Remark").send_keys(fun_data_character(100, 1000))
        time.sleep(1)
        driver.find_element_by_id("btnSave").click()
        time.sleep(5)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "单据添加成功" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2204_01_Add.jpg")
                print(i.text)
                unittest.expectedFailure("test_2204_01_Add")

    '''库存管理-借料申请单-单据复制到功能'''
    def test_2204_02_goto(self):
        """库存管理-借料申请单-单据复制到功能"""
        driver = self.driver
        driver.find_element_by_id("BtnAdd").click()
        time.sleep(3)
        driver.switch_to.frame("winSendInspection_IFrame")     # 切换到新增页面
        driver.find_element_by_id("btnLast").click()
        time.sleep(3)
        if driver.find_element_by_id("btnCopyTo").is_displayed():
            driver.find_element_by_id("btnCopyTo").click()
            time.sleep(1)
            driver.find_element_by_link_text("借料单").click()
            time.sleep(4)
            driver.switch_to.default_content()
            driver.switch_to.frame("frame_tab_PM000884")
            driver.find_element_by_xpath("//*[@id='OutWarehouse_Container']/div/span").click()
            time.sleep(3)
            driver.switch_to.frame("winAdd_IFrame")
            driver.find_elements_by_class_name("x-grid3-row")[0].click()
            driver.find_element_by_id("btnSelect").click()
            time.sleep(2)
            driver.switch_to.parent_frame()
            driver.find_element_by_id("btnSave").click()
            time.sleep(4)
            v_tip = driver.find_elements_by_class_name("ext-mb-text")
            for i in v_tip:
                if "成功" in i.text:
                    print(i.text)
                elif "流程已触发" in i.text:
                    print(i.text)
                else:
                    driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2204_02_goto.jpg")
                    print(i.text)
                    unittest.expectedFailure("test_2204_02_goto")
        else:
            print("库存转储申请-单据已清，无复制到选项")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    unittest.main()