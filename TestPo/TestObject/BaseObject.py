

# 创建基础类
from appium import webdriver


class BasePage(object):
    #初始化
    def __init__(self, driver):
        # server 启动参数
        self.desired_caps = {}
        # 设备信息
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['platformVersion'] = '5.1.1'
        self.desired_caps['deviceName'] = '127ac0b0'
        # desired_caps['deviceName'] = 'HINBSSU899999999'
        self.desired_caps['noReset'] = True

        # app信息
        # cb59731 u0 com.zhihu.android/.app.ui.activity.MainActivity t10334
        # com.zhihu.android/.app.ui.activity.MainActivity t35
        self.desired_caps['appPackage'] = 'com.zhihu.android'
        # desired_caps['appActivity'] = '.app.ui.activity.MainActivity t35'
        self.desired_caps['appActivity'] = '.app.ui.activity.MainActivity t10334'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)

        # self.base_url = 'https://mail.qq.com/'
        # self.driver = driver
        # self.timeout = 30

    # #打开页面
    # def _open(self):
    #     url = self.base_url
    #     self.driver.get(url)
    #     self.driver.switch_to.frame('login_frame')  #切换到登录窗口的iframe

    # def open(self):
    #     self._open()

    #定位方法封装
    def find_element(self,*loc):
        return self.driver.find_element(*loc)