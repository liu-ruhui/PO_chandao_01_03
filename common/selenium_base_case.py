import unittest
from common.base_page import BasePage
from common.browser import Browser
from  common.conf_utils import conf
'''自定义unittest.TestCase，新增一个子类。简化test用例的写法，不用重复调用'''

class SeleniumBaseCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.url = conf.get_chandao_path

    def setUp(self):
        self.base_page = BasePage(Browser().get_driver())
        self.base_page.set_maxwindow()
        self.base_page.implicitly_wait()
        self.base_page.open_url(self.url)

    def tearDown(self):
        self.base_page.close()
        #测试用例失败截图
