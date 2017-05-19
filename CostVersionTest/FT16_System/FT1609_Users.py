# -*- coding: utf-8 -*-
from PubliCode.onlineClass import *


class Users(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)

    '''系统管理-用户设置-用户管理'''
    def test_1609_user_check(self):
        '''系统管理-用户设置-用户管理'''
        driver = self.driver
        ClasMenu.menu_full_text(self, "系统管理", "用户设置", "用户管理")
        driver.switch_to.frame("frame_tab_PM000003")
        v_text = driver.find_elements_by_class_name("custom_list-header-text")
        for i in v_text:
            if "用户列表" in i.text:
                print("系统管理-用户设置-用户管理页面显示正常")
            else:
                print("BUG 系统管理-用户设置-用户管理页面不显示")
                unittest.expectedFailure("test_1609_user_check")

    '''系统管理-用户设置-部门管理'''
    def test_1609_department_check(self):
        '''系统管理-用户设置-部门管理'''
        driver = self.driver
        ClasMenu.menu_full_text(self, "系统管理", "用户设置", "部门管理")
        driver.switch_to.frame("frame_tab_PM000006")
        v_text = driver.find_elements_by_class_name("custom_list-header-text")
        for i in v_text:
            if "部门列表" in i.text:
                print("系统管理-用户设置-部门列表页面显示正常")
            else:
                print("BUG 系统管理-用户设置-部门列表页面不显示")
                unittest.expectedFailure("test_1609_department_check")

    '''系统管理-用户设置-岗位列表'''
    def test_1609_job_check(self):
        '''系统管理-用户设置-岗位列表'''
        driver = self.driver
        ClasMenu.menu_full_text(self, "系统管理", "用户设置", "岗位管理")
        driver.switch_to.frame("frame_tab_PM000005")
        v_text = driver.find_elements_by_class_name("custom_list-header-text")
        for i in v_text:
            if "岗位列表" in i.text:
                print("系统管理-用户设置-岗位列表页面显示正常")
            else:
                print("BUG 系统管理-用户设置-岗位列表页面不显示")
                unittest.expectedFailure("test_1609_job_check")

    '''系统管理-用户设置-角色列表'''
    def test_1609_role_check(self):
        '''系统管理-用户设置-角色列表'''
        driver = self.driver
        ClasMenu.menu_full_text(self, "系统管理", "用户设置", "角色管理")
        driver.switch_to.frame("frame_tab_PM000004")
        v_text = driver.find_elements_by_class_name("custom_list-header-text")
        for i in v_text:
            if "角色列表" in i.text:
                print("系统管理-用户设置-角色列表页面显示正常")
            else:
                print("BUG 系统管理-用户设置-角色列表页面不显示")
                unittest.expectedFailure("test_1609_role_check")

    '''系统管理-用户设置-组列表'''
    def test_1609_group_check(self):
        '''系统管理-用户设置-角色列表'''
        driver = self.driver
        ClasMenu.menu_full_text(self, "系统管理", "用户设置", "组管理")
        driver.switch_to.frame("frame_tab_PM000123")
        v_text = driver.find_elements_by_class_name("custom_list-header-text")
        for i in v_text:
            if "组列表" in i.text:
                print("系统管理-用户设置-组列表页面显示正常")
            else:
                print("BUG 系统管理-用户设置-组列表页面不显示")
                unittest.expectedFailure("test_1609_role_check")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()

    testsuit.addTest(Menu("test_1616_Custom"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)