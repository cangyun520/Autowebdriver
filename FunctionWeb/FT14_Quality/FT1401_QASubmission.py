from PubliCode.webClass import *


class QASubmission(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "采购管理", "质检", "送检单")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000831")

    '''采购管理-送检单-新增单据功能'''
    def test_1401_01(self):
        """采购管理-送检单-新增单据功能"""
        driver = self.driver
        driver.find_element_by_id("BtnAdd").click()
        time.sleep(5)
        # 进入添加界面
        driver.switch_to.frame("winSendInspection_IFrame")
        driver.find_element_by_id("cbInspectionType").click()
        v_check = driver.find_elements_by_class_name("x-combo-list-item")
        v_check[0].click()
        time.sleep(1)
        driver.find_element_by_class_name("x-form-twin-triggers").find_element_by_id("ext-gen91").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")     # 切换到订单信息选择窗体
        driver.find_element_by_id("gpSelect").click()
        driver.find_element_by_id("Button1").click()
        time.sleep(3)
        driver.switch_to.default_content()
        driver.switch_to.frame("frame_tab_PM000831")
        driver.switch_to.frame("winSendInspection_IFrame")
        driver.find_element_by_id("ext-comp-1015").click()
        time.sleep(2)
        driver.find_element_by_id("btnSave").click()
        time.sleep(5)
        driver.switch_to.parent_frame()
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "添加成功" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_050610_01_Add.jpg")
                print(i.text)
                unittest.expectedFailure("test_050610_01_Add")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(QASubmission("test_1401_01"))
    runner = unittest.TextTestRunner()
    runner.run(testsuit)