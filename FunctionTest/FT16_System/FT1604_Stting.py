# -*- coding: utf-8 -*-
from PubliCode.onlineClass import *


class Stting(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)

    """业务设置-费用设置-类型添加功能"""
    def test_1604_01_ApplyAdd(self):
        """业务设置-费用设置-类型添加功能"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "系统管理", "业务设置", "费用设置", "报销类型设置")
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000762")
        driver.find_element_by_id("btnAdd").click()
        time.sleep(2)
        v_tim = time.strftime("%m%d%H%M")
        driver.find_element_by_id("Type").send_keys("费用类型" + v_tim)
        driver.find_element_by_id("Digest").send_keys("全选菜单Auto" + v_tim)
        # 关联菜单
        driver.find_element_by_xpath("//*[@id='x-form-el-MenuLink']/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winTypeAdd_IFrame")
        v_check = driver.find_elements_by_class_name("x-grid3-row-checker")
        for i in v_check:
            i.click()
        time.sleep(1)
        driver.find_element_by_id("Button1").click()
        time.sleep(2)
        driver.switch_to.parent_frame()
        # 科目代码
        driver.find_element_by_xpath("//*[@id='x-form-el-AcctCode']/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winTypeAdd_IFrame")
        driver.find_element_by_id("txtBPartners").send_keys("100201")
        driver.find_element_by_id("btnBPartners").click()
        time.sleep(1)
        for i in driver.find_elements_by_class_name("x-grid3-cell-inner"):
            i.click()
            break
        driver.find_element_by_id("Button1").click()
        time.sleep(2)
        driver.switch_to.parent_frame()
        driver.find_element_by_id("BtnSaveForm").click()
        time.sleep(2)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功" in i.text:
                print(i.text)
            elif "费用类型已存在" in i.text:
                print(i.text)
            else:
                print(i.text)
                unittest.expectedFailure("test_1604_01_ApplyAdd")

    """费用设置-财务设置-报销金额添加功能"""
    def test_1604_02_FinanceAdd(self):
        """费用设置-财务设置-报销金额添加功能"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "系统管理", "业务设置", "费用设置", "财务设置")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000763")
        driver.find_element_by_id("btnSave").click()
        time.sleep(2)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功！" in i.text:
                print(i.text)
            else:
                print(i.text)
                unittest.expectedFailure("test_1604_02_FinanceAdd")

    """业务设置-销售合同条款-合同条款添加添加"""
    def test_1604_03_SalesContract(self):
        """业务设置-销售合同条款-合同条款添加添加"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "系统管理", "业务设置", "销售设置", "销售合同条款")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000728")
        v_save = driver.find_element_by_id("btnSave")
        v_tim = time.strftime("%Y%m%d%H%M")
        if v_save.is_displayed():
            driver.find_element_by_id("descrption").clear()
            driver.find_element_by_id("descrption").send_keys(v_tim + fun_data_character(100, 1000))
            time.sleep(2)
            v_save.click()
            time.sleep(3)
            print("业务设置-销售设置-销售合同条款添加数据OK")
        else:
            print("BUG 业务设置-销售设置-销售合同条款添加数据错误")
            unittest.expectedFailure("test_1604_03_SalesContract")

    """业务设置-销售设置-收款阶段设置报警天数添加"""
    def test_1604_04_SalesPhase(self):
        """业务设置-销售设置-收款阶段设置报警天数添加"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "系统管理", "业务设置", "销售设置", "收款阶段设置")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000726")
        v_add = driver.find_element_by_id("btnAdd")
        v_tim = time.strftime("%y%m%d%H%M")
        if v_add.is_displayed():
            v_add.click()
            time.sleep(2)
            driver.find_element_by_id("txtName").send_keys("付款名称Auto" + v_tim)
            driver.find_element_by_id("txtWarningDays").send_keys(random.randint(1, 100))
            driver.find_element_by_id("BtnSaveForm").click()
            time.sleep(3)
            print("业务设置-销售设置-收款阶段设置添加报警天数OK")
        else:
            print("BUG 业务设置-销售设置-收款阶段设置添加报警天数错误")
            unittest.expectedFailure("test_1604_04_SalesPhase")

    """采购设置-采购合同条款-数据添加功能"""
    def test_1604_05_Contract(self):
        """采购设置-采购合同条款-数据添加功能"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "系统管理", "业务设置", "采购设置", "采购合同条款")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000729")
        v_save = driver.find_element_by_id("btnSave")
        v_tim = time.strftime("%y%m%d%H%M")
        if v_save.is_displayed():
            driver.find_element_by_id("descrption").clear()
            time.sleep(1)
            driver.find_element_by_id("descrption").send_keys(v_tim + fun_data_character(300, 800))
            time.sleep(2)
            v_save.click()
            time.sleep(3)
            print("业务设置-采购设置-采购合同条款数据添OK")
        else:
            print("BUG 业务设置-采购设置-采购合同条款数据添加错误")
            unittest.expectedFailure("test_1604_05_Contract")

    """采购设置-付款阶段设置-付款阶段设置添加报警天数功能"""
    def test_1604_06_Phase(self):
        """采购设置-付款阶段设置-付款阶段设置添加报警天数功能"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "系统管理", "业务设置", "采购设置", "付款阶段设置")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000727")
        v_add = driver.find_element_by_id("btnAdd")
        v_tim = time.strftime("%y%m%d%H%M")
        if v_add.is_displayed():
            v_add.click()
            time.sleep(2)
            driver.find_element_by_id("txtName").send_keys("付款名称Auto" + v_tim)
            driver.find_element_by_id("txtWarningDays").send_keys(random.randint(1, 100))
            driver.find_element_by_id("BtnSaveForm").click()
            time.sleep(3)
            print("业务设置-采购设置-付款阶段设置添加报警天数正常")
        else:
            print("BUG 业务设置-采购设置-付款阶段设置添加报警天数正常错误")
            unittest.expectedFailure("test_1604_06_Phase")

    """业务设置-库存设置-库存收货添加功能"""
    def test_1604_07_TransceiverStart(self):
        """业务设置-库存设置-库存收货添加功能"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "系统管理", "业务设置", "库存设置", "库存收发货设置")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000730")
        driver.find_element_by_id("btnAdd").click()
        time.sleep(2)
        v_tim = time.strftime("%d%H%M")
        driver.find_element_by_id("Name").send_keys("库存收货Auto" + v_tim)
        # 科目代码
        driver.find_element_by_xpath("//*[@id='x-form-el-AcctCode']/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winTypeAdd_IFrame")
        driver.find_element_by_id("txtBPartners").send_keys("100101")
        time.sleep(1)
        for i in driver.find_elements_by_class_name("x-grid3-cell-inner"):
            i.click()
            break
        driver.find_element_by_id("Button1").click()
        time.sleep(2)
        driver.switch_to.parent_frame()
        # 类型
        driver.find_element_by_id("InOutType").click()
        for i in driver.find_elements_by_class_name("x-combo-list-item"):
            if i.text == "库存收货":
                i.click()
                time.sleep(1)
                break
        driver.find_element_by_id("BtnSaveForm").click()
        time.sleep(2)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功！" in i.text:
                print(i.text)
            else:
                unittest.expectedFailure("test_1604_07_TransceiverStart")

    """业务设置-库存设置-库存发货添加功能"""
    def test_1604_08_delivery(self):
        """业务设置-库存设置-库存发货添加功能"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "系统管理", "业务设置", "库存设置", "库存收发货设置")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000730")
        driver.find_element_by_id("btnAdd").click()
        time.sleep(2)
        v_tim = time.strftime("%d%H%M")
        driver.find_element_by_id("Name").send_keys("库存发货Auto" + v_tim)
        # 科目代码
        driver.find_element_by_xpath("//*[@id='x-form-el-AcctCode']/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winTypeAdd_IFrame")
        driver.find_element_by_id("txtBPartners").send_keys("100101")
        time.sleep(1)
        for i in driver.find_elements_by_class_name("x-grid3-cell-inner"):
            i.click()
            break
        driver.find_element_by_id("Button1").click()
        time.sleep(2)
        driver.switch_to.parent_frame()
        # 类型
        driver.find_element_by_id("InOutType").click()
        for i in driver.find_elements_by_class_name("x-combo-list-item"):
            if i.text == "库存发货":
                i.click()
                time.sleep(1)
                break
        driver.find_element_by_id("BtnSaveForm").click()
        time.sleep(2)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功！" in i.text:
                print(i.text)
            else:
                unittest.expectedFailure("test_1604_08_delivery")

    """业务设置-项目设置-项目类型添加功能"""
    def test_1604_10_TypeAdd(self):
        """业务设置-项目设置-项目类型添加功能"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "系统管理", "业务设置", "项目设置", "项目类型")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000758")
        v_add = driver.find_element_by_id("btnAdd")
        v_tim = time.strftime("%y%m%d%H%M")
        if v_add.is_displayed():
            v_add.click()
            time.sleep(2)
            driver.find_element_by_id("txtTitle_F").send_keys("项目类型Auto" + v_tim)
            driver.find_element_by_id("BtnSaveForm").click()
            time.sleep(3)
            print("项目设置-项目类型-页面显示正常")
        else:
            unittest.expectedFailure("test_1604_10_TypeAdd")

    """业务设置-项目设置-项目组加功能"""
    def test_1604_11_PrjGroup(self):
        """业务设置-项目设置-项目组加功能"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "系统管理", "业务设置", "项目设置", "项目组")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000759")
        v_tim = time.strftime("%m%d%H%M")
        driver.find_element_by_id("btnAdd").click()
        driver.find_element_by_id("txtTitle_F").send_keys("项目组名称Auto" + v_tim)
        time.sleep(1)
        driver.find_element_by_class_name("x-form-twin-triggers").find_element_by_id("ext-gen68").click()
        time.sleep(2)
        for i in driver.find_elements_by_class_name("x-grid3-row-checker"):
            i.click()
        time.sleep(1)
        driver.find_element_by_id("Button2").click()
        time.sleep(3)
        driver.find_element_by_id("BtnSaveForm").click()
        time.sleep(3)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "添加成功" in i.text:
                print(v_tip)
            else:
                unittest.expectedFailure("test_1604_11_PrjGroup")

    """移动端配置-微信企业号-自定义事件发布功能"""
    def test_1604_12_WeixinEdd(self):
        """移动端配置-微信企业号-自定义事件发布功能"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "移动端配置", "微信企业号", "自定义事件")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000595")
        driver.find_element_by_id("btnAdd").click()
        time.sleep(3)
        driver.switch_to.frame("winDetail_IFrame")
        v_tim = time.strftime("%y%m%d%H%M")
        # 事件名称
        driver.find_element_by_id("txtTitle").send_keys("时间名称" + v_tim)
        # 事件key
        driver.find_element_by_id("txtEventKey").send_keys(v_tim)
        # 回复内容
        driver.find_element_by_xpath("//*[@id='txtContent_Container']/div/span").click()
        time.sleep(3)
        v_lists = driver.find_elements_by_class_name("x-grid3-row")
        if len(v_lists) > 0:
            v_lists[0].click()
            driver.find_element_by_id("Button1").click()
            time.sleep(1)
            driver.find_element_by_id("btnSave").click()
            time.sleep(2)
            v_tip = driver.find_elements_by_class_name("ext-mb-text")
            for i in v_tip:
                if "成功" in i.text:
                    print(i.text)
                else:
                    unittest.expectedFailure("test_1604_12_WeixinEnSeting")
        else:
            print("回复内容数据为空")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(Stting("test_1604_12_WeixinEdd"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)