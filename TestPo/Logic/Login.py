#创建test_user_login()函数
from TestPo.TestObject.LoginPage import LoginPage


def user_login(driver):
    """测试用户名/密码是否可以登录"""
    login_page = LoginPage(driver)
    # login_page.open()
    # login_page.type_username(username)
    # login_page.type_password(password)
    login_page.type_login()