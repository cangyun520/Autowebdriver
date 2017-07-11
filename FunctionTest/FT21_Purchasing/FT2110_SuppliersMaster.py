
from PubliCode.onlineClass import *
from PubliCode.randData import *


class SuppliersMaster(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        ClasMenu.menu_full_text(self, "采购管理", "供应商主数据")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000417")

    """客商管理-供应商主数据-新增单据功能"""
    def test_2110_01_Add(self):
        """客商管理-供应商主数据-新增单据功能"""
        driver = self.driver
        v_tim = time.strftime("%y%m%d%H%M%S")
        # 供应商代码
        driver.find_element_by_id("txtCardCode").send_keys("VA" + str(random.randint(1000, 9000)))
        # 供应商名称
        driver.find_element_by_id("txtCardName").send_keys("供应商Auto" + v_tim + "有限公司")
        # 外文名称
        driver.find_element_by_id("txtCardFName").send_keys("Suppliers" + v_tim)
        # 组
        driver.find_element_by_xpath("//*[@id='tfGroupCode_Container']/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")
        v_gyslist = driver.find_elements_by_class_name("x-grid3-row")
        v_gyslist[random.randint(0, len(v_gyslist) - 1)].click()
        driver.find_element_by_id("Button1").click()
        time.sleep(1)
        driver.switch_to.parent_frame()
        # 电话，传真，站点
        driver.find_element_by_id("txtPhone1").send_keys("021-" + str(random.randint(111111, 999999)))
        driver.find_element_by_id("txtPhone2").send_keys("028-" + str(random.randint(111111, 999999)))
        driver.find_element_by_id("txtFax").send_keys("010-" + str(random.randint(111111, 999999)))
        driver.find_element_by_id(
            "txtWebsite").send_keys("www." + "".join(random.choice("abcdefghjklmnopqrst") for i in range(6)) + ".com")
        driver.find_element_by_id(
            "txtEmailAddress").send_keys("".join(random.choice("0123456789") for i in range(9)) + "@tech" + ".com")
        # 移动电话
        v_iphone = random.choice(
            ['139', '188', '185', '136', '158', '151'])+"".join(random.choice("0123456789") for i in range(8))
        driver.find_element_by_id("txtCellular").send_keys(v_iphone)
        # 备注
        driver.find_element_by_id("txtNotes").send_keys("自动添加的供应商" + v_tim)
        time.sleep(1)
        # 备注页签
        driver.find_element_by_link_text("备注").click()
        time.sleep(1)
        driver.find_element_by_id("bzjy").send_keys(fun_data_character(600, 700))
        time.sleep(2)
        driver.find_element_by_id("btnSave").click()
        time.sleep(5)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2110_01_Add.jpg")
                print(i.text)
                unittest.expectedFailure("test_2110_01_Add")

    """客商管理-供应商主数据-更新功能"""
    def test_2110_02(self):
        """客商管理-供应商主数据-更新功能"""
        driver = self.driver
        driver.find_element_by_id("btnFirst").click()
        time.sleep(4)
        # 备注页签
        driver.find_element_by_link_text("备注").click()
        time.sleep(1)
        driver.find_element_by_id("bzjy").clear()
        driver.find_element_by_id("bzjy").send_keys(fun_data_character(100, 1000))
        time.sleep(2)
        driver.find_element_by_id("btnSave").click()
        time.sleep(5)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        if len(v_tip) == 0:
            print("没有获取到提示窗体")
            unittest.expectedFailure("test_2110_02")
        else:
            for i in v_tip:
                if "成功" in i.text:
                    print(i.text)
                else:
                    driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2110_02.jpg")
                    print("Error：" + i.text)
                    unittest.expectedFailure("test_2110_02")

    '''采购管理-供应商主数据-查询功能'''
    def test_2110_03_query(self):
        """采购管理-供应商主数据-查询功能"""
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
            unittest.expectedFailure("test_2110_03_query")
            print("BUG-单据查询数据不正常")
            driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_2110_03_query.jpg")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    unittest.main()