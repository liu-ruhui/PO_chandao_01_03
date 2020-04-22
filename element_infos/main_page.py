import os,time
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.login_utils import login
from element_infos.login_page import LoginPage
from common.base_page import BasePage

class MainPage(BasePage):
    def __init__(self,driver):
       super().__init__(driver)

       self.companyname_showbox = {'element_name': '公司名称',
                                 'locator_type': 'xpath',
                                 'locator_value': '//h1[@id="companyname"]',
                                 'timeout': 2}
       self.myzone_menu = {'element_name': '我的地盘模块',
                                   'locator_type': 'xpath',
                                   'locator_value': '//li[@data-id="my"]',
                                   'timeout': 2}
       self.product_menu = {'element_name': '产品模块',
                                   'locator_type': 'xpath',
                                   'locator_value': '//li[@data-id="product"]',
                                   'timeout': 2}
       self.project_menu = {'element_name': '项目模块',
                                   'locator_type': 'xpath',
                                   'locator_value': '//li[@data-id="project"]',
                                   'timeout': 2}
       self.username_showspan = {'element_name': '用户按钮',
                                   'locator_type': 'xpath',
                                   'locator_value': '//span[@class="user-name"]',
                                   'timeout': 2}
    # def get_companyname(self,text):  #获取公司名称
    #     self.getattribute(self.companyname_showbox,text)
    def goto_myzone(self):  #进入我的地盘
        self.click(self.myzone_menu)
    def goto_product(self):  #进入产品菜单
        self.click(self.product_menu)
    def goto_project(self):  #进入项目菜单
        self.click(self.project_menu)
    # def get_usename(self):  #获取用户名
    #     self.text(self.username_showspan)


if __name__ =="__main__":
    currrent_path = os.path.dirname(__file__)
    driver_path = os.path.join(currrent_path, '..\\webdriver\geckodriver.exe')
    driver = webdriver.Firefox(executable_path=driver_path)
    login_page = LoginPage(driver)
    login_page.open_url('http://127.0.0.1:8080/zentao/user-login-L3plbnRhby8=.html')
    login_page.input_username('admin')
    login_page.input_password('Lrh19960912')
    login_page.click_login()
    main_page = MainPage(driver)
    main_page.goto_project()
