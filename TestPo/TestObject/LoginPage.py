# 创建LoginPage类
import time
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

from TestPo.TestObject.BaseObject import BasePage




class LoginPage(BasePage):
    # //*[contains(@text,'未登录')]
    user_login = (By.XPATH, "//*[contains(@text,'未登录')]")
    # // *[contains( @ resource - id, 'com.zhihu.android:id/qq_login_btn')]
    qq_login = (By.XPATH, "// *[contains(@resource-id, 'com.zhihu.android:id/qq_login_btn')]")
    # qq = (By.CLASS_NAME, "android.widget.LinearLayout")
    # TouchAction(UserLogin.test_user_login().driver).tap(x=155, y=250).perform()
    login = (By.CLASS_NAME, 'android.widget.Button')
    # login = (By.XPATH, '//*[contains(@text, "登录"]')
    # username_loc = (By.ID, "u")
    # password_loc = (By.ID, "p")
    # login_loc = (By.ID, "login_button")

    # 输入用户名
    # def type_username(self,username):
    #     self.find_element(*self.username_loc).send_keys(username)

    #输入密码
    # def type_password(self,password):
    #     self.find_element(*self.password_loc).send_keys(password)

    #点击登录
    def type_login(self):
        time.sleep(5)
        self.find_element(*self.user_login).click()
        time.sleep(5)
        self.find_element(*self.qq_login).click()
        time.sleep(5)
        self.driver.tap([(400,1150)])
        # self.find_element(*self.qq).click()
        time.sleep(10)
        self.find_element(*self.login).click()
        # return self

