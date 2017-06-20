# -*- coding: utf-8 -*-
from PubliCode.config import *
from PubliCode.onlineClass import *
from PubliCode.randData import *
'''
    *   Arvin
    *   2017-01-13
'''


class MeetArchives(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "行政办公", "会议室管理", "会议室档案")
        time.sleep(2)
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000799")

    '''行政办公-会议室管理-会议室档案添加'''
    def test_0404_01_add(self):
        """行政办公-会议室管理-会议室档案添加功能"""
        driver = self.driver
        driver.find_element_by_id("btnAdd").click()
        v_tim = time.strftime("%y%m%d%H%M")
        driver.find_element_by_id("txtAddName").send_keys("会议室名称" + v_tim)
        time.sleep(1)
        # 可容纳人数
        driver.find_element_by_id("numfieCount").send_keys(random.randint(1, 9999))
        time.sleep(1)
        # 设备情况
        driver.find_element_by_id("txtAddCondition").send_keys("设备一切正常Auto" + v_tim)
        # 所在地点
        driver.find_element_by_id("txtAddPlace").send_keys("公司大厦内部")
        # 会议室管理员
        driver.find_element_by_id("txtAddManager").send_keys("Python童鞋")
        # 会议室描述
        driver.find_element_by_id("txtAddDecription").send_keys("会议室设备状况良好，可以使用Auto。检查日期：" + v_tim)
        driver.find_element_by_id("BtnSaveForm").click()
        time.sleep(3)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "添加成功!" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/oa/test_0404_01_add.jpg")
                print(i.text)
                unittest.expectedFailure("test_0404_01_add")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(MeetArchives("test_0404_01_add"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)