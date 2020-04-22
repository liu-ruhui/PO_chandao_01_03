import os
from element_infos.login_page import LoginPage
from selenium import webdriver
from common.conf_utils import conf


class Login(object):
    def __init__(self):
        currrent_path = os.path.dirname(__file__)
        driver_path = os.path.join(currrent_path, conf.get_gecko_path)
        driver = webdriver.Firefox(executable_path=driver_path)
        self.driver = driver
    def login_success(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.open_url(conf.get_chandao_path)
        self.login_page.input_username(conf.get_username)
        self.login_page.input_password(conf.get_password)
        self.login_page.click_login()
login = Login()

if __name__ == '__main__':
    login.login_success()