# -*- coding: utf-8 -*-
from PubliCode.onlineClass import *
from PubliCode.randData import *


class Archives(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "人事管理", "人员管理", "档案管理")
        # 移动到页面顶部，防止对象遮挡
        driver.switch_to.frame("frame_tab_PM000888")

    '''人事管理-人员管理-档案管理添加功能'''
    def test_0503_01_add(self):
        """人事管理-人员管理-档案管理添加功能"""
        driver = self.driver
        driver.find_element_by_id("btnAdd").click()
        time.sleep(3)
        driver.switch_to.frame("winEdit_IFrame")
        # 员工姓名
        driver.find_element_by_id("txtEmployeeName").send_keys(fun_data_name())
        # 系统用户
        driver.find_element_by_xpath("//*[@id='txtEmployeeCode_Container']/div/span").click()
        time.sleep(2)
        driver.switch_to.frame("winItem_IFrame")
        v_l_user = driver.find_elements_by_class_name("x-grid3-row")
        if len(v_l_user) > 0:
            v_l_user[0].click()
            driver.find_element_by_id("Button1").click()
        else:
            driver.find_element_by_id("Button16").click()
        time.sleep(2)
        driver.switch_to.parent_frame()
        # 招聘来源
        driver.find_element_by_id("cboRecruitmentSource").click()
        v_recruitment = driver.find_elements_by_class_name("x-combo-list-item")
        v_recruitment[random.randint(1, len(v_recruitment) - 1)].click()
        # 性别
        driver.find_element_by_id("txtGender").click()
        time.sleep(2)
        for i in driver.find_elements_by_class_name("x-combo-list-item"):
            if i.text == random.choice(['男', '女']):
                i.click()
                break
        # 身份证号码
        driver.find_element_by_id("txtIDCard").send_keys(fun_idcard())
        driver.find_element_by_id("txtWorkEmail").click()
        for i in driver.find_elements_by_class_name("ext-mb-text"):
            if "身份证格式不正确" in i.text:
                ClasForm.form_button_yes(self, "确定")
                time.sleep(1)
                break
                driver.find_element_by_id("txtIDCard").clear()
                driver.find_element_by_id("txtIDCard").send_keys(fun_idcard())
        # 婚姻状况
        driver.find_element_by_id("txtMaritalStatus").click()
        time.sleep(2)
        for i in driver.find_elements_by_class_name("x-combo-list-item"):
            if i.text == random.choice(['未婚', '已婚', '离异']):
                i.click()
                break
        # 邮箱
        driver.find_element_by_id("txtWorkEmail").send_keys(fun_data_email())
        # 紧急联系人电话
        driver.find_element_by_id("txtEmergencyPhone").click()
        driver.find_element_by_id("txtEmergencyPhone").send_keys(fun_data_mobile())
        # 手机号
        driver.find_element_by_id("txtTelephoneNumber").send_keys(fun_data_mobile())
        # 国籍
        driver.find_element_by_id("txtNationality").click()
        for i in driver.find_elements_by_class_name("x-combo-list-item"):
            if i.text == "中国":
                i.click()
                break
        # 籍贯
        driver.find_element_by_id("txtNativePlace").send_keys(fun_data_city())
        # 出生地
        driver.find_element_by_id("txtBirthPlace").send_keys(fun_data_address())
        # 户籍地址
        driver.find_element_by_id("txtPermanentAddress").send_keys(fun_data_address())
        # 政治面貌
        driver.find_element_by_id("txtPoliticalLandscape").click()
        time.sleep(2)
        for i in driver.find_elements_by_class_name("x-combo-list-item"):
            if i.text == random.choice(['中共党员', '共青团员', '民革党员', '无党派', '致公党党员']):
                i.click()
                break
        # 民族
        driver.find_element_by_id("txtEthnic").send_keys(fun_data_nation())
        # 参加工作时间
        driver.find_element_by_id("txtParticipateWorkTime").click()
        time.sleep(2)
        for i in driver.find_elements_by_class_name("x-btn-mc"):
            if i.text == "今天":
                i.click()
        # 最高学位
        driver.find_element_by_id("txtAcademicDegree").click()
        time.sleep(2)
        for i in driver.find_elements_by_class_name("x-combo-list-item"):
            if i.text == random.choice(['学士', '硕士', '博士']):
                i.click()
                break
        # 最高学历
        driver.find_element_by_id("cboEducationExperienceRecord").click()
        time.sleep(2)
        for i in driver.find_elements_by_class_name("x-combo-list-item"):
            if i.text == random.choice(['中专', '大专', '本科', '研究生']):
                i.click()
                break
        # 毕业学校
        driver.find_element_by_id("txtGraduationSchool").send_keys(fun_data_university())
        # 专业
        driver.find_element_by_id("txtProfessionals").send_keys(fun_data_specialty())
        # 资格证书
        driver.find_element_by_id("txtCredentials").send_keys(fun_data_certificate())
        # 专业技术职务
        driver.find_element_by_id("txtProfessionalTechnicalPosition").send_keys(fun_data_position())
        driver.find_element_by_id("btnSave").click()
        time.sleep(3)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "保存成功" in i.text:
                print(i.text)
            elif "请检查表单必填项" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/hr/test_0503_01_add.jpg")
                print("Error：" + i.text)
                unittest.expectedFailure("test_0503_01_add")

    '''人事管理-人员管理-档案管理更新'''
    def test_0503_02_update(self):
        """人事管理-人员管理-档案管理添加功能"""
        driver = self.driver
        v_spans = driver.find_elements_by_tag_name("span")
        for i in v_spans:
            if i.text == "详细":
                i.click()
                break
        time.sleep(3)
        driver.switch_to.frame("winEdit_IFrame")

        driver.find_element_by_id("btnSave").click()
        time.sleep(3)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "保存成功" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/hr/test_0503_02_update.jpg")
                print("Error：" + i.text)
                unittest.expectedFailure("test_0503_02_update")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(Archives("test_0503_01_add"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)