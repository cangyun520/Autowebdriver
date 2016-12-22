
from PubliCode.onlineClass import *

class ST14_ErpInventory(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)

    # -----------库存管理
    def test_1401_SaleDelivery(self):
        """库存管理-销售交货-"常规"检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, uu"库存管理", u"销售交货")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000194")
        SaleDelivery_Content = driver.find_element_by_link_text("内容")
        try:
            SaleDelivery_Content.is_displayed()
            print("销售交货-页面-显示正常")
        except ImportError:
            print("BUG 销售交货-内容页签-不显示")

    def test_1402_SaleReturn(self):
        """库存管理-销售退货-"常规"检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, uu"库存管理", u"销售退货")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000195")
        SaleReturn_Content = driver.find_element_by_link_text("内容")
        try:
            SaleReturn_Content.is_displayed()
            print("销售退货-页面-显示正常")
        except ImportError:
            print("BUG 销售退货-内容页签-不显示")

    def test_1403_PurchaseReceiving(self):
        """库存管理-采购收货-"常规"检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, uu"库存管理", u"采购收货")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000197")
        PurchaseReceiving_Content = driver.find_element_by_link_text("内容")
        try:
            PurchaseReceiving_Content.is_displayed()
            print("采购收货-页面-显示正常")
        except ImportError:
            print("BUG 采购收货-内容页签-不显示")

    def test_1404_PurchaseReturn(self):
        """库存管理-采购退货-"常规"检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, uu"库存管理", u"采购退货")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000201")
        PurchaseReturn_Content = driver.find_element_by_link_text("内容")
        try:
            PurchaseReturn_Content.is_displayed()
            print("采购退货-页面-显示正常")
        except ImportError:
            print("BUG 采购退货-内容页签-不显示")

    # -----------库存管理------库存转储
    def test_1405_StockTransfer_Apply(self):
        """库存管理-库存转储申请-"常规"检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, uu"库存管理", u"转储管理", u"库存转储申请")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000736")
        Apply_Content = driver.find_element_by_link_text("内容")
        try:
            Apply_Content.is_displayed()
            print("库存转储申请-页面-显示正常")
        except ImportError:
            print("BUG 库存转储申请-内容页签-不显示")
            unittest.expectedFailure("test_1405_StockTransfer_Apply")

    def test_1406_StockTransfer(self):
        """库存管理-库存转储申请-"常规"检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, uu"库存管理", u"转储管理", u"库存转储")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000214")
        Apply_Content = driver.find_element_by_link_text("内容")
        try:
            Apply_Content.is_displayed()
            print("库存转储-页面-显示正常")
        except ImportError:
            print("BUG 库存转储-内容页签-不显示")
            unittest.expectedFailure("test_1406_StockTransfer")

    def test_1415_Apply(self):
        """库存管理-借料申请单-"常规"检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, uu"库存管理", u"借料还料", u"借料申请单")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000871")
        Apply_Add = driver.find_element_by_id("BtnAdd")
        try:
            Apply_Add.is_displayed()
        except ImportError:
            print("BUG 借料申请单-【添加】-不显示")
        else:
            print("借料申请单-页面-显示正常")

    def test_1416_LoanSupplies(self):
        """库存管理-借料单-"常规"检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, uu"库存管理", u"借料还料", u"借料单")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000883")
        LoanSupplies_Add = driver.find_element_by_id("btnAdd")
        try:
            LoanSupplies_Add.is_displayed()
        except ImportError:
            print("BUG 借料单-【添加】-不显示，借料单")
        else:
            print("借料单-页面-显示正常")

    def test_1417_ReturnSupplies(self):
        """库存管理-还料单-"常规"检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, uu"库存管理", u"借料还料", u"还料单")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000885")
        ReturnSupplies_Add = driver.find_element_by_id("btnAdd")
        try:
            ReturnSupplies_Add.is_displayed()
        except ImportError:
            print("BUG 还料单-【添加】-不显示，还料单")
        else:
            print("还料单-页面-显示正常")
    # # -----------库存管理------其他出入库

    def test_1418_WarehouseOut(self):
        """库存管理-其他出库-"常规"检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, uu"库存管理", u"其他出入库", u"其他出库")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000209")
        out_content = driver.find_element_by_link_text("内容")
        try:
            out_content.is_displayed()
        except ImportError:
            print("BUG 其他出库-【添加】-不显示")
        else:
            print("其他出库-页面-显示正常")

    def test_1418_WarehouseOut(self):
        """库存管理-其他入库-"常规"检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, uu"库存管理", u"其他出入库", u"其他入库")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000207")
        out_content = driver.find_element_by_link_text("内容")
        try:
            out_content.is_displayed()
        except ImportError:
            print("BUG 其他入库-【添加】-不显示，其他入库")
        else:
            print("其他入库-页面-显示正常")

    # # -----------库存管理------库存盘点------库存冻结

    def test_1419_Freeze(self):
        """库存管理-库存冻结-"常规"检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, uu"库存管理", u"库存盘点", u"库存冻结")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM001037")
        out_content = driver.find_element_by_id("btnExportRegTable")
        try:
            out_content.is_displayed()
        except ImportError:
            print("BUG 库存冻结-【添加】-不显示")
        else:
            print("库存冻结-页面-显示正常")

    def test_1420_Inventory(self):
        """库存管理-盘点登记-"常规"检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, uu"库存管理", u"库存盘点", u"盘点登记")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM001039")
        Add = driver.find_element_by_id("btnAdd")
        try:
            Add.is_displayed()
        except ImportError:
            print("BUG 盘点登记-【添加】-不显示")
        else:
            print("盘点登记-页面-显示正常")

    def test_1421_Posting(self):
        """库存管理-待过账-"常规"检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, uu"库存管理", u"库存盘点", u"待过账")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM001040")
        Posting_Save = driver.find_element_by_id("btnSave")
        try:
            Posting_Save.is_displayed()
            print("待过账-页面-显示正常")
        except ImportError:
            print("BUG 待过账-【添加】-不显示")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(ST14_ErpInventory("test_1421_Posting"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)