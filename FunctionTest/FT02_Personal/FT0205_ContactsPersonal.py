
from PubliCode.onlineClass import *
from PubliCode.randData import *
'''
    *   Arvin
    *   2017-01-13
'''


class ContactsPersonal(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "个人事务", "通讯录", "个人通讯录")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM001018")

    # 个人事务-个人通讯录-新增数据功能
    def test_0205_01_add(self):
        """个人事务-个人通讯录-新增数据功能"""
        driver = self.driver
        driver.find_element_by_partial_link_text("新增").click()
        time.sleep(3)
        v_data = csv.reader(open(root_path() + 'PubliData/cvs/basedata.csv', 'r'))
        # 创建二维数组-8列
        v_list_data = [[] for i in range(8)]
        for i in v_data:
            # 对每列数组添加数据
            v_list_data[0].append(i[0])    # 姓名
            v_list_data[1].append(i[1])    # 电话
            v_list_data[2].append(i[2])    # 邮箱
            v_list_data[3].append(i[3])    # 英文名称
            v_list_data[4].append(i[4])    # 座机
            v_list_data[5].append(i[5])    # 职位
            v_list_data[6].append(i[6])    # 公司名称
            v_list_data[7].append(i[7])    # 地址
        v_tim = time.strftime("%Y%m%d %H%M%S")
        # 姓名
        driver.find_element_by_id("TempName").send_keys((v_list_data[0])[random.randint(1, len(v_list_data[0]))])
        # 手机号
        driver.find_element_by_id("TempTel").send_keys((v_list_data[1])[random.randint(1, len(v_list_data[1]))])
        # 邮箱地址
        driver.find_element_by_id("TempEmail").send_keys((v_list_data[2])[random.randint(1, len(v_list_data[2]))])
        # 英文名
        driver.find_element_by_id("EngName").send_keys((v_list_data[3])[random.randint(1, len(v_list_data[3]))])
        # 职位名称
        driver.find_element_by_id("DutyName").send_keys((v_list_data[5])[random.randint(1, 40)])
        # 单位名称
        driver.find_element_by_id("UnitName").send_keys((v_list_data[6])[random.randint(1, 330)])
        # 办公电话
        driver.find_element_by_id("TempPhoneNo").send_keys((v_list_data[4])[random.randint(1, len(v_list_data[4]))])
        # 传真
        driver.find_element_by_id("FaxNumber").send_keys((v_list_data[4])[random.randint(1, len(v_list_data[4]))])
        # 办公地址
        driver.find_element_by_id("Address").send_keys((v_list_data[7])[random.randint(1, 500)])
        # 备注
        driver.find_element_by_id("Remark").send_keys("自动添加的数据，这是测试说的" + v_tim)
        driver.find_element_by_id("btnSave").click()
        time.sleep(3)
        driver.switch_to.parent_frame()
        v_tip = driver.find_elements_by_class_name("bootbox-body")
        for i in v_tip:
            if "成功" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/oa/test_0205_01_add.jpg")
                print(i.text)
                unittest.expectedFailure("test_0205_01_add")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(ContactsPersonal("test_0205_01_add"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)