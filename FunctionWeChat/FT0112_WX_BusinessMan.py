# encoWX:utf-8
from PubliCode.dingTalkClass import *


class BusinessMan(unittest.TestCase):
    def setUp(self):
        # 调用微信初始化公共方法
        desired_caps = WeChatPublic.start_weixin(self)
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(25)

        try:
            self.driver.find_element_by_name("OnlineBox产品").click()
        except Exception as err:
            print(err)
        self.driver.find_element_by_name("业务管理").click()
        timesl(5)
        # 全局变量
        global v_tim
        v_tim = time.strftime("%Y-%m-%d %H:%M:%S")

    """客户管理-页面检查"""
    def test_0112_01_customerAdd(self):
        """客户管理-页面检查"""
        driver = self.driver

        # 屏幕像素
        # driver.tap([(100, 300)])
        driver.find_element_by_accessibility_id("客户管理 Link").click()
        timesl(3)
        driver.find_element_by_accessibility_id(" Link").click()
        timesl(2)
        # driver.find_element_by_id("ajp").click()

        # 进入添加页面
        driver.find_element_by_accessibility_id("代码*").click()
        v_num = "KHDD" + str(random.randint(11111, 99999))
        driver.find_element_by_accessibility_id("代码*").send_keys(v_num)
        driver.find_element_by_accessibility_id("名称").click()
        driver.find_element_by_accessibility_id("名称").send_keys("客户WX" + v_tim + "有限公司")
        driver.find_element_by_accessibility_id("外文名称").send_keys(fun_data_englishname())
        driver.find_element_by_accessibility_id("电话").send_keys("027-" + str(random.randint(111111, 999999)))
        driver.find_element_by_accessibility_id("移动电话").send_keys(fun_data_mobile())
        driver.find_element_by_accessibility_id("传真").send_keys("027-" + str(random.randint(111111, 999999)))
        driver.find_element_by_accessibility_id("电子邮件").send_keys(fun_data_email())
        driver.find_element_by_accessibility_id("Web站点").send_keys(fun_data_www())
        # 上下滑动屏幕
        driver.swipe(0, 0, 0, 100, 500)
        time.sleep(1)
        driver.find_element_by_accessibility_id("备注").send_keys("Python应用于微信端自动添加数据" + v_tim)

        driver.find_element_by_accessibility_id("添加 Link").click()
        time.sleep(8)

        # e 检测对象是否存在
        v_tip = "保存成功，单号：" + v_num
        try:
            driver.find_element_by_accessibility_id(v_tip).is_displayed()
            print(v_tip)
        except Exception as err:
            print(err)
            driver.get_screenshot_as_file(root_path() + "TestPicture/WX/test_0112_01_customerAdd.jpg")
            unittest.expectedFailure("test_0101_02_Customer")

    """客户管理-供应商添加"""
    def test_0101_02_supplierAdd(self):
        """客户管理-供应商添加"""
        driver = self.driver

        driver.tap([(250, 200)])
        # driver.find_element_by_accessibility_id(" 供应商管理 Link").click()
        time.sleep(3)
        driver.find_element_by_accessibility_id(" Link").click()
        timesl(2)

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
        driver.swipe(0, 0, 0, 100, 500)
        driver.find_element_by_accessibility_id("备注").click()
        time.sleep(1)
        driver.find_element_by_accessibility_id("备注").send_keys("Python应用于微信端自动添加供应商数据" + v_tim)
        driver.find_element_by_accessibility_id("添加 Link").click()
        time.sleep(8)

        # e 检测对象是否存在
        v_tip = "保存成功，单号：" + v_num
        try:
            driver.find_element_by_accessibility_id(v_tip).is_displayed()
            print(v_tip)
        except Exception as err:
            print(err)
            driver.get_screenshot_as_file(root_path() + "TestPicture/WX/test_0101_02_supplierAdd.jpg")
            unittest.expectedFailure("test_0101_02_supplierAdd")

    """客户管理-库存查询检查"""
    def test_0101_03_InventoryLook(self):
        """客户管理-库存查询检查"""
        driver = self.driver

        driver.tap([(500, 200)])
        # driver.find_element_by_accessibility_id(" 库存查询 Link").click()
        time.sleep(3)

        # 进入查看页面

        try:
            driver.find_element_by_name("库存查询").is_displayed()
        except Exception as err:
            print(err)
            driver.get_screenshot_as_file(root_path() + "TestPicture/WX/test_0101_03_InventoryLook.jpg")
            unittest.expectedFailure("test_0101_03_InventoryLook")

        v_list = driver.find_elements_by_class_name("android.view.View")
        v_list[1].click()
        time.sleep(5)
        # 进入物料查看详情页面

        try:
            driver.find_element_by_accessibility_id(" 返回").is_displayed()
        except Exception as err:
            print(err)
            driver.get_screenshot_as_file(root_path() + "TestPicture/WX/test_0101_03_InventoryLook.jpg")
            unittest.expectedFailure("test_0101_03_InventoryLook")

    """客户管理-销售订单状态"""
    def test_0101_04_SalesOrderStatus(self):
        """客户管理-销售订单状态"""
        driver = self.driver

        driver.tap([(100, 650)])
        time.sleep(3)

        # 进入查看页面

        try:
            driver.find_element_by_name("销售订单状态").is_displayed()
        except Exception as err:
            print(err)
            driver.get_screenshot_as_file(root_path() + "TestPicture/WX/test_0101_04_SalesOrderStatus.jpg")
            unittest.expectedFailure("test_0101_04_SalesOrderStatus")

        v_list = driver.find_elements_by_class_name("android.view.View")
        v_list[1].click()
        time.sleep(5)
        # 进入订单查看详情页面

        try:
            driver.find_element_by_accessibility_id(" 返回 Link").is_displayed()
        except Exception as err:
            print(err)
            driver.get_screenshot_as_file(root_path() + "TestPicture/WX/test_0101_04_SalesOrderStatus.jpg")
            unittest.expectedFailure("test_0101_04_SalesOrderStatus")

    """客户管理-订单预警"""
    def test_0101_05_OrderWarning(self):
        """客户管理-订单预警"""
        driver = self.driver

        driver.tap([(300, 650)])
        time.sleep(3)

        # 进入查看页面

        try:
            driver.find_element_by_name("订单预警").is_displayed()
        except Exception as err:
            print(err)
            driver.get_screenshot_as_file(root_path() + "TestPicture/WX/test_0101_05_OrderWarning.jpg")
            unittest.expectedFailure("test_0101_05_OrderWarning")

        v_list = driver.find_elements_by_class_name("android.view.View")
        v_list[1].click()
        time.sleep(5)
        # 进入订单查看详情页面

        try:
            driver.find_element_by_name("订单预警").is_displayed()
        except Exception as err:
            print(err)
            driver.get_screenshot_as_file(root_path() + "TestPicture/WX/test_0101_05_OrderWarning.jpg")
            unittest.expectedFailure("test_0101_05_OrderWarning")

    """客户管理-采购订单状态"""
    def test_0101_06_PurchaseOrderStatu(self):
        """客户管理-采购订单状态"""
        driver = self.driver

        driver.tap([(500, 650)])
        time.sleep(3)

        # 进入查看页面

        try:
            driver.find_element_by_name("采购订单状态").is_displayed()
        except Exception as err:
            print(err)
            driver.get_screenshot_as_file(root_path() + "TestPicture/WX/test_0101_06_PurchaseOrderStatu.jpg")
            unittest.expectedFailure("test_0101_06_PurchaseOrderStatu")

        v_list = driver.find_elements_by_class_name("android.view.View")
        v_list[1].click()
        time.sleep(5)
        # 进入订单查看详情页面

        try:
            driver.find_element_by_accessibility_id(" 返回 Link").is_displayed()
        except Exception as err:
            print(err)
            driver.get_screenshot_as_file(root_path() + "TestPicture/WX/test_0101_06_PurchaseOrderStatu.jpg")
            unittest.expectedFailure("test_0101_06_PurchaseOrderStatu")

    """客户管理-采购到货跟踪"""
    def test_0101_07_PurchaseTrack(self):
        """客户管理-采购到货跟踪"""
        driver = self.driver

        driver.tap([(100, 850)])
        time.sleep(3)

        # 进入查看页面

        try:
            driver.find_element_by_name("采购到货跟踪").is_displayed()
        except Exception as err:
            print(err)
            driver.get_screenshot_as_file(root_path() + "TestPicture/WX/test_0101_PurchaseTrack.jpg")
            unittest.expectedFailure("test_0101_PurchaseTrack")

        v_list = driver.find_elements_by_class_name("android.view.View")
        v_list[1].click()
        time.sleep(5)
        # 进入订单查看详情页面

        try:
            driver.find_element_by_accessibility_id(" 返回 Link").is_displayed()
        except Exception as err:
            print(err)
            driver.get_screenshot_as_file(root_path() + "TestPicture/WX/test_0101_PurchaseTrack.jpg")
            unittest.expectedFailure("test_0101_PurchaseTrack")

    """客户管理-进度跟踪"""

    def test_0101_08_ProgressTrack(self):
        """客户管理-进度跟踪"""
        driver = self.driver

        driver.tap([(250, 850)])
        time.sleep(3)

        # 进入查看页面

        try:
            driver.find_element_by_name("进度跟踪").is_displayed()
        except Exception as err:
            print(err)
            driver.get_screenshot_as_file(root_path() + "TestPicture/WX/test_0101_08_ProgressTrack.jpg")
            unittest.expectedFailure("test_0101_08_ProgressTrack")

    """客户管理-移动审批"""

    def test_0101_09_MobileApproval(self):
        """客户管理-移动审批"""
        driver = self.driver

        driver.tap([(500, 850)])
        time.sleep(3)

        # 进入查看页面

        try:
            driver.find_element_by_name("移动审批").is_displayed()
        except Exception as err:
            print(err)
            driver.get_screenshot_as_file(root_path() + "TestPicture/WX/test_0101_09_MobileApproval.jpg")
            unittest.expectedFailure("test_0101_09_MobileApproval")

    """客户管理-销售订单添加"""
    # def test_0101_08_SalesOrderAdd(self):
    #     """客户管理-销售订单添加"""
    #     driver = self.driver
    #
    #     driver.tap([(250, 400)])
    #     time.sleep(5)
    #     driver.find_element_by_accessibility_id(" Link").click()
    #     time.sleep(2)
    #
    #     # 进入添加页面
    #     driver.find_element_by_accessibility_id("客户名称* Link").click()
    #     time.sleep(2)
    #     # 进入业务伙伴选择页面
    #     # x = driver.get_window_size()['width']
    #     # y = driver.get_window_size()['height']
    #     # print(x, y)
    #     # 720 1280
    #
    #     v_list = driver.find_elements_by_class_name("android.view.View")
    #     v_list[1].click()
    #     driver.find_element_by_id("common_webview").click()
    #
    #     driver.tap([(1350, 200)])
    #     # driver.find_element_by_accessibility_id("确定 Link").click()
    #     time.sleep(2)
    #
    #     driver.find_element_by_accessibility_id("物料明细* Link").click()
    #     time.sleep(2)
    #     # 进入物料选择页面
    #     v_list_wl = driver.find_elements_by_class_name("android.view.View")
    #     v_list_wl[1].click()
    #     driver.find_element_by_accessibility_id("提交 Link").click()
    #     time.sleep(1)
    #     driver.find_element_by_accessibility_id("添加物料明细项 Link").click()
    #     v_list_wl[2].click()
    #     driver.find_element_by_accessibility_id("提交 Link").click()
    #     time.sleep(1)
    #     driver.find_element_by_accessibility_id(" 返回 Link").click()
    #     time.sleep(1)
    #
    #     # 上下滑动屏幕
    #     driver.find_element_by_accessibility_id("备注").send_keys("Python应用于微信端自动添加销售报价单" + v_tim)
    #     driver.swipe(0, 0, 0, 100)
    #     driver.find_element_by_accessibility_id("添加 Link").click()
    #     time.sleep(6)
    #
    #     # e 检测对象是否存在
    #     v_tip = "保存成功"
    #     try:
    #         driver.find_element_by_accessibility_id(v_tip).is_displayed()
    #         print(v_tip)
    #     except Exception as err:
    #         print(err)
    #         driver.get_screenshot_as_file(root_path() + "TestPicture/WX/test_0101_04_SalesOfferAdd.jpg")
    #         unittest.expectedFailure("test_0101_04_SalesOfferAdd")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
