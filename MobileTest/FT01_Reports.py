# -*- coding: utf-8 -*-
from uiautomator import device as d
import uiautomator
from selenium import webdriver
import time
import sys
import random
import unittest

class Reports(unittest.TestCase):
    '''初始准备工作，进入到微信-Onlinebox主页面'''
    def setUp(self):
        d.press.home()
        d(text="微信").click()
        time.sleep(3)
        if d(text="OnlineBox产品").exists:
            d(text="OnlineBox产品").click()
        else:
            pass

    '''系统管理-用户设置-用户管理'''
    def test_check(self):
        self.dr = webdriver.Android

        dr = self.dr
        dr.find


        print(u"开启APP")

    '''退出清理工作,返回到微信主页面'''
    def tearDown(self):
        d.press.home()
        d.press.recent()
        time.sleep(3)

        d.swipe(200, 500, 200, 0, steps=10)
        d.press.home()

