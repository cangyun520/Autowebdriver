
from PubliCode.onlineClass import *
from PubliCode.randData import *


class Dump(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "库存管理", "转储管理", "库存转储")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000214")
        # 排除自定义字段遮挡干扰
        ClasForm.form_field_hide(self)

    '''库存管理-库存转储'''
    def test_2203_01_Add(self):
        """库存管理-库存转储-新增单据功能"""
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
        # 到仓库
        driver.find_element_by_xpath("//*[@id='tfToWas_Container']/div/span").click()
        time.sleep(2)
        driver.switch_to.frame("winAdd_IFrame")
        driver.find_elements_by_class_name("x-grid3-row")[3].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
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
        v_wlcode = driver.find_elements_by_class_name("x-grid3-row")
        v_total = 0
        while v_total <= 4:
            v_wlcode[v_total].click()
            v_total += 1
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        driver.switch_to.parent_frame()
        driver.find_element_by_id("txtRemark").send_keys("库存转储添加Auto" + v_tim)
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
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2203_01_Add.jpg")
                print(i.text)
                unittest.expectedFailure("test_2203_01_Add")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    unittest.main()