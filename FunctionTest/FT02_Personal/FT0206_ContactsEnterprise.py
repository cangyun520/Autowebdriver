
from PubliCode.onlineClass import *
from PubliCode.randData import *
'''
    *   Arvin
    *   2017-01-13
'''


class ContactsEnterprise(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self,"个人事务", "通讯录", "企业通讯录")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000295")

    # 个人事务-企业通讯录-站内信发送功能
    def test_0206_01_add(self):
        """个人事务-企业通讯录-站内信发送功能"""
        driver = self.driver
        v_list = driver.find_elements_by_class_name("row-imagecommand")
        v_list[random.randint(1, len(v_list) - 1)].click()
        time.sleep(3)
        driver.switch_to.default_content()
        driver.switch_to.frame("frame_tab_PM001067")
        v_write_file = open(root_path() + 'PubliData/character5K.txt', 'r')
        v_lines = v_write_file.read()
        v_tim = time.strftime("%Y-%m-%d %H:%M:%S")
        driver.find_element_by_id("txt_title").send_keys(v_tim + "消息标题Auto")
        v_content = "//*[@id='ngSection']/div[1]/div/div/div/div/div/div[1]/div[3]/div/div[2]/div[4]/div[3]"
        driver.find_element_by_xpath(v_content).send_keys(v_tim + v_lines[10:200])
        time.sleep(2)
        driver.find_element_by_id("btnsave").click()
        time.sleep(3)
        ClasForm.form_top(self, 0)
        v_tip = driver.find_elements_by_class_name("bootbox-body")
        for i in v_tip:
            if "发送成功" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/oa/test_0206_01_add.jpg")
                print(i.text)
                unittest.expectedFailure("test_0206_01_add")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(ContactsEnterprise("test_0206_01_add"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)