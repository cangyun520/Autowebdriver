from PubliCode.onlineClass import *
from PubliCode.randData import *
import re
'''
    *   Arvin
    *   2017-06-23
'''


class DataRelated(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, u"订货管理", u"系统管理", u"常规设置", u"行格式自定义")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000255")

    '''系统管理-常规设置-添加分配规则'''
    def test_1615_01_AddFPGZ(self):
        """系统管理-警报设置-数据相关查询"""
        driver = self.driver
        # 获取文件名称
        driver.find_element_by_xpath(
            "//*[@id='ext-comp-1002']/table/tbody/tr/td/table/tbody/tr/td/div/div/div/img").click()
        time.sleep(1)
        v_lists = driver.find_elements_by_class_name("x-combo-list-item")
        v_meus = []
        for i in v_lists:
            if re.search(r'(物料)', i.text) or re.search(r'(服务)', i.text) or re.search(r'库存', i.text):
                v_meus.append(i.text)
            else:
                pass

        # 剔除多余数据
        for j in v_meus:
            l = ['调拨计划物料选择']
            for d in l:
                if d == j:
                    v_meus.remove(j)
        # print(v_meus)
        # quit()
        n = len(v_meus)
        m = 0

        # 开始循环
        while m < n:
            # 清理输入框
            driver.find_element_by_id("comboBoxXmlName").clear()
            driver.find_element_by_id("comboBoxXmlName").send_keys(v_meus[m])
            time.sleep(1)
            driver.find_element_by_id("comboHidColumn").click()
            time.sleep(3)
            driver.find_element_by_id("comboHidColumn").click()
            time.sleep(2)

            v_list = driver.find_elements_by_class_name("x-mcombo-text")
            for i in v_list:
                if "分配规则" == i.text:
                    i.click()
                    # time.sleep(1)
                    # 显示隐藏列
                    driver.find_element_by_id("btnHidColumn").click()
                    time.sleep(1)
                    driver.find_element_by_id("btnSave").click()
                    time.sleep(2)
                    v_tip = driver.find_elements_by_class_name("ext-mb-text")
                    # 提示
                    for j in v_tip:
                        try:
                            "保存成功" in j.text
                            ClasForm.form_button_yes(self, "确定")
                            print(v_meus[m])
                        except Exception as err:
                            driver.get_screenshot_as_file(root_path() + "TestPicture/SYS/test_1615_01_AddFPGZ.jpg")
                            print(err)
                            unittest.expectedFailure("test_1615_01_AddFPGZ")
                    break
            m += 1

    '''系统管理-常规设置-隐藏特定行字段'''

    def test_1615_02_HideZD(self):
        """系统管理-警报设置-数据相关查询"""
        driver = self.driver
        v_lists = driver.find_elements_by_class_name("x-grid3-hd-row")
        fro
        i in v_lists
        v_meus = []


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
