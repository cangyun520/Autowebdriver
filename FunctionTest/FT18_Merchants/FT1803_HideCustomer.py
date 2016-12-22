from PubliCode.onlineClass import *
from PubliCode.randData import *


class HideCustomer(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "销售管理", "客商管理", "潜在客户主数据")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000734")

    # --客商管理---潜在客户主数据
    def test_1803_01_Add(self):
        """客商管理-潜在客户主数据-单据取消功能"""
        driver = self.driver
        v_tim = time.strftime("%y%m%d%H%M%S")
        # 客户代码
        driver.find_element_by_id("txtCardCode").send_keys("LA" + str(random.randint(1000, 9000)))
        # 客户名称
        driver.find_element_by_id("txtCardName").send_keys("潜在客户Auto" + v_tim + "技术公司")
        # 外文名称
        driver.find_element_by_id("txtCardFName").send_keys("CustomerAuto" + v_tim)
        # 组
        driver.find_element_by_xpath("//*[@id='tfGroupCode_Container']/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")
        v_khlist = driver.find_elements_by_class_name("x-grid3-row")
        v_khlist[random.randint(0, len(v_khlist) - 1)].click()
        driver.find_element_by_id("Button1").click()
        time.sleep(1)
        driver.switch_to.parent_frame()
        # 电话，传真，站点
        driver.find_element_by_id("txtPhone1").send_keys("027-" + str(random.randint(111111, 999999)))
        driver.find_element_by_id("txtPhone2").send_keys("010-" + str(random.randint(111111, 999999)))
        driver.find_element_by_id("txtFax").send_keys("010-" + str(random.randint(111111, 999999)))
        driver.find_element_by_id("txtWebsite").send_keys("www." + "".join(random.choice("abcdefghjklmnopqrst") for i in range(6)) + ".com")
        driver.find_element_by_id("txtEmailAddress").send_keys("".join(random.choice("0123456789") for i in range(9)) + "@tech" + ".com")
        # 移动电话
        v_iphone = random.choice(
            ['139', '188', '185', '136', '158', '151'])+"".join(random.choice("0123456789") for i in range(8))
        driver.find_element_by_id("txtCellular").send_keys(v_iphone)
        # 备注
        driver.find_element_by_id("txtNotes").send_keys("自动添加的潜在客户" + v_tim)
        time.sleep(1)
        # 备注页签
        driver.find_element_by_link_text("备注").click()
        time.sleep(1)
        driver.find_element_by_id("bzjy").send_keys(fun_data_character(200, 1200))
        time.sleep(2)
        driver.find_element_by_id("btnSave").click()
        time.sleep(5)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_1803_01_Add.jpg")
                print(i.text)
                unittest.expectedFailure("test_1803_01_Add")

    # 客商管理-潜在客户主数据-单据取消功能
    def test_1803_02(self):
        """客商管理-潜在客户主数据-单据取消功能"""
        driver = self.driver
        driver.find_element_by_id("btnFirst").click()
        time.sleep(4)
        # 备注页签
        driver.find_element_by_link_text("备注").click()
        time.sleep(1)
        write_file = open(root_path() + 'PubliData/character5K.txt', 'r')
        v_lines = write_file.read()
        driver.find_element_by_id("bzjy").clear()
        driver.find_element_by_id("bzjy").send_keys(v_lines[200:1200])
        time.sleep(2)
        driver.find_element_by_id("btnSave").click()
        time.sleep(5)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_1803_02.jpg")
                print(i.text)
                unittest.expectedFailure("test_1803_02")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(HideCustomer("test_1803_01_Add"))

    runner = unittest.TextTestRunner()
    runner.run(testsuit)