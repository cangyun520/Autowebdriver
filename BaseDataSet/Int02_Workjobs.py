# -*- coding: utf-8 -*-
from PubliCode.onlineClass import *


class Workjobs(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_part_text(self, "系统管理", "审批流程", "相对岗管理")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000231")

    '''审批警报-固定流程设计-相对岗管理'''
    def test_Int02_01(self):
        """审批警报-固定流程设计-相对岗管理添加"""
        driver = self.driver
        v_list = driver.find_elements_by_class_name("x-grid3-row")
        if len(v_list) < 3:
            driver.find_element_by_id("btnAdd").click()
            time.sleep(2)
            driver.find_element_by_id("txtTitle_F").send_keys("Auto发起")
            driver.find_element_by_id("BtnSaveForm").click()
            time.sleep(1)
            driver.find_element_by_id("txtTitle_F").clear()
            driver.find_element_by_id("txtTitle_F").send_keys("Auto审批")
            driver.find_element_by_id("BtnSaveForm").click()
            time.sleep(1)
            driver.find_element_by_id("txtTitle_F").clear()
            driver.find_element_by_id("txtTitle_F").send_keys("Auto终审")
            driver.find_element_by_id("BtnSaveForm").click()
            time.sleep(1)
            # 关闭
            driver.find_element_by_id("Button1").click()
        else:
            print("已经有3个相对岗了")

    # 审批警报-相对岗管理-发起岗位用户添加
    def test_Int02_02(self):
        """审批警报-相对岗管理-发起岗位用户添加"""
        driver = self.driver
        driver.find_element_by_id("txtSelectName").send_keys("Auto发起")
        driver.find_element_by_id("btnSelect").click()
        time.sleep(2)
        driver.find_elements_by_class_name("x-grid3-row")[0].click()
        driver.find_element_by_id("btnAddUser").click()
        time.sleep(3)
        driver.switch_to.frame("winSelectUser_IFrame")      # 切换到用户多选窗体
        driver.find_element_by_id("txtuserName").send_keys("fq")
        driver.find_element_by_id("btnQuery").click()
        time.sleep(2)
        driver.find_elements_by_class_name("x-grid3-row")[0].click()
        driver.find_elements_by_class_name("x-grid3-row")[1].click()
        driver.find_elements_by_class_name("x-grid3-row")[2].click()
        driver.find_element_by_id("btnConfirm").click()
        time.sleep(1)
        driver.switch_to.parent_frame()
        v_tip = driver.find_elements_by_tag_name("bootbox-body")
        for i in v_tip:
            if "操作成功" in i.text:
                print(i.text)
            else:
                print(i.text)
                unittest.expectedFailure("test_Int02_02")

    '''审批警报-相对岗管理-审批岗位用户添加'''
    def test_Int02_03(self):
        """审批警报-相对岗管理-审批岗位用户添加"""
        driver = self.driver
        driver.find_element_by_id("txtSelectName").send_keys("Auto审批")
        driver.find_element_by_id("btnSelect").click()
        time.sleep(2)
        driver.find_elements_by_class_name("x-grid3-row")[0].click()
        driver.find_element_by_id("btnAddUser").click()
        time.sleep(3)
        driver.switch_to.frame("winSelectUser_IFrame")      # 切换到用户多选窗体
        driver.find_element_by_id("txtuserName").send_keys("sp")
        driver.find_element_by_id("btnQuery").click()
        time.sleep(2)
        driver.find_elements_by_class_name("x-grid3-row")[0].click()
        driver.find_elements_by_class_name("x-grid3-row")[1].click()
        driver.find_elements_by_class_name("x-grid3-row")[2].click()
        driver.find_element_by_id("btnConfirm").click()
        time.sleep(1)
        driver.switch_to.parent_frame()
        v_tip = driver.find_elements_by_tag_name("bootbox-body")
        for i in v_tip:
            if "操作成功" in i.text:
                print(i.text)
            else:
                unittest.expectedFailure("test_Int02_03")
                print(i.text)

    '''审批警报-相对岗管理-审批岗位用户添加'''
    def test_Int02_04(self):
        """审批警报-相对岗管理-审批岗位用户添加"""
        driver = self.driver
        driver.find_element_by_id("txtSelectName").send_keys("Auto终审")
        driver.find_element_by_id("btnSelect").click()
        time.sleep(2)
        driver.find_elements_by_class_name("x-grid3-row")[0].click()
        driver.find_element_by_id("btnAddUser").click()
        time.sleep(3)
        driver.switch_to.frame("winSelectUser_IFrame")      # 切换到用户多选窗体
        count = 0
        while count < 6:
            driver.find_elements_by_class_name("x-grid3-row")[count].click()
            count += 1
        driver.find_element_by_id("btnConfirm").click()
        time.sleep(3)
        driver.switch_to.parent_frame()
        v_tip = driver.find_elements_by_tag_name("ext-mb-text")
        for i in v_tip:
            if "操作成功" in i.text:
                print(i.text)
            elif "一个人" in i.text:
                print(i.text)
            else:
                unittest.expectedFailure("test_Int02_04")
                print(i.text)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(Workjobs("test_Int02_01"))
    testsuit.addTest(Workjobs("test_Int02_05"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)