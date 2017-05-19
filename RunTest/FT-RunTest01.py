
import unittest
import time
from HTMLTestRunner import HTMLTestRunner
from PubliCode.randData import root_path

# 修改当前测试URL地址
url = "http://test.b1box.net"
f = open(root_path() + 'PubliData/config/url.txt', 'w+')
if f.readline() == url:
    pass
else:
    f.write(url)
    f.close()

# 指定测试用例为当前文件夹下的test_case目录
# 通过自定函数获取当前文件所在路径
test_dir = root_path() + "FunctionTest"
discover = unittest.defaultTestLoader.discover(test_dir, pattern='FT0*.py')
if __name__ == '__main__':
    v_tim = time.strftime("%Y%m%d")
    FileName = root_path() + 'TestReport/FTRport/' + v_tim + 'FT_online01.htm'
    fp = open(FileName, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='online功能集成自动化测试',
                            description='online自动化测试——主流程功能测试执行结果统计')
    runner.run(discover)
    fp.close()