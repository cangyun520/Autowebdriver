
from PubliCode.onlineClass import *
from PubliCode.randData import *


class QAWait(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "采购管理", "质检", "待检管理")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000833")

    '''质检管理-待检管理-分配质检员'''
    def test_1402_01(self):
        """质检管理-待检管理-分配质检员功能"""
        driver = self.driver
        driver.find_elements_by_class_name("x-grid3-row")[0].click()
        time.sleep(1)
        driver.find_element_by_id("BtnAdd").click()     # 分配质检员
        time.sleep(3)
        driver.switch_to.frame("winSendInspection_IFrame")
        v_user = driver.find_elements_by_class_name("x-grid3-row")
        v_user[random.randint(0, len(v_user) - 1)].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        driver.switch_to.parent_frame()
        ClasForm.form_button_yes(self, "确定")
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "分配成功" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_1402_01.jpg")
                print(i.text)
                unittest.expectedFailure("test_1402_01")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(QAWait("test_1402_01"))
    runner = unittest.TextTestRunner()
    runner.run(testsuit)