
import unittest
import time
from HTMLTestRunner import HTMLTestRunner
from PubliCode.randData import root_path

# 指定测试用例为当前文件夹下的test_case目录
# 通过自定函数获取当前文件所在路径
test_dir = root_path() + "BaseDataSet"
discover = unittest.defaultTestLoader.discover(test_dir, pattern='Int*.py')
v_tim = time.strftime("%Y%m%d")
if __name__ == '__main__':
    FileName = root_path() + 'TestReport/BDReport/' + v_tim + 'Int_online.htm'
    fp = open(FileName, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='online初始化数据添加',
                            description='online初始化数据添加结果统计')
    runner.run(discover)
    fp.close()

