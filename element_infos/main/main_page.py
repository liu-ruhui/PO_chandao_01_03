from common.base_page import BasePage
from common.browser import Browser
from common.conf_utils import conf
from common.element_data_utils import ElementDataUtils
from element_infos.login.login_page import LoginPage
'''实现退出功能'''


class MainPage(BasePage):
    def __init__(self,driver):
       super().__init__(driver)
       element = ElementDataUtils('项目').get_element_info('main_page')
       self.companyname_showbox = element['companyname_showbox']
       self.myzone_menu = element['myzone_menu']
       self.product_menu = element['product_menu']
       self.project_menu = element['project_menu']
       self.username_showspan = element['username_showspan']
       self.quit_button = element['quit_button']
       # print(self.quit_button)

    def get_companyname(self,text):  #获取公司名称
        value = self.get_element_attribute(self.companyname_showbox,text)
        print(value)

    def goto_myzone(self):  #进入我的地盘
        self.click(self.myzone_menu)
    def goto_product(self):  #进入产品菜单
        self.click(self.product_menu)
    def goto_project(self):  #进入项目菜单
        self.click(self.project_menu)
    def get_usename(self):  #获取用户名
      value = self.text(self.username_showspan)
      return value
    def click_username(self):
        self.click(self.username_showspan)
    def click_quit_button(self):
        self.click(self.quit_button)


if __name__ =="__main__":
    driver = Browser().get_driver()
    login_page = LoginPage(driver)
    login_page.open_url(conf.get_chandao_path)
    main_page = MainPage(driver)
    login_page.input_username('admin')
    login_page.input_password('Lrh19960912')
    login_page.click_login()
    main_page.get_companyname('title')
    main_page.goto_project()
    main_page.goto_product()
    main_page.get_usename()
