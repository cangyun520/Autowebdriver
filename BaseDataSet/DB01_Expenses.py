
from PubliCode.onlineClass import *


class Expenses(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)

    # 业务设置-费用设置-类型添加
    def test_DB01_01_ApplyAdd(self):
        """业务设置-费用设置-类型添加"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "系统管理", "业务设置", "费用设置", "报销类型设置")
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000762")
        driver.find_element_by_id("btnAdd").click()
        time.sleep(2)
        v_tim = time.strftime("%m%d%H%M")
        driver.find_element_by_id("Type").send_keys("费用类型" + v_tim)
        driver.find_element_by_id("Digest").send_keys("全选菜单Auto" + v_tim)
        # 关联菜单
        driver.find_element_by_class_name("x-form-twin-triggers").find_element_by_id("ext-gen65").click()
        time.sleep(3)
        driver.switch_to_frame("winTypeAdd_IFrame")
        v_check = driver.find_elements_by_class_name("x-grid3-row-checker")
        for i in v_check:
            i.click()
        time.sleep(1)
        driver.find_element_by_id("Button1").click()
        time.sleep(2)
        driver.switch_to.parent_frame()
        # 科目代码
        driver.find_element_by_xpath("//*[@id='x-form-el-AcctCode']/div/span").click()
        time.sleep(3)
        driver.switch_to_frame("winTypeAdd_IFrame")
        driver.find_element_by_id("txtBPartners").send_keys("100201")
        driver.find_element_by_id("btnBPartners").click()
        time.sleep(1)
        for i in driver.find_elements_by_class_name("x-grid3-cell-inner"):
            i.click()
            break
        driver.find_element_by_id("Button1").click()
        time.sleep(2)
        driver.switch_to.parent_frame()
        driver.find_element_by_id("BtnSaveForm").click()
        time.sleep(2)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功！" in i.text:
                print(i.text)
            else:
                print(i.text)
                unittest.expectedFailure("test_DB01_01_ApplyAdd")

    # 费用设置-财务设置-报销金额添加
    def test_DB01_02_FinanceAdd(self):
        """费用设置-财务设置-报销金额添加"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "系统管理", "业务设置", "费用设置", "财务设置")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000763")
        driver.find_element_by_id("btnSave").click()
        time.sleep(2)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功！" in i.text:
                print(i.text)
            else:
                print(i.text)
                unittest.expectedFailure("test_DB01_02_FinanceAdd")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    unittest.main()
