import unittest
from actions.login_action import LoginAction
from common.base_page import BasePage
from common.browser import Browser
from common.conf_utils import conf

class LoginTest(unittest.TestCase):
    def setUp(self)->None:
        self.base_page = BasePage(Browser().get_driver())
        self.base_page.set_maxwindow()
        self.base_page.implicitly_wait()
        self.base_page.open_url(conf.get_chandao_path)

    def tearDown(self):
        self.base_page.close()

    def test_login_success(self):
        login_action = LoginAction(self.base_page.driver)
        mainpage = login_action.login_success('admin','Lrh19960912')
        # a = mainpage.get_usename()
        self.assertEqual(mainpage.get_usename(),'admin','test_login_success用例执行失败')


if __name__ == '__main__':
    unittest.main()
