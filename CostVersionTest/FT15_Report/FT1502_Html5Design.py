
from selenium.webdriver.common.action_chains import ActionChains
from PubliCode.onlineClass import *
from PubliCode.randData import *


class Html5Design(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, u"系统管理", u"报表设置", u"Html5报表设计器")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000656")

    """系统管理-报表设置-SQL为空检验"""
    def test_1502_01_sqlNull(self):
        """系统管理-报表设置-SQL为空检验"""
        driver = self.driver
        driver.find_element_by_id("btnSwitchingView").click()
        time.sleep(2)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "SQL语句为空" in i.text:
                print(i.text)
            else:
                print(i.text)
                unittest.expectedFailure("test_1502_01_sqlNull")

    # 系统管理-报表设置-数据为空导出
    def test_1502_02_exportNull(self):
        """系统管理-报表设置-数据为空导出"""
        driver = self.driver
        driver.find_element_by_id("btnReset").click()
        driver.find_element_by_id("btnexl").click()
        time.sleep(2)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "没有导出数据" in i.text:
                print(i.text)
            else:
                print(i.text)
                unittest.expectedFailure("test_1502_02_exportNull")

    """费用管理-费用申请-添加界面关闭功能"""
    def test_1502_03_add(self):
        driver = self.driver
        # 选择SBO数据库
        driver.find_element_by_id("cboDataBase").click()
        time.sleep(1)
        v_tim = time.strftime("%Y-%m-%d %H:%M:%S")
        driver.find_elements_by_class_name("x-combo-list-item")[1].click()
        driver.find_element_by_id("btnReset").click()
        time.sleep(1)
        # print(fun_data_sql("ordr.txt"))
        driver.find_element_by_id("txtSql").send_keys(fun_data_sql("ordr.txt"))
        time.sleep(1)
        driver.find_element_by_id("btnCarriedOut").click()
        time.sleep(3)
        # 配置项目-选择图形
        driver.find_element_by_id("cbxGraph").click()
        time.sleep(2)
        v_graphics_check = random.choice(["柱状图", "折线图"])
        # print(v_graphics_check)
        v_list = driver.find_elements_by_class_name("x-combo-list-item")
        for i in v_list:
            if v_graphics_check in i.text:
                i.click()
                break
                time.sleep(2)
        # 配置项目-图例
        driver.find_element_by_id("muCbxTl").click()
        for i in driver.find_elements_by_class_name("x-mcombo-text"):
            i.click()
        driver.find_element_by_id("muCbxTl").click()
        time.sleep(2)
        # 配置项目-横轴
        driver.find_element_by_id("cbxX").click()
        time.sleep(2)
        v_x_check = random.choice(["客户名称", "单据税额", "单据总计", "过帐时间", "客户编码", "单据编号"])
        v_list = driver.find_elements_by_class_name("x-combo-list-item")
        for i in v_list:
            if v_x_check in i.text:
                i.click()
                break
                time.sleep(1)
        driver.find_element_by_id("btnItemSave").click()
        time.sleep(5)
        # 报表分类
        driver.find_element_by_id("cboRPType").click()
        time.sleep(1)
        v_type_check = random.choice(["管理层报表", "财务报表", "销售报表", "采购报表", "库存报表", "公共报表"])
        v_list = driver.find_elements_by_class_name("x-combo-list-item")
        for i in v_list:
            if v_type_check in i.text:
                i.click()
                break
                time.sleep(1)
        # 标题
        driver.find_element_by_id("txtTitle").send_keys(v_type_check + v_tim)
        time.sleep(1)
        driver.find_element_by_id("btnSave").click()
        time.sleep(3)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/test_1502_01_add.jpg")
                print(i.text)
                unittest.expectedFailure("test_1502_01_add")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(Html5Design("test_0904_01_add"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)