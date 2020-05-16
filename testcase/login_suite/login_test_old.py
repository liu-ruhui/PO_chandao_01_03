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
        main_page = login_action.login_success('admin','Lrh19960912')
        a = main_page.get_usename()
        print(a)
        self.assertEqual(main_page.get_usename(),'admin','test_login_success用例执行失败')

    def test_login_fail(self):
        login_action = LoginAction(self.base_page.driver)
        actual_result = login_action.login_fail('admin','123456')
        print('actual:%s'%actual_result)
        self.assertEqual(actual_result,'登录失败，请检查您的用户名或密码是否填写正确。')




if __name__ == '__main__':
    unittest.main()
