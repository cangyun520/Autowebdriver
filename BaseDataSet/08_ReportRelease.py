
from PubliCode.onlineClass import *


class DB08_ReportRelease(unittest.TestCase):
    def setUp(self):
        ClasLogin.login_setup(self)

    def test_1308_01_add(self):
        """系统管理-报表&打印-报表发布之水晶打印水晶报表发布"""
        driver = self.driver
        driver.find_element_by_link_text(u"系统管理").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"报表&打印").click()
        driver.find_element_by_link_text(u"报表发布").click()
        # 移动到页面顶部，防止对象遮挡
        time.sleep(3)
        ClasForm.form_top(driver="driver", number=0)
        driver.switch_to_frame("frame_tab_PM000013")
        time.sleep(1)
        driver.find_element_by_id("btnAddSJ").click()
        time.sleep(3)
        driver.switch_to_frame("winSetReport_IFrame")       # 切换到水晶报表发布窗体
        v_tim = time.strftime("%y%m%d%H%M")
        # 标题
        driver.find_element_by_id("txtTitle").send_keys("销售报价单（打印）Auto")
        time.sleep(1)
        # 分类
        driver.find_element_by_id("cbxType").click()
        driver.find_elements_by_class_name("x-combo-list-item")[2].click()
        # 报表用途
        driver.find_element_by_id("cbxUseClass").send_keys("打印")
        # 数据库
        driver.find_element_by_id("cbxConnectionStrings").click()
        for i in driver.find_elements_by_class_name("x-combo-list-item"):
            if i.text == "SBO":
                i.click()
                break
        # 描述
        driver.find_element_by_id("txtDescription").send_keys("业务单据公共打印报表Auto" + v_tim)
        # 上传水晶报表
        driver.find_element_by_id("txtPath").click()
        time.sleep(3)
        driver.switch_to_frame("panelUploadCrystalReport_IFrame")
        time.sleep(5)
        driver.switch_to.parent_frame()
        driver.find_element_by_id("btnSave").click()
        time.sleep(5)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功" in i.text:
                print("系统管理-报表&打印-报表发布之水晶打印水晶报表发布OK")
            else:
                print("BUG 系统管理-报表&打印-报表发布之水晶打印水晶报表发布失败")
                unittest.expectedFailure("test_1308_01_add")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()