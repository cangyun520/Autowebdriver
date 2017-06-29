# -*- coding: utf-8 -*-
from PubliCode.onlineClass import *
from PubliCode.randData import *
'''
    *   Arvin
    *   2017-01-13
'''


class Bookes(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        # self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "行政办公", "图书管理")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000797")

    '''行政办公-图书管理-单据添加'''
    def test_0403_01_add(self):
        """行政办公-图书管理-单据添加功能"""
        driver = self.driver
        driver.find_element_by_id("btnAdd").click()
        v_tim = time.strftime("%y%m%d%H%M")
        time.sleep(2)
        driver.find_element_by_id("txtAddBookName").send_keys("图书" + v_tim)
        time.sleep(1)
        # 图书分类
        driver.find_element_by_id("txtAddType").send_keys("IT编程类")
        time.sleep(1)
        # ISBN号
        driver.find_element_by_id("txtAddIsbn").send_keys("978-7-" + str(random.randint(10, 500)))
        time.sleep(1)
        # 出版社
        driver.find_element_by_id("txtAddPublisher").send_keys("出版社" + v_tim)
        time.sleep(1)
        # 出版日期
        ClasForm.form_today(self, "datefiPublishDate")
        time.sleep(1)
        # 存放地点
        driver.find_element_by_id("txtPlace").send_keys("存放地点" + v_tim)
        # 单价
        driver.find_element_by_id("numfieldAddPrice").send_keys(random.randint(5, 500))
        # 数量
        driver.find_element_by_id("numfieCount").send_keys(random.randint(1, 5000))
        # 内容简介
        v_description = "这本图书是一本很畅销的网络作品，这是测试说的。当前添加时间："
        driver.find_element_by_id("txtAddDescription").send_keys(v_description + v_tim)
        time.sleep(2)
        driver.find_element_by_id("BtnSaveForm").click()
        time.sleep(3)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "添加成功!" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/oa/test_0403_01_add.jpg")
                print(i.text)
                unittest.expectedFailure("test_0403_01_add")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(Bookes("test_0403_01_add"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)