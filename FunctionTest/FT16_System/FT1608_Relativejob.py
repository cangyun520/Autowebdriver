# -*- coding: utf-8 -*-
from PubliCode.onlineClass import *


class Workjobs(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        # self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_part_text(self, "系统管理", "流程设置", "相对岗管理")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000231")

    '''审批警报-固定流程设计-相对岗管理添加'''
    def test_1608_01_add(self):
        """审批警报-固定流程设计-相对岗管理添加"""
        dr = self.driver
        dr.find_element_by_id("btnAdd").click()
        time.sleep(1)
        v_tim = time.strftime("%Y%m%d%H%M")
        v_job = "相对岗" + str(v_tim)
        dr.find_element_by_id("txtTitle_F").send_keys(v_job)
        dr.find_element_by_id("txtRemark_F").send_keys(fun_data_character(10, 100))
        dr.find_element_by_id("BtnSaveForm").click()
        dr.find_element_by_id("BtnSaveForm").click()
        time.sleep(2)
        v_tip = dr.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "相对岗名已存在" in i.text:
                print(i.text)
            else:
                dr.get_screenshot_as_file(root_path() + "TestPicture/hr/test_1608_01_add.jpg")
                print("Error：" + i.text)
                unittest.expectedFailure("test_1608_01_add")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    unittest.main()
