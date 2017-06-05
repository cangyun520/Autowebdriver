from PubliCode.onlineClass import *
from PubliCode.randData import *

'''
    *   Arvin
    *   2017-04-13
'''


class LogWrite(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.PhantomJS()
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "事务处理", "工作日志", "日志填报")
        driver.switch_to.frame("frame_tab_PM000483")

    '''事务处理-工作日志-日志填报'''
    def test_0202_01(self):
        """事务处理-工作日志-日报功能测试"""
        driver = self.driver
        v_time = time.strftime("%Y-%m-%d %H:%M:%S")
        # 今日完成
        driver.find_element_by_id("WorkDiaryContent").send_keys('Arvin-日报-自动化测试 ' + v_time)
        # 明日计划
        driver.find_element_by_id("WorkDiaryWorkRecord").send_keys(v_time + fun_data_character(10, 200))
        driver.find_element_by_id("WorkDiaryWorkSummary").send_keys(v_time + fun_data_character(100, 500))   # 需协调的工作
        time.sleep(1)
        # 汇报人-选择
        driver.find_element_by_link_text("选择").click()
        time.sleep(2)
        # 用户弹出窗体
        driver.switch_to.default_content()
        ClasForm.form_top(self,0)
        driver.switch_to.frame("frame_tab_PM000483")
        driver.switch_to.frame("frame_users")
        for i in driver.find_elements_by_tag_name("td"):
            if "超级管理员" in i.text:
                i.click()
                break
        time.sleep(2)
        driver.find_element_by_id("ckAll").click()
        time.sleep(1)
        # 确定
        driver.find_element_by_id("btnSelect").click()
        # 添加
        time.sleep(2)
        driver.switch_to.parent_frame()     # 返回上一层级iframe
        driver.find_element_by_id("btnDay").click()
        time.sleep(3)
        for i in driver.find_elements_by_class_name("bootbox-body"):
            try:
                '提交成功' in i.text
                print(i.text)
            except ImportError:
                driver.get_screenshot_as_file(root_path() + "/TestPicture/oa/test_0202_01.jpg")
                # print(i.text)
                unittest.expectedFailure("test_0202_01")

    '''事务处理-工作日志-周报功能测试'''
    def test_0202_02(self):
        """事务处理-工作日志-周报功能测试"""
        driver = self.driver
        driver.find_element_by_link_text(u"周报").click()
        v_time = time.strftime("%Y-%m-%d %H:%M:%S")
        # 本周完成
        driver.find_element_by_id("WorkWeekDiaryContent").send_keys('Arvin-周报-自动化测试 ' + v_time)
        # 本周总结
        driver.find_element_by_id("WorkWeekDiaryWorkSummary").send_keys(v_time + fun_data_character(10, 200))
        # 下周计划
        driver.find_element_by_id("WorkWeekDiaryWorkRecord").send_keys(v_time + fun_data_character(50, 300))
        # 需协调的工作
        driver.find_element_by_id("WorkWeekDiaryWorkConcert").send_keys(v_time + fun_data_character(100, 500))
        # 汇报人-选择
        driver.find_element_by_link_text("选择").click()
        time.sleep(2)
        # 用户弹出窗体
        driver.switch_to.default_content()
        ClasForm.form_top(self,0)
        driver.switch_to.frame("frame_tab_PM000483")
        driver.switch_to.frame("frame_users")
        for i in driver.find_elements_by_tag_name("td"):
            if i.text == "超级管理员":
                i.click()
                break
        time.sleep(2)
        driver.find_element_by_id("ckAll").click()
        time.sleep(2)
        # 确定
        driver.find_element_by_id("btnSelect").click()
        # 添加
        time.sleep(2)
        driver.switch_to.parent_frame()     # 返回上一层级iframe
        driver.find_element_by_id("btnWeek").click()
        time.sleep(3)
        for i in driver.find_elements_by_class_name("bootbox-body"):
            try:
                "提交成功" in i.text
                print(i.text)
            except ImportError:
                driver.get_screenshot_as_file(root_path() + "TestPicture/oa/test_0202_02.jpg")
                unittest.expectedFailure("test_0202_02")

    '''事务处理-工作日志-月报功能测试'''
    def test_0202_03(self):
        """事务处理-工作日志-月报功能测试"""
        driver = self.driver
        driver.find_element_by_link_text(u"月报").click()
        v_time = time.strftime("%Y-%m-%d %H:%M:%S")
        # 本月完成
        driver.find_element_by_id("WorkMonthDiaryContent").send_keys('Arvin-月报-自动化测试 ' + v_time)
        # 本月总结
        driver.find_element_by_id("WorkMonthDiarySummary").send_keys(v_time + fun_data_character(100, 300))
        # 下月计划
        driver.find_element_by_id("WorkMonthDiaryRecord").send_keys(v_time + fun_data_character(200, 400))
        # 需协调的工作
        driver.find_element_by_id("WorkMonthDiaryConcert").send_keys(v_time + fun_data_character(400, 600))
        time.sleep(1)
        # 汇报人-选择
        driver.find_element_by_link_text("选择").click()
        time.sleep(2)
        # 用户弹出窗体
        driver.switch_to.frame("frame_users")
        for i in driver.find_elements_by_tag_name("td"):
            if i.text == "超级管理员":
                i.click()
                break
        time.sleep(2)
        driver.find_element_by_id("ckAll").click()
        time.sleep(2)
        # 确定
        driver.find_element_by_id("btnSelect").click()
        # 添加
        time.sleep(2)
        driver.switch_to.parent_frame()     # 返回上一层级iframe
        driver.find_element_by_id("btnMonth").click()
        time.sleep(3)
        for i in driver.find_elements_by_class_name("bootbox-body"):
            try:
                "提交成功" in i.text
                print(i.text)
            except ImportError:
                driver.get_screenshot_as_file(root_path() + "/TestPicture/oa/test_0202_03.jpg")
                # print(i.text)
                unittest.expectedFailure("test_0202_03")

    '''事务处理-工作日志-我发出的日志查看'''
    def test_0202_04(self):
        """事务处理-工作日志-我发出的日志查看"""
        driver = self.driver
        driver.find_element_by_link_text(u"我发出的").click()
        driver.find_elements_by_link_text("查看详情")[0].click()
        time.sleep(2)
        # 评论
        v_time = time.strftime("%Y-%m-%d %H:%M:%S")
        driver.find_element_by_id("txt_comment").send_keys(v_time + fun_data_character(10, 100))
        time.sleep(1)
        driver.find_element_by_id("btncomment").click()
        time.sleep(1)
        for i in driver.find_elements_by_class_name("bootbox-body"):
            try:
                "提交成功" in i.text
                print(i.text)
            except AssertionError:
                driver.get_screenshot_as_file(root_path() + "TestPicture/oa/test_0202_04.jpg")
                print(i.text)
                unittest.expectedFailure("test_0202_04")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(LogWrite("test_0202_01"))
    testsuit.addTest(LogWrite("test_0202_02"))
    v_time = time.strftime("%y%m%d%H%M")
    # 定义报告存放路径
    FileName = root_path() + 'TestReport/FT04_Task/' + v_time + ' FT04_WriteLog.htm'
    ReportFile = open(FileName, 'wb')
    runner = HTMLTestRunner(stream=ReportFile,
                            title="事务处理-工作日志-日志填报",
                            description="黑盒自动化测试执行结果统计")
    # 运行测试用例集合
    runner.run(testsuit)
    ReportFile.close()

