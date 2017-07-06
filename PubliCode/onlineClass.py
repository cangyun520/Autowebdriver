from PubliCode.randData import *
from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class ClasLogin:
    """初始测试准备工作"""
    def __login_url(self):
        # 环境URL地址
        driver = self.driver
        f = open(root_path() + 'PubliData/config/url.txt', 'r')
        v_url = f.readline()
        f.close()
        driver.maximize_window()
        driver.get(v_url)
        forget_pasd = driver.find_element_by_partial_link_text("忘记密码")
        if forget_pasd.is_displayed():
            driver.get(v_url)
        time.sleep(2)

    def __login_user(self, uname):
        """用户登录"""
        log_file = open(root_path() + 'PubliData/LogName.txt', 'r')

        # 读取所有行数据，并匹配当前登陆用户
        for i in log_file.readlines():
            try:
                uname in i
                break
            except Exception as err:
                print(err)

        driver = self.driver
        password = 123456
        driver.find_element_by_id("user_login").clear()
        driver.find_element_by_id("user_login").send_keys(uname)
        driver.find_element_by_id("user_pass").clear()
        driver.find_element_by_id("user_pass").send_keys(password)
        driver.find_element_by_id("btn_Login").click()
        time.sleep(3)
        if driver.find_element_by_id("tab_home").is_displayed():
            driver.find_element_by_id("tab_home").click()
        else:
            driver.refresh()
            time.sleep(2)

    def login_setup(self):
        # 设置页面上隐形的智能等待时间30秒
        self.driver.implicitly_wait(20)
        # 定义空verificationErrors数组，脚本运行错误信息被记录到整个数组中
        self.verificationErrors = []
        # 是否接受下一个警告，默认为是
        self.accept_next_alert = True
        driver = self.driver
        time.sleep(1)
        # 打开菜单
        ClasLogin.__login_url(self)
        # 用户登录
        ClasLogin.__login_user(self, "admin")

    def login_setup_fq(self):
        # 设置页面上隐形的等待时间30秒
        self.driver.implicitly_wait(30)
        # 定义空verificationErrors数组，脚本运行错误信息被记录到整个数组中
        self.verificationErrors = []
        # 是否接受下一个警告，默认为是
        self.accept_next_alert = True
        driver = self.driver
        # 打开菜单
        ClasLogin.__login_url(self)
        # 用户登录
        ClasLogin.__login_user(self, "fq01")

    def login_setup_bear(self):
        # 设置页面上隐形的等待时间30秒
        self.driver.implicitly_wait(30)
        # 定义空verificationErrors数组，脚本运行错误信息被记录到整个数组中
        self.verificationErrors = []
        # 是否接受下一个警告，默认为是
        self.accept_next_alert = True
        driver = self.driver
        # 打开菜单
        ClasLogin.__login_url(self)
        # 用户登录
        ClasLogin.__login_user(self, "bear")

    def login_setup_admin(self):
        # 设置页面上隐形的等待时间30秒
        self.driver.implicitly_wait(30)
        # 定义空verificationErrors数组，脚本运行错误信息被记录到整个数组中
        self.verificationErrors = []
        # 是否接受下一个警告，默认为是
        self.accept_next_alert = True
        driver = self.driver
        # 打开菜单
        ClasLogin.__login_url(self)
        # 用户登录
        ClasLogin.__login_user(self, "admin")

    def login_setup_arvin(self):
        # 设置页面上隐形的等待时间30秒
        self.driver.implicitly_wait(30)
        # 定义空verificationErrors数组，脚本运行错误信息被记录到整个数组中
        self.verificationErrors = []
        # 是否接受下一个警告，默认为是
        self.accept_next_alert = True
        driver = self.driver
        # 打开菜单
        ClasLogin.__login_url(self)
        # 用户登录
        ClasLogin.__login_user(self, "arvin")

    def login_setup_sp01(self):
        # 设置页面上隐形的等待时间30秒
        self.driver.implicitly_wait(30)
        # 定义空verificationErrors数组，脚本运行错误信息被记录到整个数组中
        self.verificationErrors = []
        # 是否接受下一个警告，默认为是
        self.accept_next_alert = True
        driver = self.driver
        # 打开菜单
        ClasLogin.__login_url(self)
        # 用户登录
        ClasLogin.__login_user(self, "sp01")


