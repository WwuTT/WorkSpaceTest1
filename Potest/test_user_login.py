#创建test_user_login()函数

from LoginPage import LoginPage


def test_user_login(driver):
    """测试用户名/密码是否可以登录"""
    login_page = LoginPage(driver)
    login_page.type_login()

