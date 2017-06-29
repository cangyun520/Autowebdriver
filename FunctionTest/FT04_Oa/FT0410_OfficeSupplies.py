# -*- coding: utf-8 -*-

from PubliCode.onlineClass import *
from PubliCode.randData import *
'''
    *   Arvin
    *   2017-01-13
'''


class OfficeSupplies(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        # self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "行政办公", "办公用品管理")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000796")

    '''行政办公-办公用品管理-单据添加功能'''

    def test_0410_01_add(self):
        """行政办公-办公用品管理-单据添加功能"""
        driver = self.driver
        v_add = driver.find_element_by_id("btnAdd")
        if v_add.is_displayed():
            v_tim = time.strftime("%y%m%d%H%M")
            v_add.click()
            time.sleep(2)
            driver.find_element_by_id("txtNam").send_keys("办公用品" + v_tim)
            time.sleep(1)
            # 单位
            driver.find_element_by_id("txtUnit").send_keys("件")
            time.sleep(1)
            # 单价
            driver.find_element_by_id("txtPrice").send_keys(random.randint(10, 500))
            time.sleep(1)
            # 供应商
            driver.find_element_by_id("txtSuppies").send_keys("供应商" + v_tim)
            time.sleep(1)
            # 当前库存
            driver.find_element_by_id("numfiCount").send_keys(random.randint(1, 10000))
            time.sleep(1)
            # 办公用品描述
            v_description = "Python自动化输入“办公用品描述”字符，当前添加时间："
            driver.find_element_by_id("txtDescription").send_keys(v_description + v_tim)
            time.sleep(2)
            driver.find_element_by_id("BtnSaveForm").click()
            time.sleep(2)
            try:
                driver.find_element_by_id("ext-gen145").is_displayed()
                print("行政办公-办公用品管理添加数据成功")
            except ImportError:
                print("BUG 行政办公-办公用品管理添加数据失败，请检查页面")
        else:
            print("BUG 行政办公-办公用品管理-【添加】-不显示，请检查页面是否正常")
            unittest.expectedFailure("test_0410_01_add")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(OfficeSupplies("test_0410_01_add"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)