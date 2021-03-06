import unittest
from actions.login_action import LoginAction
from common.base_page import BasePage
from common.browser import Browser
from common.conf_utils import conf
from common.selenium_base_case import SeleniumBaseCase

class LoginTest(SeleniumBaseCase):  #LoginTest继承SeleniumBaseCase继承unittest.TestCase

#调用父类的setup后再个性化调用子类的Setup（单个测试模块需要加载一些新的代码时才写）
    def setUp(self):
      super().setUp()  #不加会将原有的方法覆盖
      print('hello')

#登陆成功的用例
    def test_login_success(self):
        login_action = LoginAction(self.base_page.driver)
        main_page = login_action.login_success('admin','Lrh19960912')
        self.assertEqual(main_page.get_usename(),'admin','test_login_success用例执行失败')
#登陆失败，密码错误的用例
    def test_login_fail(self):
        login_action = LoginAction(self.base_page.driver)
        actual_result = login_action.login_fail('admin','123456')
        print('actual:%s'%actual_result)
        self.assertEqual(actual_result,'登录失败，请检查您的用户名或密码是否填写正确。')




if __name__ == '__main__':
    unittest.main()
