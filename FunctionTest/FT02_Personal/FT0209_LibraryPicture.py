# -*- coding: utf-8 -*-
from PubliCode.onlineClass import *
from PubliCode.randData import *


class LibraryPicture(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "个人事务", "知识文库", "图片浏览")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000811")

    # 知识文库-图片浏览-单据添加功能
    def test_0209_01_add(self):
        """知识文库-图片浏览-单据添加功能"""
        driver = self.driver
        driver.find_element_by_id("btnAddCategory").click()
        v_tim = time.strftime("%Y%m")
        time.sleep(2)
        driver.find_element_by_id("txtCategoryName").send_keys("目录" + v_tim)
        time.sleep(1)
        driver.find_element_by_id("Button1").click()
        time.sleep(2)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功" in i.text:
                print(i.text)
            elif "目录名称已存在" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/oa/test_0209_01_add.jpg")
                print(i.text)
                unittest.expectedFailure("test_0209_01_add")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(LibraryPicture("test_0209_01_add"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)