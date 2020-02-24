from appium import webdriver

from Logic.Login import user_login
import pytest
import requests


class UserWork():
    def __init__(self):
        # driver = webdriver.Edge()
        # username = '3494xxxxx'    #qq号码
        # password = 'kemixxxx'    #qq密码
        desired_caps = {}
        # 设备信息
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1.1'
        desired_caps['deviceName'] = '127ac0b0'
        # desired_caps['deviceName'] = 'HINBSSU899999999'
        desired_caps['noReset'] = True

        # app信息
        # cb59731 u0 com.zhihu.android/.app.ui.activity.MainActivity t10334
        # com.zhihu.android/.app.ui.activity.MainActivity t35
        desired_caps['appPackage'] = 'com.zhihu.android'
        # desired_caps['appActivity'] = '.app.ui.activity.MainActivity t35'
        desired_caps['appActivity'] = '.app.ui.activity.MainActivity t10334'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test_user_login(self):

        user_login(driver=self.driver)

    def teardown_class(self):
        self.driver.quit()


s = requests.session()

s.keep_alive = False

work = UserWork()
work.test_user_login()


