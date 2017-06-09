# -*- coding: utf-8 -*-

from PubliCode.onlineClass import *
from PubliCode.randData import *


class ReleaseTrue(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self,"人事管理", "培训管理", "培训记录")
        # 移动到页面顶部，防止对象遮挡
        time.sleep(3)
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM001052")

    """人事管理-培训管理-培训记录查看"""
    def test_0513_01(self):
        """人事管理-培训管理-培训记录查看"""
        driver = self.driver
        v_list = driver.find_elements_by_partial_link_text("详细")
        if len(v_list) > 0:
            v_list[0].click()
            time.sleep(6)
            driver.switch_to.default_content()
            driver.switch_to.frame("frame_tab_PM001055")
            v_button = driver.find_elements_by_tag_name("button")
            for i in v_button:
                if i.text == "查询":
                    print("培训记录查看，详情页面OK")
                    break
                else:
                    print("培训记录查看 BUG")
                    unittest.expectedFailure("test_0513_01")
        else:
            print("列表无数据")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(ReleaseTrue("test_0513_01"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)