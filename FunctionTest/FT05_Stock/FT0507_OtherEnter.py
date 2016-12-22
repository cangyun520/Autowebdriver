
from PubliCode.onlineClass import *
from PubliCode.randData import *


class OtherEnter(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "库存管理", "其他出入库", "其他入库")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000207")
        # 排除自定义字段遮挡干扰
        ClasForm.form_field_hide(self, driver)

    # 库存管理---其他入库
    def test_0507_01_Add(self):
        """库存管理-其他入库-新增单据功能"""
        driver = self.driver
        driver.find_element_by_xpath("//*[@id='tfName_Container']/div/span").click()        # 库存收发货类型
        time.sleep(3)
        driver.switch_to_frame("winAdd_IFrame")
        driver.find_elements_by_class_name("x-grid3-row")[0].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(1)
        v_tim = time.strftime("%Y-%m-%d %H:%M:%S")
        driver.switch_to.parent_frame()
        # 行物料
        driver.find_element_by_xpath(
            "//*[@id='GridPanelNR']/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath(
            "//*[@id='GridPanelNR']/div/div/div/div/div[2]/div[2]/div/span").click()
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
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        driver.switch_to.parent_frame()
        driver.find_element_by_id("txtRemark").send_keys("其他入库添加Auto" + v_tim)
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
                driver.get_screenshot_as_file(root_path() + "TestPicture/test_0507_01_Add.jpg")
                print(i.text)
                unittest.expectedFailure("test_0507_01_Add")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()