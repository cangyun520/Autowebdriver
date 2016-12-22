
from selenium.webdriver.common.action_chains import ActionChains
from PubliCode.onlineClass import *
from PubliCode.randData import *
import win32api
from FunctionTest import *


class FreeProcesses(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        # 打开登录页面
        ClasLogin.login_setup_arvin(self)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest()
    testsuit.addTest()
    testsuit.addTest()
    runner = unittest.TextTestRunner()
    runner.run(testsuit)