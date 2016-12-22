
from PubliCode.onlineClass import *
from PubliCode.randData import *


class ProjectApproval(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        ClasMenu.menu_full_text(self, "项目管理", "项目立项")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to_frame("frame_tab_PM000755")

    # 项目管理-项目立项-添加单据
    def test_050302_01_add(self):
        """项目管理-项目立项-添加单据功能"""
        driver = self.driver
        v_tim = time.strftime("%y%m%d%H%M")
        # 项目编号
        driver.find_element_by_id("txtProjectCode").send_keys("PRJNO_" + v_tim)
        # 项目名称
        write_file = open(root_path() + 'PubliData/character5K.txt', 'r')
        v_lines = write_file.read()
        v_project = random.choice(
            ['南方电网公司', '国家电网公司', '郑州铁路局', '湖北交通局', '广西税务局', '上海进出口局', '南昌盐业公司', '新疆烟草公司', '云南公安厅', '武汉移动通信', '南京移动通信', '青海旅游局']
        )
        driver.find_element_by_id("txtProjectName").send_keys(v_project + "21世纪信息化总建设--" + v_tim)
        # 提前执行合同
        driver.find_element_by_id("cbIshasContract").click()
        driver.find_element_by_id("btnSave").click()
        time.sleep(3)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "添加成功" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_050302_01_add.jpg")
                print(i.text)
                unittest.expectedFailure("test_050302_01_add")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(ProjectApproval("test_050302_01_add"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)