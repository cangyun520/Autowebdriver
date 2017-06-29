
from PubliCode.onlineClass import *
from PubliCode.randData import *


class DumpApply(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        ClasMenu.menu_full_text(self, "库存管理", "转储管理", "库存转储申请")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000736")
        # 排除自定义字段遮挡干扰
        ClasForm.form_field_hide(self)

    '''库存管理---库存转储申请'''
    def test_2202_01(self):
        """库存管理-库存转储申请-新增单据功能"""
        driver = self.driver
        driver.find_element_by_xpath("//*[@id='txtBuyer_Container']/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")     # 切换到业务伙伴选择窗体
        driver.find_element_by_id("txtBPartners").send_keys("C")
        driver.find_element_by_id("Button6").click()
        time.sleep(2)
        driver.find_elements_by_class_name("x-grid3-row")[random.randint(0, 4)].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        v_tim = time.strftime("%Y-%m-%d %H:%M:%S")
        driver.switch_to.parent_frame()
        # 行物料选择
        driver.find_element_by_xpath(
            "//*[@id='GridPanelNR']/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath(
            "//*[@id='GridPanelNR']/div/div/div/div/div[2]/div[2]/div/span").click()
        time.sleep(2)
        driver.switch_to.frame("winAdd_IFrame")     # 切换到物料选择窗体
        driver.find_element_by_id("txtItems").send_keys("A000")
        driver.find_element_by_id("btnItems").click()
        time.sleep(1)
        driver.find_elements_by_class_name("x-grid3-row")[0].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        driver.switch_to.parent_frame()
        time.sleep(1)
        # 到仓库
        v_dckcode = driver.find_elements_by_class_name("x-grid3-td-WarehouseCode")
        v_dckcode[1].click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='GridPanelNR']/div/div/div/div/div[2]/div[3]/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")
        driver.find_elements_by_class_name("x-grid3-row")[3].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        driver.switch_to.parent_frame()
        driver.find_element_by_id("txtRemark").send_keys("库存转储申请添加Auto" + v_tim)
        driver.find_element_by_id("btnSave").click()
        time.sleep(4)
        ClasForm.form_top(self, 0)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功" in i.text:
                print(i.text)
            elif "流程已触发" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2202_01.jpg")
                print(i.text)
                unittest.expectedFailure("test_2202_01")

    '''库存管理-库存转储申请-单据复制到功能'''
    def test_2202_02_goto(self):
        """库存管理-库存转储申请-单据复制到功能"""
        driver = self.driver
        driver.find_element_by_id("btnLast").click()
        time.sleep(3)
        try:
            driver.find_element_by_id("btnCopyTo").is_displayed()
            driver.find_element_by_id("btnCopyTo").click()
            time.sleep(1)
            driver.find_element_by_link_text("库存转储").click()
            time.sleep(4)
            driver.switch_to.default_content()
            driver.switch_to.frame("frame_tab_PM000214")
            driver.find_element_by_id("btnSave").click()
            time.sleep(4)
            v_tip = driver.find_elements_by_class_name("ext-mb-text")
            for i in v_tip:
                if "成功" in i.text:
                    print(i.text)
                elif "流程已触发" in i.text:
                    print(i.text)
                else:
                    driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2202_02_goto.jpg")
                    print(i.text)
                    unittest.expectedFailure("test_2202_02_goto")
        except ImportError:
            print("库存转储申请-单据已清，无复制到选项")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    unittest.main()