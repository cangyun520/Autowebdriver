# -*- coding: utf-8 -*-
from PubliCode.onlineClass import *
from PubliCode.randData import *


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
    def test_0804_01_add_add(self):
        """人事管理-员工异动-入职"""
        driver = self.driver
        driver.find_element_by_id("btnAdd").click()
        time.sleep(3)
        driver.switch_to.frame("winEdit_IFrame")        # 切换到新增页面
        v_tim = time.strftime("%Y%m%d %H:%M")
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
        v_type = random.choice(['非农业', '农业'])
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
                unittest.expectedFailure("test_0804_01_add")
                driver.get_screenshot_as_file(root_path() + "TestPicture/hr/test_0804_01_add.jpg")
                print("Error：" + i.text)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(TakingWork("test_0804_01_add"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)