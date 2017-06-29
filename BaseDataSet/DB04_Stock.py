# -*- coding: utf-8 -*-
from PubliCode.onlineClass import *


class DB04_Stock(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)

    # 业务设置-库存设置-库存收货
    def test_DB04_01_TransceiverStart(self):
        """业务设置-库存设置-库存收货添加功能检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "订货管理", "系统管理", "业务设置", "库存设置", "库存收发货设置")

        driver.switch_to.frame("frame_tab_PM000730")
        driver.find_element_by_id("btnAdd").click()
        time.sleep(2)
        v_tim = time.strftime("%d%H%M")
        driver.find_element_by_id("Name").send_keys("库存收货Au" + v_tim)
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
                print(i.text)
                unittest.expectedFailure("test_DB04_01_TransceiverStart")

        # 启用状态
        v_tds = driver.find_element_by_class_name("x-grid3-hd-row").find_elements_by_tag_name("td")
        for i in v_tds:
            if i.text == "是否启用":
                i.click
                time.sleep(1)
                driver.find_elements_by_class_name("x-grid3-row")[0].click()
                driver.find_element_by_id("btnStart").click()
                time.sleep(2)
                v_tip = driver.find_elements_by_class_name("ext-mb-text")
                for i in v_tip:
                    if "启用成功" in i.text:
                        ClasForm.form_button_yes(self, "确定")
                    else:
                        print(i.text)
                        unittest.expectedFailure("test_DB04_02_TransceiverStart")
                break
            else:
                pass

    # 业务设置-库存设置-库存发货
    def test_DB04_02_TransceiverStart(self):
        """业务设置-库存设置-库存发货添加功能检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "系统管理", "业务设置", "库存设置", "库存收发货设置")

        driver.switch_to.frame("frame_tab_PM000730")
        driver.find_element_by_id("btnAdd").click()
        time.sleep(2)
        v_tim = time.strftime("%d%H%M")
        driver.find_element_by_id("Name").send_keys("库存发货Au" + v_tim)
        # 科目代码
        driver.find_element_by_xpath("//*[@id='x-form-el-AcctCode']/div/span").click()
        time.sleep(3)
        driver.switch_to_frame("winTypeAdd_IFrame")
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
            if "成功" in i.text:
                ClasForm.form_button_yes(self, "确定")
            else:
                print(i.text)
                unittest.expectedFailure("test_DB04_02_TransceiverStart")

        # 启用状态
        v_tds = driver.find_element_by_class_name("x-grid3-hd-row").find_elements_by_tag_name("td")
        for i in v_tds:
            if i.text == "是否启用":
                i.click
                time.sleep(1)
                driver.find_elements_by_class_name("x-grid3-row")[0].click()
                driver.find_element_by_id("btnStart").click()
                time.sleep(2)
                v_tip = driver.find_elements_by_class_name("ext-mb-text")
                for i in v_tip:
                    if "启用成功" in i.text:
                        ClasForm.form_button_yes(self, "确定")
                    else:
                        print(i.text)
                        unittest.expectedFailure("test_DB04_02_TransceiverStart")
                break
            else:
                pass

    # 系统管理-业务设置-库存设置-借料还料设置
    def test_DB04_04_CirculateAdd(self):
        """业务设置-库存设置-借料还料设置添加功能检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "系统管理", "业务设置", "库存设置", "借料还料设置")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000877")
        v_add = driver.find_element_by_id("BtnAdd")
        v_tim = time.strftime("%y%m%d%H%M")
        if v_add.is_displayed():
            v_add.click()
            time.sleep(2)
            driver.find_element_by_id("txtTypeName").send_keys("借料类型Auto" + v_tim)
            driver.find_element_by_id("txtRemark").send_keys("备注" + v_tim)
            driver.find_element_by_id("BtnSaveForm").click()
            time.sleep(3)
            print("库存设置-借料还料设置-添加功能OK")
        else:
            print("BUG 业务设置-库存设置-借料还料设置-添加功能错误")
            unittest.expectedFailure("test_DB04_04_CirculateAdd")

    # 业务设置-库存设置-借料还料默认仓库
    def test_DB04_05_Warehouse(self):
        """业务设置-库存设置-借料还料默认仓库"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "系统管理", "业务设置", "库存设置", "借料还料设置")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000877")
        driver.find_element_by_xpath("//*[@id='Toolbar1']/table/tbody/tr/td/table/tbody/tr/td[2]/div/span").click()
        time.sleep(3)
        driver.switch_to_frame("winAdd_IFrame")
        driver.find_element_by_id("txtSearchText").send_keys("03")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(1)
        driver.find_elements_by_class_name("x-grid3-row")[0].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(2)
        driver.switch_to.parent_frame()
        driver.find_element_by_id("btnSet").click()
        time.sleep(2)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "设置成功" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/test_DB04_05_Warehouse.jpg")
                # print(i.text)
                unittest.expectedFailure("test_DB04_05_Warehouse")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(DB04_Stock("test_DB04_01_TransceiverStart"))
    testsuit.addTest(DB04_Stock("test_DB04_02_TransceiverStart"))
    testsuit.addTest(DB04_Stock("test_DB04_04_CirculateAdd"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)