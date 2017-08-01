from PubliCode.onlineClass import *

test_dir = root_path() + "MobileTest"
discover = unittest.defaultTestLoader.discover(
    test_dir,
    pattern='FT*.py'
)
if __name__ == '__main__':
    v_tim = time.strftime("%Y%m%d")
    FileName = root_path() + 'TestReport/FTRport/' + v_tim + 'MT_DingWeChat.htm'
    fp = open(FileName, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='online微信钉钉自动化测试',
                            description='online微信钉钉自动化测试——主流程功能测试执行结果统计')
    runner.run(discover)
    fp.close()
