# -*- coding: utf-8 -*-
from PubliCode.onlineClass import *
from PubliCode.randData import *


class CarsArchives(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "行政办公", "车辆管理", "车辆档案")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000802")

    # 行政办公-车辆管理-车辆档案添加功能
    def test_0401_01_add(self):
        """行政办公-车辆管理-车辆档案添加功能"""
        driver = self.driver
        driver.find_element_by_id("btnAdd").click()
        time.sleep(2)
        v_tim = time.strftime("%y%m%d%H%M")
        # 车牌号
        v_chr = chr(random.randint(97, 122))
        driver.find_element_by_id("txtPlateNumber").send_keys("鄂AU"+v_chr.upper()+str(random.randint(100, 999)))
        time.sleep(1)
        # 名称
        with open(root_path() + 'PubliData/carName.txt', 'r') as v_carFile:
            v_lines = v_carFile.readlines()
            # print(len(v_lines))
        v_car = v_lines[random.randint(0, len(v_lines)-1)]
        driver.find_element_by_id("txtName").send_keys(v_car)
        # 座位数
        driver.find_element_by_id("numSeats").send_keys(random.randint(1, 7))
        # 购买时间
        driver.find_element_by_id("dtBuyTime").click()
        time.sleep(1)
        for i in driver.find_elements_by_class_name("x-btn-mc"):
            # print(i.text)
            if "今天" in i.text:
                i.click()
        # 购买金额
        driver.find_element_by_id("numAmount").send_keys(random.randint(200000, 800000))
        # 备注
        driver.find_element_by_id("txtRemark").send_keys("豪车一辆，这是测试说的Auto。登记日期：" + v_tim)
        driver.find_element_by_id("btnSave").click()
        time.sleep(3)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功" in i.text:
                print(i.text)
            elif "该车辆选择时间段内已被申请" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + "TestPicture/oa/test_0401_01_add.jpg")
                print("Error：" + i.text)
                unittest.expectedFailure("test_0401_01_add")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(CarsArchives("test_0401_01_add"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)