
from PubliCode.onlineClass import *
from PubliCode.randData import *
'''
    *   Arvin
    *   2017-01-13
'''


class WorkTask(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        ClasMenu.menu_full_text(self,"个人事务", "任务管理", "工作任务")
        driver.switch_to.frame("frame_tab_PM000795")

    # 个人事务-任务管理-工作任务
    def test_0210(self):
        """个人事务-任务管理-工作任务查看流程进度跟踪"""
        driver = self.driver
        v_list = driver.find_elements_by_class_name("x-grid3-row")
        try:
            len(v_list) != 0
            v_list[random.randint(0, len(v_list) - 1)].click()
            try:
                driver.find_element_by_id("btnLook").is_displayed()
                driver.find_element_by_id("btnLook").click()
                time.sleep(3)
                for i in driver.find_elements_by_class_name("x-window-header-text"):
                    if i.text == "查看任务":
                        print("查看任务,查看页面显示OK")
                        break
            except ImportError:
                pass
        except ImportError:
            pass
            print("工作任务，列表无数据可操作")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(WorkTask("test_0210"))

    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)