import time
from selenium.webdriver.common.by import By
from BasePage import BasePage


class LoginPage(BasePage):
    # //*[contains(@text,'未登录')]
    user_login = (By.XPATH, "//*[contains(@text,'未登录')]")
    # // *[contains( @ resource - id, 'com.zhihu.android:id/qq_login_btn')]
    qq_login = (By.XPATH, "// *[contains(@resource-id, 'com.zhihu.android:id/qq_login_btn')]")
    login = (By.CLASS_NAME, 'android.widget.Button')
    # self.base_page = BasePage()
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