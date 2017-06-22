
from selenium.webdriver.common.action_chains import ActionChains
from PubliCode.onlineClass import *
import sys


class FreeAdmin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        # 打开登录页面
        ClasLogin.login_setup_admin(self)

    # 首页-流程审批
    def test_1301_bearadmin(self):
        """Online流程中间审批通过"""
        driver = self.driver
        time.sleep(2)
        v_list = driver.find_elements_by_class_name("task-title-sp")
        # 创建迭代
        if len(v_list) != 0:
            v_a = 0
            while v_a < len(v_list):
                v_list2 = driver.find_elements_by_class_name("task-title-sp")
                # 取第一条
                ActionChains(driver).double_click(v_list2[0]).perform()
                time.sleep(4)
                # 获取对象
                var_active = driver.find_element_by_class_name("active")
                print(var_active.text)
                # 获取对象ID
                var_active_id = var_active.get_attribute("id")
                # 截取第3个字符到结尾
                var_menu_id = var_active_id[3:]
                driver.switch_to.frame("frame" + var_menu_id)
                # 审批通过 ,默认通过，兼容打回
                if driver.find_element_by_id("btnPass").is_displayed():
                    driver.find_element_by_id("btnPass").click()
                elif driver.find_element_by_id("btnReSave").is_displayed():
                    driver.find_element_by_id("btnReSave").click()

                v_tip = driver.find_elements_by_class_name("ext-mb-text")
                for i in v_tip:
                    if "成功" in i.text:
                        print(i.text)
                    elif "流程已结束" in i.text:
                        print(i.text)
                    elif "已结算" in i.text:
                        print(i.text)
                    else:
                        print(i.text)
                        unittest.expectedFailure("test_1301_bearadmin")
                ClasForm.form_button_yes(self, "确定")
                # 返回初始页面
                driver.switch_to.default_content()
                time.sleep(1)
                v_a += 1
        else:
            print("当前没有待审批流程!!!")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(FreeAdmin("test_1301_bearadmin"))
    v_tim = time.strftime("%y%m%d%H%M")
    FileName = root_path() + 'TestReport/STRport/' + v_tim + ' ST01_Index.html'
    ReportFile = open(FileName, 'wb')
    runner = HTMLTestRunner(stream=ReportFile,
                            title="首页冒烟测试",
                            description="用例执行情况")
    # 运行测试用例集合
    runner.run(testsuit)
    ReportFile.close()
