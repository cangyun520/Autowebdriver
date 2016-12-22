
from selenium.webdriver.common.action_chains import ActionChains
from PubliCode.onlineClass import *
from PubliCode.randData import *


class Borrowing(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "费用管理", "借款")
        # 移动到页面顶部，防止对象遮挡
        js = "window.scrollTo(0,0)"
        driver.execute_script(js)
        driver.switch_to.frame("frame_tab_PM000768")

    """费用管理-借款-单据添加功能"""
    def test_0903_01_add(self):
        """费用管理-借款-单据添加功能"""
        driver = self.driver
        driver.find_element_by_id("btnAdd").click()
        time.sleep(3)
        driver.switch_to.frame("winActivity_IFrame")        # 切换到新增页面
        v_tim = time.strftime("%y%m%d%H%M")
        driver.find_element_by_id("IsReturnTiem").send_keys(time.strftime("%Y-%m-%d"))       # 预计归还时间
        driver.find_element_by_id("Sum").send_keys(random.randint(100, 5000))        # 借款金额
        driver.find_element_by_xpath("//*[@id='ProjectCode_Container']/div/span").click()        # 项目
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")
        v_Projectlist = driver.find_elements_by_class_name("x-grid3-row")
        v_Projectlist[random.randint(0, (len(v_Projectlist)-1))].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(1)
        driver.switch_to.parent_frame()
        # 开户银行
        driver.find_element_by_id("AccountBank").send_keys(fun_data_bank())
        # 银行账号
        driver.find_element_by_id("Account").send_keys(fun_idcard())
        # 开户姓名
        driver.find_element_by_id("AccountName").send_keys(fun_data_name())
        # 借款事由
        driver.find_element_by_id("Remark").send_keys(
            "这是一张借款单Auto，这是测试说的Auto。申请日期：" + v_tim)
        # 调用自由流审批人选择函数
        ClasFlow.flow_free(self, "bear")
        driver.find_element_by_id("btnWorkflow").click()
        time.sleep(4)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "流程已触发" in i.text:
                print(i.text)
            elif "成功" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/oa/test_0903_01_add.jpg")
                print(i.text)
                unittest.expectedFailure("test_0903_01_add")

    """费用管理-借还款-借款界面关闭功能"""
    def test_0903_02(self):
        """费用管理-借还款-借款界面关闭功能"""
        driver = self.driver
        # 随机双击行数据进入到查看界面
        v_list = driver.find_elements_by_class_name("x-grid3-row")
        # 如果行列表无数据时则通过点击添加进入到页面
        if len(v_list) == 0:
            driver.find_element_by_id("btnAdd").click()
        else:
            ActionChains(driver).double_click(v_list[random.randint(0, len(v_list)-1)].click()).perform()
        time.sleep(3)
        driver.switch_to.frame("winActivity_IFrame")        # 切换到新增页面
        driver.find_element_by_id("btnCancel").click()
        time.sleep(2)
        ClasForm.form_button_yes(self, "是")
        driver.switch_to.parent_frame()
        try:
            driver.find_element_by_id("btnAdd").is_displayed()
            print("费用管理-费用申请-查看界面关闭功能OK")
        except ImportError:
            unittest.expectedFailure("test_0903_02")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(Borrowing("test_0904_01_add"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)