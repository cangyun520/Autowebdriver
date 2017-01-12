from PubliCode.onlineClass import *
from PubliCode.randData import *


class BusinessActivity(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        ClasMenu.menu_full_text(self, "销售管理", "客商管理", "业务活动")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000740")

    # 业务活动---业务活动
    def test_1804_01_call(self):
        """业务活动-业务活动-业务活动功能"""
        driver = self.driver
        v_tim = time.strftime("%y%m%d%H%M%S")
        # 业务伙伴代码
        driver.find_element_by_xpath("//*[@id='bodyContent_ctl37_Container']/div/div/div/span").click()
        time.sleep(3)
        # 切换到业务伙伴选择窗体
        driver.switch_to.frame("winAdd_IFrame")
        driver.find_element_by_id("txtCodeWhere").send_keys("C")
        driver.find_element_by_id("Button2").click()
        time.sleep(2)
        driver.find_elements_by_class_name("x-grid3-row")[2].click()
        driver.find_element_by_id("Button13").click()
        time.sleep(3)
        driver.switch_to.parent_frame()
        # 联系人
        driver.find_element_by_id("cmbCntctCode").click()
        driver.find_elements_by_class_name("x-combo-list-item")[0].click()
        # 备注
        driver.find_element_by_id("txtDetail").send_keys("这是一次商务测试活动Auto。这是测试说的" + v_tim)
        # 内容页签
        driver.find_element_by_link_text("内容").click()
        time.sleep(1)
        write_file = open(root_path() + 'PubliData/character5K.txt', 'r')
        v_lines = write_file.read()
        driver.find_element_by_id("txtNotes").send_keys(v_lines[300:1300])
        time.sleep(2)
        # 链接凭证页签-单据类型
        driver.find_element_by_link_text("链接凭证").click()
        time.sleep(1)
        driver.find_element_by_id("cmbDocType").click()
        time.sleep(2)
        driver.find_elements_by_class_name("x-combo-list-item")[3].click()
        time.sleep(2)
        # 链接凭证页签-单据编号
        driver.find_element_by_xpath("//*[@id='txtDocNum_Container']/div/span").click()
        time.sleep(3)
        # 切换到单据选择窗体
        driver.switch_to.frame("winAdd_IFrame")
        v_djlist = driver.find_elements_by_class_name("x-grid3-row")
        v_djlist[random.randint(1, len(v_djlist) -1)].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(2)
        driver.switch_to.parent_frame()
        # 添加
        driver.find_element_by_id("btnSave").click()
        time.sleep(3)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_1804_01_call.jpg")
                # print(i.text)
                unittest.expectedFailure("test_1804_01_call")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(BusinessActivity("test_1804_01_call"))

    runner = unittest.TextTestRunner()
    runner.run(testsuit)