import os
from element_infos.login_page import LoginPage
from selenium import webdriver

class Login(object):
    def __init__(self):
        currrent_path = os.path.dirname(__file__)
        driver_path = os.path.join(currrent_path, '..\\webdriver\geckodriver.exe')
        driver = webdriver.Firefox(executable_path=driver_path)
        self.driver = driver
    def login_success(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.open_url('http://127.0.0.1:8080/zentao/user-login-L3plbnRhby8=.html')
        self.login_page.input_username('admin')
        self.login_page.input_password('Lrh19960912')
        self.login_page.click_login()
login = Login()

if __name__ == '__main__':
    login.login_success()