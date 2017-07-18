
from selenium.webdriver.common.action_chains import ActionChains
from PubliCode.onlineClass import *
from PubliCode.randData import *


class CustomerMaster(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "销售管理", "客商管理", "客户主数据")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000067")

    '''客商管理-客户主数据-新增单据功能'''
    def test_1801_01_Add(self):
        """客商管理-客户主数据-新增单据功能"""
        driver = self.driver
        v_tim = time.strftime("%y%m%d%H%M%S")
        # 客户代码
        driver.find_element_by_id("txtCardCode").send_keys("KH" + str(random.randint(11111, 99999)))
        # 客户名称
        driver.find_element_by_id("txtCardName").send_keys("客户Au" + v_tim + "股份公司")
        # 外文名称
        driver.find_element_by_id("txtCardFName").send_keys(fun_data_englishname())
        # 组
        driver.find_element_by_xpath("//*[@id='tfGroupCode_Container']/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")
        v_khlist = driver.find_elements_by_class_name("x-grid3-row")
        v_khlist[random.randint(0, len(v_khlist)-1)].click()
        driver.find_element_by_id("Button1").click()
        time.sleep(1)
        driver.switch_to.parent_frame()
        # 电话，传真，站点，
        driver.find_element_by_id("txtPhone1").send_keys("027-" + str(random.randint(111111, 999999)))
        driver.find_element_by_id("txtPhone2").send_keys("010-" + str(random.randint(111111, 999999)))
        driver.find_element_by_id("txtFax").send_keys("010-" + str(random.randint(111111, 999999)))
        driver.find_element_by_id("txtWebsite").send_keys(fun_data_www())
        # 邮箱
        driver.find_element_by_id("txtEmailAddress").send_keys(fun_data_email())
        # 移动电话
        driver.find_element_by_id("txtCellular").send_keys(fun_data_mobile())
        # 备注
        driver.find_element_by_id("txtNotes").send_keys("自动添加的客户" + v_tim)
        time.sleep(1)
        # 业务伙伴项目
        driver.find_element_by_xpath("//*[@id='txtProjectCode_Container']/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")
        v_prjlist = driver.find_elements_by_class_name("x-grid3-row")
        v_prjlist[random.randint(0, len(v_prjlist) - 1)].click()
        driver.find_element_by_id("Button11").click()
        time.sleep(2)
        driver.switch_to.parent_frame()
        # 备注页签
        driver.find_element_by_link_text("备注").click()
        time.sleep(1)
        driver.find_element_by_id("bzjy").send_keys(fun_data_character(100, 300))
        time.sleep(2)
        driver.find_element_by_id("btnSave").click()
        time.sleep(5)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_1801_01_Add.jpg")
                print(i.text)
                unittest.expectedFailure("test_1801_01_Add")

    '''客商管理-客户主数据-更新添加联系人'''
    def test_1801_02(self):
        """客商管理-客户主数据-更新添加联系人"""
        driver = self.driver
        driver.find_element_by_id("btnLast").click()
        v_tim = time.strftime("%y%m%d%H%M%S")
        time.sleep(4)
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
        v_write_file.close()

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
        driver.find_element_by_id("TPosition").send_keys(fun_data_job())
        # 姓
        driver.find_element_by_id("TLastName").send_keys(fun_data_surname())
        # 地址
        driver.find_element_by_id("TAddress").send_keys(fun_data_address())
        # 电话1
        driver.find_element_by_id("TPhone1").send_keys(fun_data_tel())
        # 电话2
        driver.find_element_by_id("TPhone2").send_keys(fun_data_tel())
        # 移动电话
        driver.find_element_by_id("TMobile").send_keys(fun_data_mobile())
        # 传真
        driver.find_element_by_id("TFax").send_keys(fun_data_tel())
        # 电子邮件
        driver.find_element_by_id("TEMail").send_keys(fun_data_email())
        # 传呼机
        driver.find_element_by_id("TPager").send_keys(fun_data_tel())
        # 备注1
        driver.find_element_by_id("TNote1").send_keys("备注1")
        # 备注2
        driver.find_element_by_id("TNote2").send_keys("备注2")
        # 密码
        driver.find_element_by_id("TPassword").send_keys("123456")
        # 出生国家
        driver.find_element_by_id("TPlaceOfBirth").click()
        driver.find_elements_by_class_name("x-combo-list-item")[3].click()
        # 出生城市
        driver.find_element_by_id("TBirthCity").send_keys(fun_data_city())
        # 出生日期
        driver.find_element_by_id("TBirthDate").click()
        for i in driver.find_elements_by_class_name("x-btn-mc"):
                if i.text == "今天":
                    i.click()
        driver.find_element_by_xpath("//*[@id='x-form-el-TSex']/div/img").click()
        # 性别
        driver.find_element_by_id("TSex").send_keys(random.choice(['男', '女']))
        # 职业
        driver.find_element_by_id("TProfession").send_keys(fun_data_position())
        driver.find_element_by_id("btnYes").click()
        time.sleep(1)
        driver.find_element_by_id("btnSave").click()
        time.sleep(4)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        if len(v_tip) == 0:
            print("没有获取到提示窗体")
            unittest.expectedFailure("test_1801_02")
        else:
            for i in v_tip:
                print(i.text)
                if "成功" in i.text:
                    print(i.text)
                else:
                    driver.get_screenshot_as_file(root_path() + "TestPicture/test_1801_02.jpg")
                    print("Error：" + i.text)
                    unittest.expectedFailure("test_1801_02")

    '''客商管理-客户主数据-查询功能'''
    def test_1801_03_search(self):
        """客商管理-客户主数据-查询功能"""
        driver = self.driver
        driver.find_element_by_id("btnSearch").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")
        v_khlist = driver.find_elements_by_class_name("x-grid3-row")
        v_khlist[random.randint(0, len(v_khlist) - 1)].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(3)
        driver.switch_to.parent_frame()
        driver.find_element_by_id("btnSave").click()
        time.sleep(4)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/erp/test_1801_03_search.jpg")
                print(i.text)
                unittest.expectedFailure("test_1801_03_search")

    '''客商管理-客户主数据-更新添加地址'''
    def test_1801_04(self):
        """客商管理-客户主数据-更新添加地址"""
        driver = self.driver
        v_tim = time.strftime("%y%m%d%H%M%S")
        driver.find_element_by_id("btnLast").click()
        time.sleep(3)
        driver.find_element_by_id("btnPrevious").click()
        time.sleep(3)
        # 地址页签
        driver.find_element_by_link_text("地址").click()
        v_person = driver.find_elements_by_class_name("x-grid3-hd-inner")[2]
        ActionChains(driver).context_click(v_person).perform()
        time.sleep(1)
        driver.find_element_by_id("AddBorrow").click()
        time.sleep(1)
        # 地址-新增地址窗体
        # 地址标识
        driver.find_element_by_id("TAddressName").send_keys(v_tim)
        # 街道邮箱
        driver.find_element_by_id("TStreet").send_keys(random.randint(111111, 999999))
        # 街区
        driver.find_element_by_id("TBlock").send_keys(fun_data_address())
        # 城市
        driver.find_element_by_id("TCity").send_keys(fun_data_city())
        # 邮政编码
        driver.find_element_by_id("TZipCode").send_keys(fun_data_email())
        # 县
        driver.find_element_by_id("TCounty").send_keys(fun_data_city())
        # 省份
        driver.find_element_by_id("TStateP").click()
        v_list = driver.find_elements_by_class_name("x-combo-list-item")
        v_list[random.randint(0, len(v_list)-0)].click()
        # 街道号
        driver.find_element_by_id("TStreetNo").send_keys(random.randint(111, 999))
        # 楼层号
        driver.find_element_by_id("TBuilding").send_keys(random.randint(11, 99))
        driver.find_element_by_id("Button3").click()
        time.sleep(2)
        driver.find_element_by_id("btnSave").click()
        time.sleep(4)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/test_1801_02.jpg")
                print("Error：" + i.text)
                unittest.expectedFailure("test_1801_02")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    unittest.main()
