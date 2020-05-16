from element_infos.login.login_page import LoginPage
from element_infos.main.main_page import MainPage
from common.conf_utils import conf

class QuitAction:
    def __init__(self,driver):
        self.main_page = MainPage(driver)

    def quit(self):
        self.main_page.click_username()
        self.main_page.click_quit_button()
        return LoginPage(self.main_page.driver)  #退出后返回到首页