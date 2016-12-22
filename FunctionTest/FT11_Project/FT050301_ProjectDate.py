
from PubliCode.onlineClass import *
from PubliCode.randData import *


class ProjectDate(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "项目管理", "项目主数据")
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000753")

    # 项目管理-项目主数据-同步项目主数据功能
    def test_050301_ProjectDate(self):
        """项目管理-项目主数据-同步项目主数据功能"""
        driver = self.driver
        driver.find_element_by_id("btnProjectAdd").click()
        time.sleep(3)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "已经保持相同记录" in i.text:
                print(i.text)
            elif "同步项目信息成功" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_050301_ProjectDate.jpg")
                print(i.text)
                unittest.expectedFailure("test_050301_ProjectDate")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(ProjectDate("test_050301_ProjectDate"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)