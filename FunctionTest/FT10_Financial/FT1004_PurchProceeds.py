
from PubliCode.onlineClass import *
from selenium.webdriver.common.action_chains import ActionChains


class PurchProceeds(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "财务管理", "财务收款")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM001099")

    '''财务管理-财务收款'''
    def test_1004_01_way(self):
        """财务管理-财务收款-金额为空校验付款方式"""
        driver = self.driver
        driver.find_element_by_id("btnPay").click()
        time.sleep(2)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "金额不能为空" in i.text:
                print(i.text)
            else:
                print(i.text)
                unittest.expectedFailure("test_1004_01_way")

    '''财务管理-财务收款-查询功能'''
    def test_1004_02_query(self):
        """财务管理-财务收款-查询功能"""
        driver = self.driver
        driver.find_element_by_id("btnSearch").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")
        driver.find_element_by_id("gpSelect").click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(2)
        driver.switch_to.parent_frame()
        v_list = driver.find_elements_by_class_name("x-grid3-row")
        if len(v_list) > 0:
            print("单据查询数据正常显示")
        else:
            unittest.expectedFailure("test_1004_02_query")
            print("BUG-单据查询数据不正常")
            driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_1004_02_query.jpg")

    '''财务管理-财务收款-新增功能'''
    def test_1004_03_add(self):
        """财务管理-财务收款-单据新增"""
        driver = self.driver
        driver.find_element_by_xpath("//*[@id='txtCardCode_Container']/div/span").click()
        time.sleep(3)
        # 切换到业务伙伴选择窗体
        driver.switch_to.frame("winAdd_IFrame")
        driver.find_element_by_id("txtCodeWhere").send_keys("C")
        driver.find_element_by_id("Button2").click()
        time.sleep(2)
        driver.find_elements_by_class_name("x-grid3-row")[1].click()
        driver.find_element_by_id("Button13").click()
        time.sleep(3)
        driver.switch_to.parent_frame()
        v_check = driver.find_elements_by_class_name("x-grid3-row-checker")
        if len(v_check) > 0:
            v_check[0].click()
            v_tim = time.strftime("%Y-%m-%d %H:%M:%S")
            driver.find_element_by_id("btnPay").click()
            time.sleep(2)
            driver.find_element_by_id("txtTrsfrRef").send_keys("自动收款" + v_tim)
            driver.find_element_by_id("btnCopyTrsfrSum").click()
            driver.find_element_by_id("btnWindowOK").click()
            time.sleep(2)
            driver.find_element_by_id("txtRemarks").send_keys("Python自动收款" + v_tim)
            driver.find_element_by_id("btnSave").click()
            time.sleep(3)
            v_tip = driver.find_elements_by_class_name("ext-mb-text")
            for i in v_tip:
                if "成功" in i.text:
                    print(i.text)
                else:
                    print(i.text)
                    unittest.expectedFailure("test_1004_03_add")
        else:
            print("收款列表为空，不用收款")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(PurchProceeds("test_050509_01_Add"))
    runner = unittest.TextTestRunner()
    runner.run(testsuit)