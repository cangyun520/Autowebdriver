# -*- coding: utf-8 -*-
from PubliCode.config import *
from PubliCode.onlineClass import *
from PubliCode.randData import *
'''
    *   Arvin
    *   2017-01-13
'''


class NewsManage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        # self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "行政办公", "新闻公告", "新闻公告类型")
        driver.switch_to.frame("frame_tab_PM000288")

    """行政办公-通知公告-新闻类型添加"""
    def test_0407_01_Add(self):
        """行政办公-通知公告-新闻类型添加"""
        driver = self.driver
        driver.find_element_by_partial_link_text("新增").click()
        time.sleep(2)
        v_tim = time.strftime("%Y%m%d%H%M")
        driver.find_element_by_id("typename").send_keys("类型" + v_tim)
        driver.find_element_by_id("btnSelect").click()
        time.sleep(2)
        msg = driver.find_elements_by_class_name("bootbox-body")
        for i in msg:
            if "添加成功" in i.text:
                print(i.text)
            elif "类名已存在" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/oa/test_0407_01_Add.jpg")
                print(i.text)
                unittest.expectedFailure("test_050502_01_Add")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(NewsManage("test_0407_01_Add"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)