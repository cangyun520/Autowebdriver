# -*- coding: utf-8 -*-
from PubliCode.config import *
from PubliCode.onlineClass import *
from PubliCode.randData import *
from selenium.webdriver.common.action_chains import ActionChains


class TakingWork(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "人事管理", "员工异动", "入职")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000892")

    """人事管理-员工异动-入职"""

    def test_0541_01_add(self):
        """人事管理-员工异动-入职"""
        driver = self.driver
        driver.find_element_by_id("btnAdd").click()
        time.sleep(3)
        # 切换到新增页面
        driver.switch_to.frame("winEdit_IFrame")
        # 员工姓名
        driver.find_element_by_xpath("//*[@id='txtArchivesManageCode_Container']/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winItem_IFrame")
        v_yhlist = driver.find_elements_by_class_name("x-grid3-row")
        v_yhlist[random.randint(0, len(v_yhlist)-1)].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(1)
        driver.switch_to.parent_frame()
        # 机构部门
        driver.find_element_by_xpath("//*[@id='txtOrg_Container']/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winItem_IFrame")
        v_yhlist = driver.find_elements_by_class_name("x-grid3-row")
        v_yhlist[random.randint(0, len(v_yhlist)-1)].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(1)
        driver.switch_to.parent_frame()
        # 岗位
        driver.find_element_by_xpath("//*[@id='txtJob_Container']/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winItem_IFrame")
        v_yhlist = driver.find_elements_by_class_name("x-grid3-row")
        v_yhlist[random.randint(0, len(v_yhlist)-1)].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(1)
        driver.switch_to.parent_frame()
        # 级别
        driver.find_element_by_id("cmbLevel").click()
        v_level = random.choice(['一级', '二级', '三级', '四级', '五级', '六级', '七级', '八级', '九级', '十级'])
        v_levellist = driver.find_elements_by_class_name("x-combo-list-item")
        for i in v_levellist:
            if i.text == v_level:
                i.click()
                break
        # 员工类型
        driver.find_element_by_id("txtInType").click()
        v_type = random.choice(['基层管理', '一般员工', '中层管理', '高层管理'])
        v_typelist = driver.find_elements_by_class_name("x-combo-list-item")
        for i in v_typelist:
            if i.text == v_type:
                i.click()
                break
        # 员工状态
        driver.find_element_by_id("cmbUserStatus").click()
        v_type = random.choice(['正式员工', '试用员工'])
        v_typelist = driver.find_elements_by_class_name("x-combo-list-item")
        for i in v_typelist:
            if i.text == v_type:
                i.click()
                break
        # 自由流审批人选择
        ClasFlow.flow_free(self, "bear")
        driver.find_element_by_id("btnWorkflow").click()
        time.sleep(4)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "流程已触发" in i.text:
                print(i.text)
            elif "保存单据成功" in i.text:
                print(i.text)
            else:
                unittest.expectedFailure("test_0541_01_add")
                driver.get_screenshot_as_file(root_path() + "TestPicture/hr/test_0541_01_add.jpg")
                print("Error：" + i.text)

    """人事管理-员工异动-添加界面关闭功能"""
    def test_1002_02_look(self):
        """人事管理-员工异动-添加界面关闭功能"""
        driver = self.driver
        # 随机双击行数据进入到查看界面
        v_list = driver.find_elements_by_class_name("x-grid3-row")
        # 如果行列表无数据时则通过点击添加进入到页面
        if len(v_list) == 0:
            driver.find_element_by_id("btnAdd").click()
        else:
            ActionChains(driver).double_click(v_list[random.randint(0, len(v_list)-1)]).perform()
        time.sleep(3)
        # 切换到新增页面
        driver.switch_to.frame("winEdit_IFrame")
        driver.find_element_by_id("btnCancel").click()
        time.sleep(2)
        ClasForm.form_button_yes(self, "是")
        time.sleep(1)
        driver.switch_to.parent_frame()
        if driver.find_element_by_id("cbxPageSize").is_displayed():
            print("人事管理-员工异动-查看界面关闭功能OK")
        else:
            unittest.expectedFailure("test_1002_02")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()