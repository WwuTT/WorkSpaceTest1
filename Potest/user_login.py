from test_user_login import test_user_login
from appium import webdriver

def user_login():
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

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    # username = '3494xxxxx'    #qq号码
    # password = 'kemixxxx'    #qq密码
    test_user_login(driver)

user_login()