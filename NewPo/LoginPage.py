
from poium import Page, PageElement



class newLoginPage(Page):
    # //*[contains(@text,'未登录')]
    # user_login = (By.XPATH, "//*[contains(@text,'未登录')]")
    # // *[contains( @ resource - id, 'com.zhihu.android:id/qq_login_btn')]
    # qq_login = (By.XPATH, "// *[contains(@resource-id, 'com.zhihu.android:id/qq_login_btn')]")
    # login = (By.CLASS_NAME, 'android.widget.Button')
    # self.base_page = BasePage()
    """
    page层，页面封装操作到的元素
    """
    not_login = PageElement(xpath = "//*[contains(@text,'未登录')]", timeout=5)
    qq_login = PageElement(xpath = "// *[contains(@resource-id, 'com.zhihu.android:id/qq_login_btn')]", timeout=5)
    login = PageElement(class_name = 'android.widget.Button', timeout=5)

    #点击登录
    # def type_login(self):
    #     time.sleep(5)
    #     self.by_xpath("//*[contains(@text,'未登录')]").click()
    #     time.sleep(5)
    #     self.by_xpath("// *[contains(@resource-id, 'com.zhihu.android:id/qq_login_btn')]").click()
    #     time.sleep(5)
    #     self.driver.tap([(400,1150)])
    #     # self.find_element(*self.qq).click()
    #     time.sleep(10)
    #     self.by_class('android.widget.Button').click()
        # return self