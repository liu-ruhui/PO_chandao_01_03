
from common.base_page import BasePage
from common.browser import Browser
from common.conf_utils import conf
from common.element_data_utils import ElementDataUtils
from common.login_utils import LoginPage
from element_infos.main.main_page import MainPage
from element_infos.project.project_page import ProjectPage


class TaskPage(BasePage):
    def __init__(self,driver):
       super().__init__(driver)
       elements = ElementDataUtils('任务').get_element_info('task_page')
       self.all_tesk = elements['all_tesk']
       self.unclosed_tesk = elements['unclosed_tesk']
       self.assignedtome_tesk = elements['assignedtome_tesk']
       self.myinvolved_tesk = elements['myinvolved_tesk']
       self.delayed_tesk = elements['delayed_tesk']
       self.more_tesk = elements['more_tesk']
       self.bysearchTab_tesk = elements['bysearchTab_tesk']
       self.creates_tesk = elements['creates_tesk']
       self.create_tesk = elements['create_tesk']

    def click_all_task(self):  #点击所有任务
        self.click(self.all_tesk)
    def click_unclosed_task(self):#点击未关闭任务
        self.click(self.unclosed_tesk)
    def click_assignedtome_task(self):#点击指派给我的任务
        self.click(self.assignedtome_tesk)
    def click_myinvolved_task(self):#点击有我参与的任务
        self.click(self.myinvolved_tesk)
    def clik_delayed_task(self): #点击已延期的任务
        self.click(self.delayed_tesk)
    def click_more_task(self):#点击所有任务
        self.click(self.more_tesk)
#搜索
    def click_bysearchTab_task(self):
        self.click(self.bysearchTab_tesk)


if __name__ =='__main__':
  driver = Browser().get_driver()
  login_page = LoginPage(driver)
  login_page.open_url(conf.get_chandao_path)
  task_page = TaskPage(driver)
  main_page = MainPage(driver)
  project_page = ProjectPage(driver)
  login_page.input_username('admin')
  login_page.input_password('Lrh19960912')
  login_page.click_login()
  main_page.goto_project()
  project_page.goto_task()
  task_page.click_all_task()
