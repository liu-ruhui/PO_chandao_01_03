from element_infos.login.login_page import LoginPage
from element_infos.main.main_page import MainPage
from common.conf_utils import conf

class LoginAction:
    def __init__(self,driver):
        self.login_page = LoginPage(driver)
        self.main_page = MainPage(driver)

    def login_action(self,username,password):
        self.login_page.input_username(username)
        self.login_page.input_password(password)
        self.login_page.click_login()

    def login_success(self,username,password):
        self.login_action(username,password)
        return MainPage(self.login_page.driver)

    def default_login(self):
        return self.login_success(conf.get_username,conf.get_password)

    def login_fail(self,username,password):
        self.login_action(username,password)
        return self.login_page.get_login_fail_alter_content()

    def login_by_cookie(self):
        pass


