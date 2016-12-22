from selenium.webdriver.common.action_chains import ActionChains
from PubliCode.onlineClass import *
from PubliCode.randData import *


class MaterialMaster(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "库存管理", "物料主数据管理")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000911")

    # 库存管理---物料主数据管理
    def test_0501_01_add(self):
        """物料主数据管理-物料主数据管理-新增物料功能"""
        driver = self.driver
        v_tim = time.strftime("%y%m%d%H%M%S")
        driver.find_element_by_id("btnSingleAdd").click()
        time.sleep(3)
        driver.switch_to_frame("winActivity_IFrame")     # 切换到新增物料页面
        # 物料编号
        v_wlcode = random.choice(
            ['CA', 'IA', 'LA', 'SA', 'HA', 'PA'])+"".join(random.choice("0123456789") for i in range(8))
        driver.find_element_by_id("txtMarCode").send_keys(v_wlcode)
        # 条形码
        driver.find_element_by_id("txtBarCode").send_keys("TXM" + v_tim)
        # 物料描述
        driver.find_element_by_id("txtDepict").send_keys("物料Auto" + v_tim)
        driver.find_element_by_id("txtEDepict").send_keys("MaterialMaster" + v_tim)
        # 单价
        driver.find_element_by_id("txtPrice").send_keys(random.randint(50, 5000))
        # 保修模板
        driver.find_element_by_xpath("//*[@id='txtTemplet_Container']/div/span").click()
        time.sleep(3)
        driver.switch_to_frame("winAdd_IFrame")     # 切换保修模板选择窗体
        v_template = driver.find_elements_by_class_name("x-grid3-row")
        v_template[random.randint(0, len(v_template) - 1)].click()
        driver.find_element_by_id("Button1").click()
        time.sleep(2)
        driver.switch_to.parent_frame()
        # 附加标识
        driver.find_element_by_id("txtIdentification").send_keys("自动添加的物料Auto。这是测试说的" + v_tim)
        # 采购数据页签
        driver.find_element_by_link_text("采购数据").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='txtFirstSupplier_Container']/div/span").click()
        time.sleep(3)
        driver.switch_to_frame("winAdd_IFrame")     # 切换供应商选择窗体
        v_suppliers = driver.find_elements_by_class_name("x-grid3-row")
        v_suppliers[random.randint(0, len(v_suppliers) - 1)].click()
        driver.find_element_by_id("Button1").click()
        time.sleep(2)
        driver.switch_to.parent_frame()
        # 制造商目录编号
        driver.find_element_by_id("txtSupplierCode").send_keys("MUBH" + v_tim)
        # 采购计量单位
        v_units = random.choice(
            ['个', '件', '条', '斤', '包', '桶', 'KG', '条'])
        driver.find_element_by_id("txtUnit").send_keys(v_units)
        # 备注页签
        driver.find_element_by_link_text("备注").click()
        time.sleep(1)
        write_file = open(root_path() + 'PubliData/character5K.txt', 'r')
        v_lines = write_file.read()
        driver.find_element_by_id("txtBZ").send_keys(v_lines[10:500])
        time.sleep(2)
        driver.find_element_by_id("btnSave").click()
        time.sleep(3)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_0501_01_add.jpg")
                print(i.text)
                unittest.expectedFailure("test_0501_01_add")

    # 物料主数据管理-物料主数据管理-更新物料功能
    def test_0501_02_Update(self):
        """物料主数据管理-物料主数据管理-更新物料功能"""
        driver = self.driver
        v_tim = time.strftime("%Y%m%d%H%M%S")
        v_wllists = driver.find_elements_by_class_name("x-grid3-row")
        ActionChains(driver).double_click(v_wllists[random.randint(0, len(v_wllists) - 1)]).perform()
        time.sleep(3)
        driver.switch_to_frame("winActivity_IFrame")     # 切换到更新物料页面
        # 条形码
        driver.find_element_by_id("txtBarCode").send_keys("TXM" + v_tim)
        driver.find_element_by_id("btnSave").click()
        time.sleep(3)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_0501_02_Update.jpg")
                print(i.text)
                unittest.expectedFailure("test_0501_02_Update")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(MaterialMaster("test_0501_01_add"))

    runner = unittest.TextTestRunner()
    runner.run(testsuit)