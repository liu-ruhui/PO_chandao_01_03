import os,time
from selenium import webdriver
from element_infos.project_page import ProjectPage
from common.login_utils import login
from element_infos.main_page import MainPage
from common.base_page import BasePage

class TaskPage(BasePage):
    def __init__(self,driver):
       super().__init__(driver)

       self.all_tesk = {'element_name': '所有任务',
                                 'locator_type': 'xpath',
                                 'locator_value':'//a[@id="all"]',
                                 'timeout': 2}
       self.unclosed_tesk = {'element_name': '未关闭的任务',
                                 'locator_type': 'xpath',
                                 'locator_value':'//a[@id="unclosed"]',
                                 'timeout': 2}
       self.assignedtome_tesk = {'element_name': '指派给我的任务',
                                 'locator_type': 'xpath',
                                 'locator_value':'//a[@id="assignedtome"]',
                                 'timeout': 2}
       self.myinvolved_tesk = {'element_name': '由我参与的任务',
                                 'locator_type': 'xpath',
                                 'locator_value':'//a[@id="myinvolved"]',
                                 'timeout': 2}
       self.more_tesk = {'element_name': '更多',
                                 'locator_type': 'xpath',
                                 'locator_value':'//div[@id="more"]',
                                 'timeout': 2}
       self.bysearchTab_tesk = {'element_name': '搜索',
                                 'locator_type': 'xpath',
                                 'locator_value':'//a[@id="bysearchTab"]',
                                 'timeout': 2}
       self.creates_tesk = {'element_name': '搜索',
                                 'locator_type': 'xpath',
                                 'locator_value':'//a[@href="/zentao/task-batchCreate-1--0.html"]',
                                 'timeout': 2}
       self.create_tesk = {'element_name': '搜索',
                                 'locator_type': 'xpath',
                                 'locator_value':'//a[@href="/zentao/task-create-1--0.html"]',
                                 'timeout': 2}

    def click_all_task(self):  #点击所有任务
        self.click(self.all_tesk)
    def click_unclosed_task(self):
        self.click(self.unclosed_tesk)
    def click_assignedtome_task(self):
            self.click(self.assignedtome_tesk)
    def click_myinvolved_task(self):
        self.click(self.myinvolved_tesk)
    def click_more_task(self):
        self.click(self.more_tesk)
    def click_bysearchTab_task(self):
        self.click(self.bysearchTab_tesk)


if __name__ =='__main__':
 login.login_success()
 task_page = TaskPage(login.driver)
 main_page = MainPage(login.driver)
project_page = ProjectPage(login.driver)
main_page.goto_project()
project_page.goto_task()
task_page.click_all_task()
task_page.close()