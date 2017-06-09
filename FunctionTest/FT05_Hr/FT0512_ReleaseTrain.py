# -*- coding: utf-8 -*-
from PubliCode.config import *
from PubliCode.onlineClass import *
from PubliCode.randData import *


class ReleaseTrain(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self,"人事管理", "培训管理", "指定培训", "发布培训")
        # 移动到页面顶部，防止对象遮挡
        time.sleep(3)
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM001053")

    """人事管理-培训管理-发布培训添加"""
    def test_0512_01(self):
        """人事管理-培训管理-发布培训数据添加"""
        driver = self.driver
        v_tim = time.strftime("%Y%m%d %H:%M")
        # 培训主题
        driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div/div/div/div/form/div[1]/div[1]/div[1]/div/div/input"
        ).send_keys(v_tim + "这是一次内部技能培训")
        # 培训讲师
        driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div/div/div/div/form/div[1]/div[1]/div[2]/div/div/div/span"
        ).click()
        time.sleep(5)
        driver.find_element_by_xpath(
            "//*[@id='modalTrainer']/div/div/div[2]/div[1]/div/div/form/div/div/div[1]/div/div/input"
        ).send_keys("ar")
        ClasForm.form_button_yes(self, "查询")
        driver.find_element_by_id("trainerdatatable").click()
        driver.find_element_by_xpath(
            "//*[@id='modalTrainer']/div/div/div[3]/button[1]"
        ).click()
        time.sleep(2)
        # 活动开始时间
        driver.find_element_by_id("BeginTime").click()
        time.sleep(2)
        v_day = driver.find_elements_by_class_name("day")
        v_day[5].click()
        # v_nday = time.strftime("%d")
        v_t = 0
        # for i in v_day:
        #     v_t += 1                                                            # 统计当前日期是第几个数字
        #     if i.text == v_nday:
        #         i.click()
        #         time.sleep(1)
        #         break
        v_hour = driver.find_elements_by_class_name("hour")
        v_nhour = time.strftime("%H" + ":00")
        for i in v_hour:
            if i.text == v_nhour:
                i.click()
                time.sleep(1)
                break
        driver.find_elements_by_class_name("minute")[0].click()
        # 活动结束时间
        driver.find_element_by_id("EndTime").click()
        time.sleep(2)
        v_day = driver.find_elements_by_class_name("day")
        v_day[v_t + 42].click()
        v_hour = driver.find_elements_by_class_name("hour")
        v_hour[33].click()
        driver.find_elements_by_class_name("minute")[12].click()
        # 指定培训人员
        driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div/div/div/div/form/div[1]/div[3]/div[2]/div/div/div/span"
        ).click()
        time.sleep(2)
        driver.find_element_by_id("chkSelectAll").click()
        ClasForm.form_button_yes(self, "确定")
        # 培训地点
        driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div/div/div/div/form/div[1]/div[3]/div[3]/div/div/input"
        ).send_keys(fun_data_address())
        # 描述
        driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div/div/div/div/form/div[1]/div[3]/div[1]/div/div/textarea"
        ).send_keys(fun_data_character(100, 200))
        # 发布
        ClasForm.form_button_yes(self, "发布")
        time.sleep(3)
        v_tip = driver.find_elements_by_class_name("toast-message")
        for i in v_tip:
            if "发布成功" in i.text:
                print(i.text)
            elif "流程已触发" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(root_path() + 'TestPicture/hr/test_0512_01.jpg')
                print("Error：" + i.text)
                unittest.expectedFailure("test_0512_01")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(ReleaseTrain("test_0512_01"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)