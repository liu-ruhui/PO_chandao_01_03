import os,time
from selenium import webdriver
from element_infos.login_page import LoginPage
from element_infos.main_page import MainPage
from common.base_page import BasePage

class ProjectPage(BasePage):
    def __init__(self,driver):
       super().__init__(driver)

       self.task_menu = {'element_name': '任务模块',
                                 'locator_type': 'xpath',
                                 'locator_value':'//li[@data-id="task"]',
                                 'timeout': 2}
       self.kanban_menu = {'element_name': '看板模块',
                                   'locator_type': 'xpath',
                                   'locator_value': '//li[@data-id="kanban"]',
                                   'timeout': 2}
       self.burn_menu = {'element_name': '燃尽图模块',
                                   'locator_type': 'xpath',
                                   'locator_value': '//li[@data-id="burn"]',
                                   'timeout': 2}
       self.list_menu = {'element_name': '更多',
                                   'locator_type': 'xpath',
                                   'locator_value': '//li[@data-id="list"]',
                                   'timeout': 2}
       self.story_menu = {'element_name': '需求模块',
                                   'locator_type': 'xpath',
                                   'locator_value': '//li[@data-id="story"]',
                                   'timeout': 2}
       self.qa_menu = {'element_name': '测试模块',
                                   'locator_type': 'xpath',
                                   'locator_value': '//li[@data-id="qa"]',
                                   'timeout': 2}
       self.doc_menu = {'element_name': '文档模块',
                                   'locator_type': 'xpath',
                                   'locator_value': '//li[@data-id="doc"]',
                                   'timeout': 2}
       self.team_menu = {'element_name': '团队模块',
                                   'locator_type': 'xpath',
                                   'locator_value': '//li[@data-id="team"]',
                                   'timeout': 2}
       self.action_menu = {'element_name': '动态模块',
                                   'locator_type': 'xpath',
                                   'locator_value': '//li[@data-id="action"]',
                                   'timeout': 2}
       self.product_menu = {'element_name': '产品模块',
                                   'locator_type': 'xpath',
                                   'locator_value': '//li[@data-id="product"]',
                                   'timeout': 2}
       self.view_menu = {'element_name': '概况模块',
                                   'locator_type': 'xpath',
                                   'locator_value': '//li[@data-id="view"]',
                                   'timeout': 2}

    def goto_task(self):  #进入任务
        self.click(self.task_menu)


if __name__ =='__main__':
    currrent_path = os.path.dirname(__file__)
    driver_path = os.path.join(currrent_path, '..\\webdriver\geckodriver.exe')
    driver = webdriver.Firefox(executable_path=driver_path)
    project_page = ProjectPage(driver)
    project_page.open_url('http://127.0.0.1:8080/zentao/user-login-L3plbnRhby8=.html')
    login_page = LoginPage(driver)
    login_page.input_usename('admin')
    login_page.input_password('Lrh19960912')
    login_page.click_login()
    main_page = MainPage(driver)
    main_page.goto_product()
    project_page.goto_task()