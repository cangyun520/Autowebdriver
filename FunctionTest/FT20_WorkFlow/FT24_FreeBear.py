
from selenium.webdriver.common.action_chains import ActionChains
from PubliCode.onlineClass import *
import sys


class FreeBear(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        # 打开登录页面
        ClasLogin.login_setup_bear(self)

    # 首页-------流程审批
    def test_0101_bearPass(self):
        """Online流程中间审批通过"""
        driver = self.driver
        time.sleep(2)
        v_list = driver.find_elements_by_class_name("task-title-sp")
        # 创建迭代
        if len(v_list) != 0:
            v_a = 0
            while v_a < len(v_list):
                v_list2 = driver.find_elements_by_class_name("task-title-sp")
                ActionChains(driver).double_click(v_list2[0]).perform()              # 取第一条
                time.sleep(4)
                var_active = driver.find_element_by_class_name("active")            # 获取对象
                # print(var_active.text)
                var_active_id = var_active.get_attribute("id")                      # 获取对象ID
                var_menu_id = var_active_id[3:]                                      # 截取第3个字符到结尾
                driver.switch_to_frame("frame" + var_menu_id)
                # 老页面自由流审批人选择-admin-审批通过
                if driver.find_element_by_id("btnSelectAppover").is_displayed():
                    driver.find_element_by_id("btnSelectAppover").click()
                    time.sleep(2)
                    driver.switch_to_frame("winSelectUser_IFrame")      # 切换到用户信息选择窗体
                    driver.find_element_by_id("txtUserName").send_keys("admin")
                    driver.find_element_by_id("btnQuery").click()
                    time.sleep(2)
                    driver.find_elements_by_class_name("x-grid3-row")[0].click()
                    driver.find_element_by_id("btnConfirm").click()
                    driver.switch_to.parent_frame()
                    time.sleep(1)
                # 新页面自由流审批人选择-admin-审批通过
                elif driver.find_element_by_id("userphoto").is_displayed():
                    driver.find_element_by_id("userphoto").click()
                    time.sleep(2)
                    driver.find_element_by_xpath("//*[@id='gridUser_filter']/label/input").send_keys("admin")
                    time.sleep(1)
                    driver.find_element_by_class_name("odd").click()
                    driver.find_element_by_id("btnUserOK").click()
                    time.sleep(1)
                driver.find_element_by_id("btnPass").click()
                # 移动到页面顶部，防止对象遮挡
                v_tip = driver.find_elements_by_class_name("ext-mb-text")
                v_masg = driver.find_elements_by_class_name("bootbox-body")
                for i in v_tip:
                    if "成功" in i.text:
                        print(i.text)
                    elif "已结算其中一个基本单据" in i.text:
                        print(i.text)
                    else:
                        print(i.text)
                        unittest.expectedFailure("test_0101_bearPass")
                ClasForm.form_button_yes(self, "确定")
                # 返回初始页面
                driver.switch_to_default_content()
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
    testsuit.addTest(FreeBear("test_0101_bearPass"))
    v_tim = time.strftime("%y%m%d%H%M")
    FileName = root_path() + 'TestReport/STRport/' + v_tim + ' ST01_Index.html'
    ReportFile = open(FileName,'wb')
    runner = HTMLTestRunner(stream=ReportFile,
                            title="首页冒烟测试",
                            description="用例执行情况")
    # 运行测试用例集合
    runner.run(testsuit)
    ReportFile.close()