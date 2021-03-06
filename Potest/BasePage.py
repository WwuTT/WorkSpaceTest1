
class BasePage():
    def __init__(self, driver):
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
        self.driver = driver

    # 定位方法封装
    def find_element(self,*loc):
        return self.driver.find_element(*loc)


