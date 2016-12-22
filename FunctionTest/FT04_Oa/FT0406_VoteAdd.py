
from PubliCode.onlineClass import *
from PubliCode.randData import *


class VoteAdd(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "行政办公", "投票管理", "创建投票")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000487")

    # 行政办公-创建投票-单选投票添加
    def test_0406_01_add(self):
        """行政办公-创建投票-单选投票添加功能"""
        driver = self.driver
        driver.find_element_by_id("btnCreateVote").click()
        v_tim = time.strftime("%Y%m%d%H%M")
        driver.find_element_by_id("txtVoteTitle").send_keys("单选投票" + v_tim)
        driver.find_element_by_id("btnVoteSave").click()
        time.sleep(3)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "添加成功" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/oa/test_0406_01_add.jpg")
                print(i.text)
                unittest.expectedFailure("test_0406_01_add")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    unittest.main()
    """# 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(VoteAdd("test_0406_01_add"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)
    """