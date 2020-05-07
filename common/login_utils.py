from common.conf_utils import conf
from common.set_driver import set_driver
from element_infos.login.login_page import LoginPage


def login_success():
        login_page = LoginPage(set_driver(conf.get_chandao_path))
        login_page.input_username(conf.get_username)
        login_page.input_password(conf.get_password)
        login_page.click_login()


if __name__ == '__main__':
    login_success()