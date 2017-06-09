# -*- coding: utf-8 -*-
from PubliCode.config import *
from PubliCode.onlineClass import *
from PubliCode.randData import *
'''
    *   Arvin
    *   2017-01-13
'''


class CarsApply(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "行政办公", "车辆管理", "车辆申请")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000803")

    '''行政办公-车辆管理-车辆申请添加'''
    def test_0402_02_add(self):
        """行政办公-车辆管理-车辆申请添加功能"""
        driver = self.driver
        driver.find_element_by_id("btnApply").click()
        time.sleep(3)
        v_tim = time.strftime("%y%m%d%H%M")
        # 切换到新增页面
        driver.switch_to.frame("winActivity_IFrame")
        # 用车人
        driver.find_element_by_xpath("//*[@id='trigfiApplyPerson_Container']/div/span/img[2]").click()
        time.sleep(3)

        # 切换到用户选择页面
        driver.switch_to.frame("winSelectUser_IFrame")
        driver.find_elements_by_class_name("x-grid3-row")[random.randint(1, 10)].click()
        driver.find_element_by_id("btnConfirm").click()
        time.sleep(1)
        # driver.switch_to.frame("frame_tab_PM000803")
        driver.switch_to.parent_frame()

        # 车牌号
        driver.find_element_by_xpath("//*[@id='trgPlateNumber_Container']/div/span/img[2]").click()
        time.sleep(3)
        driver.switch_to.frame("winSelectTraffic_IFrame")      # 切换到车辆选择页面
        v_car = driver.find_elements_by_class_name("x-grid3-row")
        v_car[random.randint(0, len(v_car) - 1)].click()
        driver.find_element_by_id("btnConfirm").click()
        time.sleep(1)
        driver.switch_to.parent_frame()
        # 随行人员
        driver.find_element_by_xpath("//*[@id='trgEntourageName_Container']/div/span/img[2]").click()
        time.sleep(3)
        # 切换到用户选择页面
        driver.switch_to.frame("winSelectUser_IFrame")
        driver.find_elements_by_class_name("x-grid3-row")[random.randint(1, 10)].click()
        driver.find_element_by_id("btnConfirm").click()
        time.sleep(1)
        driver.switch_to.parent_frame()
        # 目的地
        end_address = random.choice([
            '黄石', '鄂州', '孝感', '长沙', '岳阳', '信阳', '成都', '郑州', '南昌', '黄冈', '宜昌', '合肥'])
        driver.find_element_by_id("txtDestination").send_keys(end_address)
        # 申请里程
        driver.find_element_by_id("txtMileageNum").send_keys(random.randint(1, 500))
        # 事由
        driver.find_element_by_id("txtReasons").send_keys("世界那么大我想带着车车去看看，测试说的Auto")
        # 备注
        driver.find_element_by_id("txtApplyRemark").send_keys("这是一次愉快的互联网约车，测试说的Auto。申请时间：" + v_tim)
        # 调用自由流审批人选择函数
        ClasFlow.flow_free(self, "bear")
        driver.find_element_by_id("btnWorkflow").click()
        time.sleep(3)
        # 单据添加后断言
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "流程已触发" in i.text:
                print(i.text)
            elif "时间段内已被申请" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/oa/test_0402_02_add.jpg")
                print("Error：" + i.text)
                unittest.expectedFailure("test_0402_02_add")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(CarsApply("test_0402_02_add"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)