class ClasMenu:
    """打开菜单连接"""
    def menu_full_text(self, *v_menu):
        # 全名称菜单
        if v_menu != "":
            for i in v_menu:
                self.driver.find_element_by_link_text(i).click()
                time.sleep(1)
        else:
            pass
        time.sleep(3)

    def menu_part_text(self, *v_menu):
        # 关键字名称菜单
        if v_menu != "":
            for i in v_menu:
                self.driver.find_element_by_partial_link_text(i).click()
                time.sleep(1)
        else:
            pass
        time.sleep(3)


class ClasForm:
    """处理表单内部特殊字段数据"""
    def form_top(self, number):
        # js移动到页面顶部，防止对象遮挡
        js_top = "window.scrollTo(0," + str(number) + ")"
        self.driver.execute_script(js_top)

    '''表头弹出时间控件选择【今天】'''
    def form_today(self, uid):
        # 选择当天日期
        self.driver.find_element_by_id(uid).click()
        for i in self.driver.find_elements_by_tag_name("button"):
            if i.text == "今天":
                i.click()
                break
        time.sleep(1)

    '''行弹出时间控件选择【今天】'''
    def form_today_line(self, uid):
        # 选择当天日期
        self.driver.find_element_by_id(uid).click()
        for i in self.driver.find_elements_by_tag_name("button"):
            if i.text == "今天":
                i.click()
                break

    '''弹出时间控件任意选择N月以后的某一天'''
    def form_today_next(self, number, uid, nextmonth, today):
        self.driver.find_element_by_id(uid).click()
        v_month = self.driver.find_elements_by_class_name("x-date-right")
        v_n = 0
        while v_n < nextmonth:
            v_month[number-1].click()
            v_n += 1
        v_day = self.driver.find_elements_by_class_name("x-date-active")
        if today <= 0 or today > 31:
            today = "24"
        for i in v_day:
            if i.text == str(today):
                i.click()
                break

    '''页面自定义字段隐藏'''
    def form_field_hide(self):
        # 隐藏自定义字段
        driver = self.driver
        if driver.find_element_by_id("panelColumn").is_displayed():
            driver.find_element_by_xpath("//*[@id='panelColumn']/div/div").click()
            time.sleep(1)
        else:
            pass

    '''根据名称点击页面按钮'''
    def form_button_yes(self, v_str):
        v_tip_t = self.driver.find_elements_by_class_name("x-window-header-text")
        for i in v_tip_t:
            if "提示" in i.text:
                for ii in self.driver.find_elements_by_tag_name("button"):
                    if ii.text == v_str:
                        ii.click()
                        break
        time.sleep(2)

    '''检查窗体是否一直处于加载中卡死'''
    def form_loading(self, testcase):
        v_load = self.driver.find_elements_by_class_name("x-mask-loading")
        for i in v_load:
            if "数据加载中" in i.text:
                print("复制从窗体界面一直处于加载中，导致页面假死，请检查！")
                unittest.expectedFailure(testcase)


class ClasFlow:
    """处理单据固定流，自由流操作"""
    def flow_free(self, usernam):
        # 自由流处理
        try:
            self.driver.find_element_by_id("btnSelectAppover").is_displayed()
            self.driver.find_element_by_id("btnSelectAppover").click()
            time.sleep(3)
            self.driver.switch_to_frame("winSelectUser_IFrame")  # 切换到用户信息选择窗体
            self.driver.find_element_by_id("txtUserName").send_keys(usernam)
            self.driver.find_element_by_id("btnQuery").click()
            time.sleep(2)
            self.driver.find_element_by_class_name("x-grid3-row-table").click()
            self.driver.find_element_by_id("btnConfirm").click()
            time.sleep(2)
            self.driver.switch_to.parent_frame()
        except:
            pass

    def flow_free_icon(self, usernam):
        self.driver.find_element_by_id("userphoto").click()
        time.sleep(3)
        for i in self.driver.find_elements_by_tag_name("td"):
            if i.text == usernam:
                i.click()
        time.sleep(1)
        self.driver.find_element_by_id("btnUserOK").click()
        time.sleep(2)


class ClasPopupWindow:
    """表头弹出窗体数据选择"""

    def popup_project(self):
        # 项目弹出窗体数据选择
        driver = self.driver
        driver.find_element_by_xpath("//*[@id='ProjectCode_Container']/div/span").click()
        time.sleep(3)
        driver.switch_to_frame("winAdd_IFrame")
        v_projectlist = driver.find_elements_by_class_name("x-grid3-row")
        v_projectlist[random.randint(0, (len(v_projectlist) - 1))].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(1)
        driver.switch_to.parent_frame()
