
from PubliCode.onlineClass import *
from PubliCode.randData import *
from selenium.webdriver.common.action_chains import ActionChains


class SalesLeads(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "客户关系", "售前管理", "销售机会")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM001072")

    """CRM-售前管理-销售机会-新增单据功能"""
    def test_1202_01_Add(self):
        """CRM-售前管理-销售机会-新增单据功能"""
        driver = self.driver
        # 进入到新增页面
        driver.find_element_by_id("btnAdd").click()
        time.sleep(3)
        driver.switch_to.default_content()
        driver.switch_to.frame("frame_tab_PM000316")
        v_tim = time.strftime("%Y-%m-%d %H:%M:%S")
        # 进入到添加页面
        driver.find_element_by_xpath("//*[@id='CompositeField2_Container']/div/div/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")
        driver.find_element_by_id("txtSearchText").send_keys("C")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(2)
        driver.find_elements_by_class_name("x-grid3-row")[random.randint(0, 8)].click()
        driver.find_element_by_id("btnSelect").click()
        driver.switch_to.parent_frame()
        time.sleep(1)
        # 销售机会
        driver.find_element_by_id("Name").send_keys("销售机会" + v_tim)
        v_lines = driver.find_element_by_xpath("//*[@id='gpOPR1']")
        ActionChains(driver).context_click(v_lines).perform()
        driver.find_element_by_link_text("添加行").click()
        time.sleep(1)
        # ------阶段页签------
        # 阶段-开始日期
        v_date_start = driver.find_element_by_xpath(
            "//*[@id='gpOPR1']/div/div/div/div/div[2]/div/div/table/tbody/tr/td[2]"
        )
        ActionChains(driver).double_click(v_date_start).perform()
        time.sleep(1)
        ClasForm.form_today(self, "DateField1")
        time.sleep(1)
        # 阶段-结算日期
        v_date_end = driver.find_element_by_xpath(
            "//*[@id='gpOPR1']/div/div/div/div/div[2]/div/div/table/tbody/tr/td[3]"
        )
        ActionChains(driver).double_click(v_date_end).perform()
        time.sleep(1)
        ClasForm.form_today_line(self, "DateField4")
        time.sleep(1)
        # 销售员
        v_date_saler = driver.find_element_by_xpath(
            "//*[@id='gpOPR1']/div/div/div/div/div[2]/div/div/table/tbody/tr/td[4]"
        )
        ActionChains(driver).double_click(v_date_saler).perform()
        time.sleep(1)
        v_saler = driver.find_element_by_xpath(
            "//*[@id='gpOPR1']/div/div/div/div/div[2]/div[4]/div/span"
        )
        ActionChains(driver).click(v_saler).perform()
        time.sleep(3)
        v_line_saler = driver.find_elements_by_class_name("x-grid3-row")
        v_line_saler[1].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(2)
        # 阶段


        # 到达地点
        v_add_end = driver.find_element_by_xpath(
            "//*[@id='gpOPR1']/div/div/div/div/div[2]/div/div/table/tbody/tr/td[5]"
        )
        ActionChains(driver).double_click(v_add_end).perform()
        time.sleep(1)
        driver.switch_to.active_element.send_keys(fun_data_city())
        # 报销项目
        v_add_end = driver.find_element_by_xpath(
            "//*[@id='gpOPR1']/div/div/div/div/div[2]/div/div/table/tbody/tr/td[6]"
        )
        ActionChains(driver).double_click(v_add_end).perform()
        time.sleep(1)
        driver.find_element_by_xpath(
            "//*[@id='ext-comp-1006']/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")
        v_type = driver.find_elements_by_class_name("x-grid3-row")
        v_type[random.randint(0, len(v_type)-1)].click()
        driver.find_element_by_id("Button1").click()
        time.sleep(1)
        driver.switch_to.parent_frame()
        # 金额
        v_money = driver.find_element_by_xpath(
            "//*[@id='gpOPR1']/div/div/div/div/div[2]/div/div/table/tbody/tr/td[8]"
        )
        ActionChains(driver).double_click(v_money).perform()
        time.sleep(1)
        driver.switch_to.active_element.send_keys(random.randint(100, 9999))







        # 主题
        driver.find_element_by_id("subject").send_keys(fun_data_character(100, 200))
        driver.find_element_by_id("btnSave").click()
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功" in i.text:
                print(i.text)
            else:
                print(i.text)
                unittest.expectedFailure("test_1202_01_Add")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(SalesLeads("test_1202_01_Add"))
    runner = unittest.TextTestRunner()
    runner.run(testsuit)