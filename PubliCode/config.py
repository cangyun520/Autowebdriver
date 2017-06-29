import time
import random
import os
import csv


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
    return root_path()
