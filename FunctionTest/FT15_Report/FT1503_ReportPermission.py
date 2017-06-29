
from PubliCode.onlineClass import *
from PubliCode.randData import *


class ReportPermission(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, u"系统管理", u"报表设置", u"报表权限")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000180")

    """系统管理-报表设置-报表权限分配"""
    def test_1503_01_set(self):
        """系统管理-报表设置-报表权限分配"""
        driver = self.driver
        v_list = driver.find_elements_by_class_name("x-grid3-row")
        for i in v_list:
            if "超级管理员" in i.text:
                i.click()
                break
                time.sleep(2)
        driver.find_element_by_class_name("x-grid3-hd-checker").click()
        time.sleep(1)
        driver.find_element_by_id("btnSave").click()
        time.sleep(2)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "保存成功" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/Report/test_1503_01_set.jpg")
                unittest.expectedFailure("test_1503_01_set")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(ReportPermission("test_0904_01_set"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)