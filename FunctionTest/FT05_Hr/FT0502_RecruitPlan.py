# -*- coding: utf-8 -*-
from PubliCode.onlineClass import *
from PubliCode.randData import *


class RecruitPlan(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        # self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self,"人事管理", "招聘管理", "招聘需求与计划")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM001012")

    """人事管理-招聘管理-招聘需求与计划查看"""
    def test_0502_01(self):
        """人事管理-招聘管理-招聘需求与计划查看"""
        driver = self.driver
        v_list = driver.find_elements_by_link_text("查看")
        if len(v_list) > 0:
            v_list[0].click()
            time.sleep(3)
            try:
                driver.find_element_by_id("btnCancel").is_displayed()
            except:
                print("点击查看后页面没有找到【取消】按钮")
                unittest.expectedFailure("test_0502_01")
            else:
                driver.find_element_by_id("btnCancel").click()
                time.sleep(2)
            try:
                driver.find_element_by_id("btnAdd").is_displayed()
            except :
                print("详情页面【取消】按钮点击无效")
                unittest.expectedFailure("test_0502_01")
            else:
                print("招聘需求与计划数据查看，与详情页面关闭OK")
        else:
            print("列表无数据")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(RecruitPlan("test_0502_01"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)