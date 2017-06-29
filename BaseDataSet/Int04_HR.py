# -*- coding: utf-8 -*-
from PubliCode.onlineClass import *


class Int04_HR(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_part_text(self, "人事管理", "人员管理", "档案管理")
        driver.switch_to.frame("frame_tab_PM000888")

    '''人事管理-人员管理-档案管理'''
    def test_Int04_01_Import(self):
        driver = self.driver
        driver.find_element_by_id("Button1").click()
        time.sleep(2)
        driver.switch_to.frame("winInit_IFrame")

        driver.find_element_by_id("UploadFile-file").send_keys(root_path() + "PubliData/excel/HR档案管理.xlsx")
        driver.find_element_by_id("ckbCover").click()
        driver.find_element_by_id("BtnSaveForm").click()
        time.sleep(4)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "导入成功" in i.text:
                print(i.text)
            elif "档案中已存在" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/test_Int04_01_Import.jpg")
                unittest.expectedFailure("test_Int04_01_Import")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    unittest.main()
