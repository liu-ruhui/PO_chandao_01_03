import unittest
from actions.login_action import LoginAction
from actions.quite_action import QuitAction
from common.selenium_base_case import SeleniumBaseCase


class LoginTest(SeleniumBaseCase):

    def test_quit(self):
        login_action = LoginAction(self.base_page.driver)
        login_action.default_login()
        quit_action = QuitAction(self.base_page.driver)
        login_page = quit_action.quit()
        actual_result = login_page.get_title()
        self.assertEqual(actual_result.__contains__('用户登录'),True,'test_quit用例不通过')



if __name__ == '__main__':
    unittest.main()
