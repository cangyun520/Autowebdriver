
from PubliCode.onlineClass import *
from PubliCode.randData import *
from selenium.webdriver.common.action_chains import ActionChains
import win32api


class PurchCredit(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_part_text(self, "采购管理", "应付贷项凭证")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000219")
        # 排除自定义字段遮挡干扰
        ClasForm.form_field_hide(self, driver)

    # 采购管理---应付贷项凭证
    def test_0708_01(self):
        """采购管理-应付贷项凭证-新增单据功能检查"""
        driver = self.driver
        driver.find_element_by_xpath("//*[@id='CompositeField2_Container']/div/div/div/span").click()
        time.sleep(3)
        driver.switch_to_frame("winAdd_IFrame")     # 切换到业务伙伴选择窗体
        driver.find_element_by_id("gpSelect").click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        v_tim = time.strftime("%Y-%m-%d %H:%M:%S")
        driver.switch_to.parent_frame()
        # 有效期至
        ClasForm.form_today(self, "dfDocDueDate")
        driver.find_element_by_xpath(
            "//*[@id='GridPanelItem']/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath(
            "//*[@id='GridPanelItem']/div/div/div/div/div[2]/div[2]/div/span").click()
        time.sleep(2)
        driver.switch_to_frame("winAdd_IFrame")     # 切换到物料选择窗体
        driver.find_element_by_id("txtSearchText").send_keys("A000")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(1)
        v_wlcode = driver.find_elements_by_class_name("x-grid3-row")
        v_total = 0
        while v_total <= 4:
            v_wlcode[v_total].click()
            v_total += 1
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        driver.switch_to.parent_frame()
        driver.find_element_by_id("txtComments").send_keys("应付贷项凭证添加Auto" + v_tim)
        driver.find_element_by_id("btnSave").click()
        time.sleep(4)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功" in i.text:
                print(i.text)
            elif "流程已触发" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_0708_01.jpg")
                print(i.text)
                unittest.expectedFailure("test_0708_01")

    # 采购管理-应付贷项凭证-业务伙伴编号为空穿透提示检查
    def test_0708_02_Client(self):
        """采购管理-应付贷项凭证-业务伙伴编号为空穿透提示检查"""
        driver = self.driver
        driver.find_element_by_id("btnGoOCRD").click()      # 业务伙伴主数据穿透
        time.sleep(2)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "业务伙伴为空" in i.text:
                print(i.text)
            else:
                print(i.text)
                unittest.expectedFailure("test_0708_02_Client")

    # 采购管理-应付贷项凭证-伙伴主数据穿透功能检查
    def test_0708_03_First(self):
        """采购管理-应付贷项凭证-业务伙伴主数据穿透功能检查"""
        driver = self.driver
        driver.find_element_by_id("btnFirst").click()
        time.sleep(3)
        driver.find_element_by_id("btnGoOCRD").click()      # 业务伙伴主数据穿透
        time.sleep(3)
        driver.switch_to_frame("winActivity_IFrame")     # 切换到业务伙伴主数据查看页面
        v_general = driver.find_element_by_link_text("常规")
        try:
            v_general.is_displayed()
            print("采购管理-应付贷项凭证穿透到伙伴主数据页面显示OK")
        except ImportError:
            print("BUG 采购管理-应付贷项凭证穿透到伙伴主数据页面显示异常")
            driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_0708_03_First.jpg")
            unittest.expectedFailure("test_0708_03_First")

    # 采购管理-应付贷项凭证-复制功能
    def test_0708_04_copy(self):
        """采购管理-应付贷项凭证-复制功能"""
        driver = self.driver
        driver.find_element_by_id("btnPrevious").click()
        time.sleep(3)
        v_object = driver.find_element_by_id("tfCardCode")
        ActionChains(driver).context_click(v_object).perform()
        time.sleep(1)
        driver.find_element_by_id("MenuCopy").click()
        time.sleep(3)
        v_tim = time.strftime("%Y-%m-%d %H:%M:%S")
        # 选择客户
        driver.find_element_by_xpath("//*[@id='CompositeField2_Container']/div/div/div/span").click()
        time.sleep(3)
        driver.switch_to_frame("winAdd_IFrame")     # 切换到业务伙伴选择窗体
        driver.find_element_by_id("txtSearchText").send_keys("V")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(2)
        driver.find_elements_by_class_name("x-grid3-row")[1].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(2)
        driver.switch_to.parent_frame()
        # 是否依据新的业务伙伴数据更新凭证行
        for i in driver.find_elements_by_tag_name("button"):
            if i.text == "是":
                i.click()
                break
        # 有效期至
        ClasForm.form_today(self, "dfDocDueDate")
        # 备注
        driver.find_element_by_id("txtComments").send_keys(v_tim + "单据复制添加Auto")
        time.sleep(1)
        driver.find_element_by_id("btnSave").click()
        time.sleep(4)
        ClasForm.form_top(self, 0)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功，单号" in i.text:
                print(i.text)
            elif "流程已触发" in i.text:
                print(i.text)
            else:
                print(i.text)
                unittest.expectedFailure("test_0708_04_copy")

    # 采购管理-应付贷项凭证-目标凭证查看
    def test_0707_05_target(self):
        """采购管理-应付贷项凭证-目标凭证查看"""
        driver = self.driver
        driver.find_element_by_id("btnFirst").click()
        time.sleep(4)
        if driver.find_element_by_id("btnTarget").is_displayed():
            driver.find_element_by_id("btnTarget").click()
            time.sleep(3)
            driver.switch_to_default_content()
            v_active = driver.find_element_by_class_name("active")        # 获取对象
            # print(v_active.text)
            v_active_id = v_active.get_attribute("id")       # 获取对象ID
            v_menu_id = v_active_id[3:]       # 截取第3个字符到结尾
            driver.switch_to_frame("frame" + v_menu_id)
            if driver.find_element_by_id("btnBase").is_displayed():
                print("目标凭证点击穿透查看OK")
        else:
            print("当前单据状态未清")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(PurchCredit("test_050404_01_Add"))

    runner = unittest.TextTestRunner()
    runner.run(testsuit)