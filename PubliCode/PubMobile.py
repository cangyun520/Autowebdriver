from appium import webdriver


def Ding_StartOpen(self):
    self.desired_caps = {}
    desired_caps = self.desired_caps
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '6.0.0'
    desired_caps['deviceName'] = 'Android Emulator'
    desired_caps['appPackage'] = 'com.alibaba.android.rimet'
    desired_caps['appActivity'] = '.biz.home.activity.HomeActivity'
    # 解决无法输入中文问题
    self.desired_caps["unicodeKeyboard"] = "True"
    self.desired_caps["resetKeyboard"] = "True"
    # self.desired_caps["automationName"] = "Selendroid"
