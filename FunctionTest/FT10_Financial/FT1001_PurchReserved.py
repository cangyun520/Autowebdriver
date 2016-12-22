
from PubliCode.randData import *
from PubliCode.onlineClass import *
from selenium.webdriver.common.action_chains import ActionChains
import win32api


class PurchReserved(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "财务管理", "财务付款")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM001079")

    # 财务管理---财务付款
    def test_1001_01_way(self):
        """财务管理-付款-金额为空校验付款方式"""
        driver = self.driver
        driver.find_element_by_id("btnPay").click()
        time.sleep(2)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "到期总金额不能为空" in i.text:
                print(i.text)
            else:
                print(i.text)
                unittest.expectedFailure("test_1001_01_way")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(PurchReserved("test_050509_01_Add"))
    runner = unittest.TextTestRunner()
    runner.run(testsuit)