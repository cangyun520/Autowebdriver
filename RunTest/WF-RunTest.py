import unittest
import time
from HTMLTestRunner import HTMLTestRunner
from PubliCode.randData import root_path

# 指定测试用例为当前文件夹下的test_case目录
# 通过自定函数获取当前文件所在路径
test_dir = root_path() + "WorkFlow"
discover = unittest.defaultTestLoader.discover(test_dir, pattern='FT*.py')
if __name__ == '__main__':
    v_tim = time.strftime("%Y%m%d")
    FileName = root_path() + 'TestReport/FTRport/' + v_tim + ' WorkFlow.htm'
    fp = open(FileName, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='online单据自由流自动化测试',
                            description='online自动化测试——单据自由流发起，审批，终审测试执行结果统计')
    runner.run(discover)
    fp.close()