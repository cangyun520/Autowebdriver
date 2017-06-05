
from PubliCode.onlineClass import *
from PubliCode.randData import *
from selenium.webdriver.common.action_chains import ActionChains


class CustomList(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_part_text(self, "销售管理", "客商管理", "客户管理列表")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM001103")

    """客商管理-客户管理列表-转正式客户"""
    def test_1802_01_BatchFormal(self):
        """客商管理-客户管理列表-转正式客户"""
        driver = self.driver
        driver.find_element_by_id("btnBatchFormal").click()
        time.sleep(1)
        v_tip = driver.find_elements_by_class_name("toast-message")
        for i in v_tip:
            if "请选择需要转为正式" in i.text:
                print(i.text)
            else:
                print(i.text)
                unittest.expectedFailure("test_1802_01_BatchFormal")

    """客商管理-客户管理列表-删除客户"""
    def test_1802_02_BatchDel(self):
        """客商管理-客户管理列表-删除客户"""
        driver = self.driver
        driver.find_element_by_id("btnBatchDel").click()
        time.sleep(1)
        v_tip = driver.find_elements_by_class_name("toast-message")
        for i in v_tip:
            if "请选择需要批量删除" in i.text:
                print(i.text)
            else:
                print(i.text)
                unittest.expectedFailure("test_1802_02_BatchDel")

    """客商管理-客户管理列表-转移"""
    def test_1802_03_BatchTransfer(self):
        """客商管理-客户管理列表-转移"""
        driver = self.driver
        driver.find_element_by_id("btnBatchTransfer").click()
        time.sleep(1)
        v_tip = driver.find_elements_by_class_name("toast-message")
        for i in v_tip:
            if "请选择需要批量转移" in i.text:
                print(i.text)
            else:
                print(i.text)
                unittest.expectedFailure("test_1802_03_BatchTransfer")

    """客商管理-客户管理列表-转移"""
    def test_1802_04_SynData(self):
        """客商管理-客户管理列表-转移"""
        driver = self.driver
        driver.find_element_by_id("btnSynData").click()
        time.sleep(1)
        v_tip = driver.find_elements_by_class_name("toast-message")
        for i in v_tip:
            if "没有需要同步的数据" in i.text:
                print(i.text)
            elif "已成功同步" in i.text:
                print(i.text)
            else:
                print(i.text)
                unittest.expectedFailure("test_1802_04_SynData")

    """客商管理-客户管理列表-新增单据功能"""
    def test_1802_05_Add(self):
        """客商管理-客户管理列表-新增单据功能"""
        driver = self.driver
        # 业务伙伴
        driver.find_element_by_id("btnAdd").click()
        time.sleep(5)
        # 进入到客户管理列表页面
        driver.switch_to.default_content()
        driver.switch_to.frame("frame_tab_PM001104")
        v_tim = time.strftime("%y%m%d%H%M%S")
        # 客户代码
        driver.find_element_by_id("txtCardCode").send_keys("KHXS" + str(random.randint(11111, 99999)))
        # 客户类型
        driver.find_element_by_id("txtCardType").click()
        time.sleep(1)
        for i in driver.find_elements_by_class_name("x-combo-list-item"):
            if i.text == random.choice(['正式客户', '潜在客户', '客户线索']):
                i.click()
                break
        # 客户名称
        driver.find_element_by_id("txtCardName").send_keys(i.text + v_tim + "公司")
        # 客户组
        driver.find_element_by_xpath("//*[@id='tfGroupCode_Container']/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")
        v_khlist = driver.find_elements_by_class_name("x-grid3-row")
        v_khlist[random.randint(0, len(v_khlist)-1)].click()
        driver.find_element_by_id("Button1").click()
        time.sleep(1)
        driver.switch_to.parent_frame()

        # 销售员窗体
        driver.find_element_by_xpath("//*[@id='tfSalesPerson_Container']/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")
        v_khlist = driver.find_elements_by_class_name("x-grid3-row")
        if len(v_khlist) > 0:
            v_khlist[random.randint(0, len(v_khlist) - 1)].click()
            driver.find_element_by_id("btnSelect").click()
        else:
            driver.find_element_by_id("Button2").click()
        time.sleep(1)
        driver.switch_to.parent_frame()
        # 电话，传真，站点，
        driver.find_element_by_id("txtCellular").send_keys("010-" + str(random.randint(111111, 999999)))
        driver.find_element_by_id("txtPhone1").send_keys("027-" + str(random.randint(111111, 999999)))
        driver.find_element_by_id("txtFax").send_keys("010-" + str(random.randint(111111, 999999)))
        driver.find_element_by_id("txtWebsite").send_keys(fun_data_www())
        # 邮箱
        driver.find_element_by_id("txtEmailAddress").send_keys(fun_data_email())
        # 备注页签
        driver.find_element_by_link_text("备注").click()
        time.sleep(1)
        driver.find_element_by_id("bzjy").send_keys(fun_data_character(100, 300))
        driver.find_element_by_id("btnSave").click()
        time.sleep(4)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功" in i.text:
                print(i.text)
            elif "流程已触发" in i.text:
                print(i.text)
            else:
                print(i.text)
                unittest.expectedFailure("test_1802_05_Add")
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_1802_05_Add.jpg")

    """客商管理-客户管理列表-更新联系人"""
    def test_1802_06_UpdatePerson(self):
        """客商管理-客户管理列表-客户主数据穿透功能"""
        driver = self.driver
        v_rows = driver.find_element_by_id("gridList").find_elements_by_tag_name("tr")
        if len(v_rows) > 1:
            # print(len(v_rows))
            if len(v_rows) > 10:
                v_cols = v_rows[random.randint(1, 9)].find_elements_by_tag_name("td")
            else:
                v_cols = v_rows[random.randint(1, len(v_rows)-1)].find_elements_by_tag_name("td")
            v_cols[2].click()
            time.sleep(5)
        driver.switch_to.default_content()
        # 进入到客户管理列表页面
        driver.switch_to.frame("frame_tab_PM001104")
        v_tim = time.strftime("%y%m%d%H%M%S")
        v_data = csv.reader(open(root_path() + 'PubliData/cvs/basedata.csv', 'r'))
        # 创建二维数组-3列
        v_list_data = [[] for i in range(3)]
        for i in v_data:
            # 对每列数组添加数据
            v_list_data[0].append(i[0])    # 姓名
            v_list_data[1].append(i[5])    # 职位
            v_list_data[2].append(i[7])    # 地址
        v_write_file = open(root_path() + 'PubliData/character5K.txt', 'r')
        v_lines = v_write_file.read()
        # 去掉税务注册输入框数据
        driver.find_element_by_id("txtGTSRegNo").clear()
        # 联系人页签
        driver.find_element_by_link_text("联系人").click()
        v_person = driver.find_element_by_id("GridPanel2")
        ActionChains(driver).context_click(v_person).perform()
        driver.find_element_by_id("AddRecord").click()
        time.sleep(1)
        # 联系人页签-新增联系人窗体
        # 联系人标识
        driver.find_element_by_id("TName").send_keys(v_tim)
        # 名
        driver.find_element_by_id("TFirstName").send_keys((v_list_data[0])[random.randint(1, len(v_list_data[0]))])
        # 头衔
        driver.find_element_by_id("TTitle1").send_keys((v_list_data[1])[random.randint(1, 40)])
        # 职位
        driver.find_element_by_id("TPosition").send_keys((v_list_data[1])[random.randint(1, 40)])
        # 姓
        driver.find_element_by_id("TLastName").send_keys(random.choice(
            ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '楮']))
        # 地址
        driver.find_element_by_id("TAddress").send_keys((v_list_data[2])[random.randint(1, 500)])
        # 电话1
        driver.find_element_by_id("TPhone1").send_keys("027-" + str(random.randint(111111, 999999)))
        # 电话2
        driver.find_element_by_id("TPhone2").send_keys("010-" + str(random.randint(111111, 999999)))
        # 移动电话
        v_iphone = random.choice(
            ['139', '188', '185', '136', '158', '151']
        )+"".join(random.choice("0123456789") for i in range(8))
        driver.find_element_by_id("TMobile").send_keys(v_iphone)
        # 传真
        driver.find_element_by_id("TFax").send_keys("027-" + str(random.randint(111111, 999999)))
        # 电子邮件
        driver.find_element_by_id("TEMail").send_keys("".join(random.choice("0123456789") for i in range(9)) + "@tech" + ".com")
        # 传呼机
        driver.find_element_by_id("TPager").send_keys("027-" + str(random.randint(111111, 999999)))
        # 备注1
        driver.find_element_by_id("TNote1").send_keys("备注1")
        # 备注2
        driver.find_element_by_id("TNote2").send_keys("备注2")
        # 密码
        driver.find_element_by_id("TPassword").send_keys("123456")
        # 出生城市
        driver.find_element_by_id("TBirthCity").send_keys(random.choice(
            ['北京', '上海', '深圳', '武汉', '成都', '郑州', '南昌', '哈尔滨', '贵阳']))
        # 出生日期
        driver.find_element_by_id("TBirthDate").click()
        for i in driver.find_elements_by_class_name("x-btn-mc"):
                if i.text == "今天":
                    i.click()
        driver.find_element_by_xpath("//*[@id='x-form-el-TSex']/div/img").click()
        # 性别
        driver.find_element_by_id("TSex").send_keys(random.choice(['男', '女']))
        # 职业
        driver.find_element_by_id("TProfession").send_keys((v_list_data[1])[random.randint(1, 40)])
        driver.find_element_by_id("btnYes").click()
        time.sleep(1)
        driver.find_element_by_id("btnUpdate").click()
        time.sleep(4)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        if len(v_tip) == 0:
            print("没有获取到提示窗体")
            unittest.expectedFailure("test_1801_02")
        else:
            for i in v_tip:
                if "成功" in i.text:
                    print(i.text)
                else:
                    driver.get_screenshot_as_file(root_path() + "TestPicture/test_1802_06_UpdatePerson.jpg")
                    print("Error：" + i.text)
                    unittest.expectedFailure("test_1802_06_UpdatePerson")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    unittest.main()