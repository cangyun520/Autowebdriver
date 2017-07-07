import os
import time
import csv
import random
# 导入测试报告
from HTMLTestRunner import HTMLTestRunner


# 获取当前项目根目录
def root_path(prjname="Autowebdriver"):
    v_path = os.getcwd()
    v_findpath = prjname
    v_thepath = v_path[:v_path.find(v_findpath)] + v_findpath + "/"
    return v_thepath


# 修改当前测试URL地址
def root_pc_testurl(url):
    f = open(root_path() + 'PubliData/config/url.txt', 'w+')
    if f.readline() == url:
        pass
    else:
        f.write(url)
        f.close()
    return url


# 休眠时间
def timesl(num):
    if 0 < num < 50:
        time.sleep(num)
    else:
        print("休眠时间非 大于0，小于50，请重新设置")
    return
