
from PubliCode.webClass import *

class ST05_Erp(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)

# #-----------
    def test_0501_Merchants(self):
        """客商管理-客户主数据-"常规"检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "客商管理", "客户主数据")
        driver.switch_to_frame("frame_tab_PM000067")
        v_general = driver.find_element_by_link_text("常规")
        try:
            v_general.is_displayed()
            print("客户主数据-页面-显示正常")
        except ImportError:
            print("BUG 客户主数据-常规页签-不显示")
            unittest.expectedFailure("test_0501_Merchants")

    def test_0502_Suppliers(self):
        """客商管理-供应商主数据-"常规"检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "客商管理", "供应商主数据")
        driver.switch_to_frame("frame_tab_PM000417")
        try:
            driver.find_element_by_link_text("常规").is_displayed()
            print("供应商主数据-页面-显示正常")
        except ImportError:
            print("BUG 供应商主数据-常规页签-不显示")

    def test_0503_PotentialCustomer(self):
        """客商管理-潜在客户主数据-"常规"检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "客商管理", "潜在客户主数据")
        driver.switch_to_frame("frame_tab_PM000734")
        try:
            driver.find_element_by_link_text("常规").is_displayed()
            print("潜在客户主数据-页面-显示正常")
        except ImportError:
            print("BUG 潜在客户主数据-常规页签-不显示")

    def test_0504_Event(self):
        """客商管理-业务活动-"常规"检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "客商管理", "业务活动")
        driver.switch_to_frame("frame_tab_PM000740")
        try:
            driver.find_element_by_link_text("常规").is_displayed()
            print("业务活动-页面-显示正常")
        except ImportError:
            print("BUG 业务活动-常规页签-不显示，业务活动")

    def test_0505_MaterialDate(self):
        """物料管理-物料主数据管理-"常规"检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "物料管理", "物料主数据管理")
        driver.switch_to_frame("frame_tab_PM000911")
        try:
            driver.find_element_by_id("ext-gen47").is_displayed()
            print("物料主数据管理-页面-显示正常")
        except ImportError:
            print("BUG 物料主数据管理-常规页签-不显示")

    # -----------项目管理
    def test_0506_Items_ProjectDate(self):
        """项目管理-项目主数据-"常规"检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "项目管理", "项目主数据")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(driver, 500)
        driver.switch_to_frame("frame_tab_PM000753")
        try:
            driver.find_element_by_id("btnProjectAdd").is_displayed()
            print("项目主数据-页面-显示正常")
        except ImportError:
            print("BUG 项目主数据-同步B1项目数据-不显示")

    def test_0507_Items_ProjectApproval(self):
        """项目管理-项目立项-"常规"检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "项目管理", "项目立项")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(driver, 500)
        driver.switch_to_frame("frame_tab_PM000755")
        try:
            driver.find_element_by_link_text("项目信息").is_displayed()
            print("项目立项-页面-显示正常")
        except ImportError:
            print("BUG 项目立项-项目信息页签-不显示")

    def test_0508_Items_ProjectChange(self):
        """项目管理-项目信息变更-"常规"检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "项目管理", "项目信息变更")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(driver, 500)
        driver.switch_to_frame("frame_tab_PM000756")
        try:
            driver.find_element_by_link_text("项目信息").is_displayed()
            print("项目信息变更-页面-显示正常")
        except ImportError:
            print("BUG 项目信息变更-项目信息页签-不显示")

    # -----------销售管理
    def test_0509_Sales_SalesQuotation(self):
        """销售管理-销售报价单-"常规"检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "销售管理", "销售报价单")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(driver, 500)
        driver.switch_to_frame("frame_tab_PM000192")
        try:
            driver.find_element_by_link_text("内容").is_displayed()
            print("销售报价单-页面-显示正常")
        except ImportError:
            print("BUG 销售报价单-内容页签-不显示")

    def test_0510_Sales_SalesOrder(self):
        """销售管理-销售报价单-"常规"检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "销售管理", "销售订单")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(driver, 500)
        driver.switch_to_frame("frame_tab_PM000190")
        try:
            driver.find_element_by_link_text("内容").is_displayed()
        except ImportError:
            print("BUG 销售订单-内容页签-不显示")
        else:
            print("销售订单-页面-显示正常")

    def test_0511_Sales_AdvancesReceived(self):
        """销售管理-预收款申请-"常规"检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "销售管理", "预收款申请")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(driver, 500)
        driver.switch_to_frame("frame_tab_PM000198")
        try:
            driver.find_element_by_link_text("内容").is_displayed()
        except ImportError:
            print("BUG 预收款申请-内容页签-不显示")
        else:
            print("预收款申请-页面-显示正常")

    def test_0512_Sales_ARI(self):
        """销售管理-应收发票-"常规"检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "销售管理", "应收发票")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(driver, 500)
        driver.switch_to_frame("frame_tab_PM000200")
        try:
            driver.find_element_by_link_text("内容").is_displayed()
        except ImportError:
            print("BUG 应收发票-内容页签-不显示")
        else:
            print("应收发票-页面-显示正常")

    def test_0513_Sales_InvoicePay(self):
        """销售管理-应收发票+付款-"常规"检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "销售管理", "应收发票+付款")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(driver, 500)
        driver.switch_to_frame("frame_tab_PM000202")
        try:
            driver.find_element_by_link_text("内容").is_displayed()
        except ImportError:
            print("BUG 应收发票+付款-内容页签-不显示")
        else:
            print("应收发票+付款-页面-显示正常")

    def test_0514_Sales_CreditMemo(self):
        """销售管理-应收贷项凭证-"常规"检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "销售管理", "应收贷项凭证")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(driver, 500)
        driver.switch_to_frame("frame_tab_PM000196")
        try:
            driver.find_element_by_link_text("内容").is_displayed()
        except ImportError:
            print("BUG 应收贷项凭证-内容页签-不显示")
        else:
            print("应收贷项凭证-页面-显示正常")

    def test_0515_AccountsReserved(self):
        """销售管理-应收预留发票-"常规"检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "销售管理", "应收预留发票")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(driver, 500)
        driver.switch_to_frame("frame_tab_PM000223")
        try:
            driver.find_element_by_link_text("内容").is_displayed()
            print("应收预留发票-页面-显示正常")
        except ImportError:
            print("BUG 应收预留发票-内容页签-不显示")

    # -----------采购管理
    def test_0516_Purch_PurchaseRequisition(self):
        """采购管理-采购申请单-"常规"检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "采购管理", "采购申请单")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(driver, 500)
        driver.switch_to_frame("frame_tab_PM000294")
        try:
            driver.find_element_by_link_text("内容").is_displayed()
            print("应收预留发票-页面-显示正常")
        except ImportError:
            print("BUG 应收预留发票-内容页签-不显示")

    def test_0517_Purch_PurchaseQuote(self):
        """采购管理-采购报价单-"常规"检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "采购管理", "采购报价单")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(driver, 500)
        driver.switch_to_frame("frame_tab_PM000193")
        try:
            driver.find_element_by_link_text("内容").is_displayed()
            print("采购报价单-页面-显示正常")
        except ImportError:
            print("BUG 采购报价单-内容页签-不显示")

    def test_0518_Purch_PurchaseOrder(self):
        """采购管理-采购订单-"常规"检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "采购管理", "采购订单")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(driver, 500)
        driver.switch_to_frame("frame_tab_PM000191")
        try:
            driver.find_element_by_link_text("内容").is_displayed()
            print("采购订单-页面-显示正常")
        except ImportError:
            print("BUG 采购订单-内容页签-不显示")

    def test_0519_Purch_PurchaseArrival(self):
        """采购管理-采购到货跟踪-"常规"检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "采购管理", "采购到货跟踪")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(driver, 500)
        driver.switch_to_frame("frame_tab_PM000732")
        try:
            driver.find_element_by_id("btnSelect").is_displayed()
            print("采购到货跟踪-页面-显示正常")
        except ImportError:
            print("BUG 采购到货跟踪-【查询】-不显示")

    def test_0520_Purch_PurchaseAdvance(self):
        """采购管理-采购预付款申请-"常规"检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "采购管理", "采购预付款申请")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(driver, 500)
        driver.switch_to_frame("frame_tab_PM000218")
        try:
            driver.find_element_by_link_text("内容").is_displayed()
            print("采购预付款申请-页面-显示正常")
        except ImportError:
            print("BUG 采购预付款申请-内容页签-不显示")

    def test_0521_Purch_PayableDetails(self):
        """采购管理-应付暂估明细-"常规"检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "采购管理", "应付暂估明细")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(driver, 500)
        driver.switch_to_frame("frame_tab_PM000733")
        try:
            driver.find_element_by_id("btnSelect").is_displayed()
            print("应付暂估明细-页面-显示正常")
        except ImportError:
            print("BUG 应付暂估明细-【查询】-不显示")

    def test_0522_Purch_PurchaseAdvance(self):
        """采购管理-应付发票-"常规"检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "采购管理", "应付发票")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(driver, 500)
        driver.switch_to_frame("frame_tab_PM000215")
        try:
            driver.find_element_by_link_text("内容").is_displayed()
            print("应付发票-页面-显示正常")
        except ImportError:
            print("BUG 应付发票-内容页签-不显示")

    def test_0523_Purch_CopeCredit(self):
        """采购管理-应付贷项凭证-"常规"检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "采购管理", "应付贷项凭证")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(driver, 500)
        driver.switch_to_frame("frame_tab_PM000219")
        try:
            driver.find_element_by_link_text("内容").is_displayed()
            print("应付贷项凭证-页面-显示正常")
        except ImportError:
            print("BUG 应付贷项凭证-内容页签-不显示")

    def test_0524_Purch_CopeCredit(self):
        """采购管理-应付预留发票-"常规"检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "采购管理", "应付预留发票")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(driver, 500)
        driver.switch_to_frame("frame_tab_PM000221")
        try:
            driver.find_element_by_link_text("内容").is_displayed()
            print("应付预留发票-页面-显示正常")
        except ImportError:
            print("BUG 应付预留发票-内容页签-不显示")
    # -----------质检管理
    def test_0525_QC_Submission(self):
        """质检管理-送检单-"常规"检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "质检管理", "送检单")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(driver, 500)
        driver.switch_to_frame("frame_tab_PM000831")
        v_content = driver.find_element_by_id("BtnAdd")
        try:
            v_content.is_displayed()
            print("送检单-页面-显示正常")
        except ImportError:
            print("BUG 送检单-内容页签-不显示")

    def test_0526_QC_Submission(self):
        """质检管理-待检管理-"常规"检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "质检管理", "待检管理")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(driver, 500)
        driver.switch_to_frame("frame_tab_PM000833")
        v_add = driver.find_element_by_id("BtnAdd")
        try:
            v_add.is_displayed()
            print("待检管理-页面-显示正常")
        except ImportError:
            print("BUG 待检管理-内容页签-不显示")

    def test_0527_QC_Quality(self):
        """质检管理-质检单-"常规"检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "质检管理", "质检单")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(driver, 500)
        driver.switch_to_frame("frame_tab_PM000834")
        v_add = driver.find_element_by_id("btnQuery")
        try:
            v_add.is_displayed()
            print("质检单-页面-显示正常")
        except ImportError:
            print("BUG 质检单-内容页签-不显示")

    # # -----------订货管理
    def test_0530_order_Order(self):
        """订货管理-订货-"常规"检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "订货管理", "订货")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(driver, 500)
        driver.switch_to_frame("frame_tab_PM001043")
        v_add = driver.find_element_by_id("BtnAdd")
        try:
            v_add.is_displayed()
            print("订货-页面-显示正常")
        except ImportError:
            print("BUG 订货-【添加】-不显示")

    def test_0531_order_Plan(self):
        """订货管理-订货需求计划-"常规"检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "订货管理", "订货需求计划")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(driver, 500)
        driver.switch_to_frame("frame_tab_PM001045")
        v_assignSuper = driver.find_element_by_id("btnAssignSuper")
        try:
            v_assignSuper.is_displayed()
            print("订货需求计划-页面-显示正常")
        except ImportError:
            print("BUG 订货需求计划-【添加】-不显示")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(ST05_Erp("test_0501_ERP_Merchants"))
    testsuit.addTest(ST05_Erp("test_0502_ERP_Suppliers"))
    testsuit.addTest(ST05_Erp("test_0503_ERP_PotentialCustomer"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)