from PubliCode.onlineClass import *
from PubliCode.randData import *

'''
    *   Arvin
    *   2017-05-13
'''


class DataRelated(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, u"系统管理", u"常规设置", u"行格式自定义")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000255")

    '''系统管理-常规设置-添加分配规则'''
    def test_1615_01_AddFPGZ(self):
        """系统管理-警报设置-数据相关查询"""
        driver = self.driver
        # 获取文件名称



        # driver.find_element_by_id("comboBoxXmlName").clear()

        # v_input = ['销售报价单(物料)', '销售报价单(服务)', '销售订单(物料)', '销售订单(服务)', "销售交货(物料)", "销售交货(服务)",
        #            "销售退货(物料)", "销售退货(服务)", '预收款申请(物料)', '预收款申请(服务)', '应收发票(物料)', '应收发票(服务)',
        #            '应收贷项凭证(物料)', '应收贷项凭证(服务)', '应收发票+付款(物料)', '应收预留发票(物料)', '应收预留发票(服务)',
        #            '采购申请(物料)', '采购申请(服务)', '采购报价单(物料)', '采购报价单(服务)', '采购订单(物料)', '采购订单(服务)',
        #            '采购收货(物料)', '采购收货(服务)', '采购退货(物料)', '采购退货(服务)', '应付发票(物料)', '应付发票(服务)',
        #            '预付款申请(物料)', '预付款申请(服务)', '应付贷项凭证(物料)', '应付贷项凭证(服务)', '应付预留发票(物料)',
        #            '应付预留发票(服务)']
        # print(len(v_input))
        n = 0
        while n < 35:
            driver.find_element_by_xpath(
                "//*[@id='ext-comp-1002'']/table/tbody/tr/td/table/tbody/tr/td/div/div/div/img").click()
            time.sleep(1)
            # 菜单列表
            v_list = driver.find_elements_by_class_name("x-combo-list-item")
            v_list[n].click()
            time.sleep(3)
            driver.find_element_by_id("comboHidColumn").click()
            time.sleep(1)
            v_list = driver.find_elements_by_class_name("x-mcombo-text")
            for i in v_list:
                # print(i.text)
                if "分配规则" in i.text:
                    i.click()
                    time.sleep(1)
                    # 显示隐藏列
                    driver.find_element_by_id("btnHidColumn").click()
                    time.sleep(1)
                    driver.find_element_by_id("btnSave").click()
                    time.sleep(3)
                    ClasForm.form_button_yes(self, "确定")
                    break
                else:
                    pass

            n += 1

    '''系统管理-常规设置-隐藏分配规则'''
    def test_1615_02_HideFPGZ(self):
        """系统管理-警报设置-数据相关查询"""
        driver = self.driver
        driver.find_element_by_id("comboBoxXmlName").clear()
        n = 0
        v_input = ['销售报价单(物料)', '销售报价单(服务)', '销售订单(物料)', '销售订单(服务)', "销售交货(物料)", "销售交货(服务)",
                   "销售退货(物料)", "销售退货(服务)", '预收款申请(物料)', '预收款申请(服务)', '应收发票(物料)', '应收发票(服务)',
                   '应收贷项凭证(物料)', '应收贷项凭证(服务)', '应收发票+付款(物料)', '应收预留发票(物料)', '应收预留发票(服务)',
                   '采购申请(物料)', '采购申请(服务)', '采购报价单(物料)', '采购报价单(服务)', '采购订单(物料)', '采购订单(服务)',
                   '采购收货(物料)', '采购收货(服务)', '采购退货(物料)', '采购退货(服务)', '应付发票(物料)', '应付发票(服务)',
                   '预付款申请(物料)', '预付款申请(服务)', '应付贷项凭证(物料)', '应付贷项凭证(服务)', '应付预留发票(物料)',
                   '应付预留发票(服务)']

        while n < len(v_input):
            driver.find_element_by_id("comboBoxXmlName").click()
            driver.find_element_by_id("comboBoxXmlName").clear()
            time.sleep(1)
            driver.find_element_by_id("comboBoxXmlName").send_keys(v_input[n])
            time.sleep(1)
            v_compare = driver.find_element_by_class_name("x-combo-list-inner")
            if v_compare.text == v_input[n]:
                v_compare.click()
            time.sleep(4)
            driver.find_element_by_id("comboHidColumn").click()
            time.sleep(1)
            v_list = driver.find_elements_by_class_name("x-mcombo-text")
            for i in v_list:
                # print(i.text)
                if "分配规则" == i.text:
                    i.click()
                    time.sleep(1)
                    # driver.find_element_by_id("comboHidColumn").click()
                    # time.sleep(1)
                    # 显示隐藏列
                    driver.find_element_by_id("btnHidColumn").click()
                    time.sleep(1)
                    driver.find_element_by_id("btnSave").click()
                    time.sleep(3)
                    ClasForm.form_button_yes(self, "确定")
                    break
                else:
                    pass
                #     # 关闭自定义字段
                #     driver.find_element_by_id("comboHidColumn").click()
                #     driver.find_element_by_id("comboBoxXmlName").clear()
                #     time.sleep(1)
            n += 1

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
