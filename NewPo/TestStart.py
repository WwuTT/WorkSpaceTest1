#创建test_user_login()函数

from LoginPage import newLoginPage
from appium import webdriver


class Test_zhihu():

    @classmethod
    def setUpClass(self):
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
        self.driver = driver

    def test_user_login(self):
        """测试用户名/密码是否可以登录"""
        # login_page = LoginPage(driver)
        # login_page.type_login()
        page = LoginPage()
        page.not_login.click()

    # @classmethod
    # def tearDownClass(self):
    #