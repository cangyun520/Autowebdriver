# encoding:utf-8
from PubliCode.config import *
from PubliCode.PubMobile import *
from PubliCode.randData import *
from appium import webdriver


class CustomerManage(unittest.TestCase):
    def setUp(self):
        # 调用钉钉初始化公共方法
        desired_caps = DingPublic.start_ding(self)
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(25)
        try:
            self.driver.find_element_by_name("工作").click()
        except Exception as err:
            print(err)

    """钉钉-业务管理首页-页面检查"""
    def test_0101_01_check(self):
        """钉钉-业务管理首页-页面检查"""
        driver = self.driver
        # driver.find_element_by_name("联系人").click()
        # try:
        #     driver.find_element_by_name("工作").click()
        # except Exception as err:
        #     print(err)

        driver.find_element_by_name("业务管理首页").click()
        time.sleep(5)

        v_an = driver.find_elements_by_class_name("android.view.View")
        # for i in v_an:
        #     print(i.id)
        v_an[3].click()
        time.sleep(3)

        # 进入到客户管理页面
        try:
            driver.find_element_by_name("客户管理").is_displayed()
        except Exception as err:
            print(err)
            driver.get_screenshot_as_file(root_path() + "TestPicture/Ding/test_0101_01_check.jpg")
            unittest.expectedFailure("test_0101_01_check")

    """钉钉-业务管理首页-客户管理添加"""

    def test_0101_02_CustomerAdd(self):
        """钉钉-业务管理首页-客户管理添加"""
        driver = self.driver
        # driver.find_element_by_name("联系人").click()
        # try:
        #     driver.find_element_by_name("工作").click()
        # except Exception as err:
        #     print(err)

        driver.find_element_by_name("业务管理首页").click()
        time.sleep(5)
        v_tim = time.strftime("%y%m%d%H%M%S")
        v_an = driver.find_elements_by_class_name("android.view.View")
        v_an[3].click()
        time.sleep(3)
        driver.find_element_by_accessibility_id(" Link").click()

        # 进入添加页面

        driver.find_element_by_accessibility_id("代码*").click()
        v_num = "KHDD" + str(random.randint(11111, 99999))
        driver.find_element_by_accessibility_id("代码*").send_keys(v_num)
        driver.find_element_by_accessibility_id("名称").click()
        driver.find_element_by_accessibility_id("名称").send_keys("客户DD" + v_tim + "有限公司")
        driver.find_element_by_accessibility_id("外文名称").send_keys(fun_data_englishname())
        driver.find_element_by_accessibility_id("电话").send_keys("027-" + str(random.randint(111111, 999999)))
        driver.find_element_by_accessibility_id("移动电话").send_keys(fun_data_mobile())
        driver.find_element_by_accessibility_id("传真").send_keys("027-" + str(random.randint(111111, 999999)))
        driver.find_element_by_accessibility_id("电子邮件").send_keys(fun_data_email())
        driver.find_element_by_accessibility_id("Web站点").send_keys(fun_data_www())
        # 上下滑动屏幕
        driver.swipe(0, 0, 0, 100)
        time.sleep(1)
        driver.find_element_by_accessibility_id("备注").send_keys("Python应用于钉钉端自动添加数据" + v_tim)
        driver.find_element_by_accessibility_id("添加 Link").click()
        time.sleep(8)

        # e 检测对象是否存在
        v_tip = "保存成功，单号：" + v_num
        try:
            driver.find_element_by_accessibility_id(v_tip).is_displayed()
            print(v_tip)
        except Exception as err:
            print(err)
            driver.get_screenshot_as_file(root_path() + "TestPicture/Ding/test_0101_02_CustomerAdd.jpg")
            unittest.expectedFailure("test_0101_02_Customer")

    """钉钉-业务管理首页-供应商添加"""

    def test_0101_03_SupplierAdd(self):
        """钉钉-业务管理首页-供应商添加"""
        driver = self.driver
        driver.find_element_by_name("业务管理首页").click()
        time.sleep(5)
        v_tim = time.strftime("%y%m%d%H%M%S")
        v_an = driver.find_elements_by_class_name("android.view.View")
        v_an[4].click()
        time.sleep(3)
        driver.find_element_by_accessibility_id(" Link").click()

        # 进入添加页面

        driver.find_element_by_accessibility_id("代码*").click()
        v_num = "VD" + str(random.randint(11111, 99999))
        driver.find_element_by_accessibility_id("代码*").send_keys(v_num)
        driver.find_element_by_accessibility_id("名称").click()
        driver.find_element_by_accessibility_id("名称").send_keys("供应商DD" + v_tim + "有限公司")
        driver.find_element_by_accessibility_id("外文名称").send_keys(fun_data_englishname())
        driver.find_element_by_accessibility_id("电话").send_keys("017-" + str(random.randint(111111, 999999)))
        driver.find_element_by_accessibility_id("移动电话").send_keys(fun_data_mobile())
        driver.find_element_by_accessibility_id("传真").send_keys("017-" + str(random.randint(111111, 999999)))
        driver.find_element_by_accessibility_id("电子邮件").send_keys(fun_data_email())
        driver.find_element_by_accessibility_id("Web站点").send_keys(fun_data_www())
        # 上下滑动屏幕
        driver.swipe(0, 0, 0, 100)
        driver.find_element_by_accessibility_id("备注").click()
        time.sleep(1)
        driver.find_element_by_accessibility_id("备注").send_keys("Python应用于钉钉端自动添加供应商数据" + v_tim)
        driver.find_element_by_accessibility_id("添加 Link").click()
        time.sleep(8)

        # e 检测对象是否存在
        v_tip = "保存成功，单号：" + v_num
        try:
            driver.find_element_by_accessibility_id(v_tip).is_displayed()
            print(v_tip)
        except Exception as err:
            print(err)
            driver.get_screenshot_as_file(root_path() + "TestPicture/Ding/test_0101_03_SupplierAdd.jpg")
            unittest.expectedFailure("test_0101_03_SupplierAdd")

    """钉钉-业务管理首页-库存查询检查"""

    def test_0101_04_InventoryLook(self):
        """钉钉-业务管理首页-库存查询检查"""
        driver = self.driver
        driver.find_element_by_name("业务管理首页").click()
        time.sleep(5)
        v_an = driver.find_elements_by_class_name("android.view.View")
        v_an[5].click()
        time.sleep(3)

        # 进入查看页面

        try:
            driver.find_element_by_name("库存查询").is_displayed()
        except Exception as err:
            print(err)
            driver.get_screenshot_as_file(root_path() + "TestPicture/Ding/test_0101_04_InventoryLook.jpg")
            unittest.expectedFailure("test_0101_04_InventoryLook")

        v_list = driver.find_elements_by_class_name("android.view.View")
        v_list[1].click()
        time.sleep(5)
        # 进入物料查看详情页面

        try:
            driver.find_element_by_accessibility_id(" 返回").is_displayed()
        except Exception as err:
            print(err)
            driver.get_screenshot_as_file(root_path() + "TestPicture/Ding/test_0101_04_InventoryLook.jpg")
            unittest.expectedFailure("test_0101_04_InventoryLook")

    """钉钉-业务管理首页-销售报价单添加"""

    def test_0101_05_SalesOfferAdd(self):
        """钉钉-业务管理首页-销售报价单添加"""
        driver = self.driver
        driver.find_element_by_name("业务管理首页").click()
        time.sleep(5)
        v_tim = time.strftime("%y%m%d%H%M%S")
        v_an = driver.find_elements_by_class_name("android.view.View")
        v_an[6].click()
        time.sleep(5)
        driver.find_element_by_accessibility_id(" Link").click()

        # 进入添加页面
        driver.find_element_by_accessibility_id("客户名称* Link").click()
        time.sleep(2)
        # 进入业务伙伴选择页面
        v_list = driver.find_elements_by_class_name("android.view.View")
        v_list[1].click()
        time.sleep(1)
        driver.find_element_by_accessibility_id("确定 Link").click()
        time.sleep(2)

        driver.find_element_by_accessibility_id("物料明细* Link").click()
        time.sleep(2)
        # 进入物料选择页面
        v_list_wl = driver.find_elements_by_class_name("android.view.View")
        v_list_wl[1].click()
        driver.find_element_by_accessibility_id("提交 Link").click()
        time.sleep(1)
        driver.find_element_by_accessibility_id("添加物料明细项 Link").click()
        v_list_wl[2].click()
        driver.find_element_by_accessibility_id("提交 Link").click()
        time.sleep(1)
        driver.find_element_by_accessibility_id(" 返回 Link").click()
        time.sleep(1)

        # 上下滑动屏幕
        driver.find_element_by_accessibility_id("备注").send_keys("Python应用于钉钉端自动添加销售报价单" + v_tim)
        driver.swipe(0, 0, 0, 100)
        driver.find_element_by_accessibility_id("添加 Link").click()
        time.sleep(6)

        # e 检测对象是否存在
        v_tip = "保存成功"
        try:
            driver.find_element_by_accessibility_id(v_tip).is_displayed()
            print(v_tip)
        except Exception as err:
            print(err)
            driver.get_screenshot_as_file(root_path() + "TestPicture/Ding/test_0101_05_SalesOfferAdd.jpg")
            unittest.expectedFailure("test_0101_05_SalesOfferAdd")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