"""
python标准异常
异常名称	描述
BaseException	所有异常的基类
SystemExit	解释器请求退出
KeyboardInterrupt	用户中断执行(通常是输入^C)
Exception	常规错误的基类
StopIteration	迭代器没有更多的值
GeneratorExit	生成器(generator)发生异常来通知退出
StandardError	所有的内建标准异常的基类
ArithmeticError	所有数值计算错误的基类
FloatingPointError	浮点计算错误
OverflowError	数值运算超出最大限制
ZeroDivisionError	除(或取模)零 (所有数据类型)
AssertionError	断言语句失败
AttributeError	对象没有这个属性
EOFError	没有内建输入,到达EOF 标记
EnvironmentError	操作系统错误的基类
IOError	输入/输出操作失败
OSError	操作系统错误
WindowsError	系统调用失败
ImportError	导入模块/对象失败
LookupError	无效数据查询的基类
IndexError	序列中没有此索引(index)
KeyError	映射中没有这个键
MemoryError	内存溢出错误(对于Python 解释器不是致命的)
NameError	未声明/初始化对象 (没有属性)
UnboundLocalError	访问未初始化的本地变量
ReferenceError	弱引用(Weak reference)试图访问已经垃圾回收了的对象
RuntimeError	一般的运行时错误
NotImplementedError	尚未实现的方法
SyntaxError	Python 语法错误
IndentationError	缩进错误
TabError	Tab 和空格混用
SystemError	一般的解释器系统错误
TypeError	对类型无效的操作
ValueError	传入无效的参数
UnicodeError	Unicode 相关的错误
UnicodeDecodeError	Unicode 解码时的错误
UnicodeEncodeError	Unicode 编码时错误
UnicodeTranslateError	Unicode 转换时错误
Warning	警告的基类
DeprecationWarning	关于被弃用的特征的警告
FutureWarning	关于构造将来语义会有改变的警告
OverflowWarning	旧的关于自动提升为长整型(long)的警告
PendingDeprecationWarning	关于特性将会被废弃的警告
RuntimeWarning	可疑的运行时行为(runtime behavior)的警告
SyntaxWarning	可疑的语法的警告
UserWarning	用户代码生成的警告
"""