from business.register_business import RegisterBusiness
from selenium import webdriver
from log.user_log import UserLog
import time,os,sys
import unittest
import HTMLTestRunner

class FirstCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.file_name="E:\\test001.png"
        cls.log = UserLog()
        cls.logger = cls.log.get_logger()
    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.get("http://www.5itest.cn/register")
        self.logger.info("this is a firfox")
        time.sleep(2)
        self.login=RegisterBusiness(self.driver)

    def tearDown(self):
        time.sleep(3)
        for method_name,error in self._outcome.errors:
            if error:
                case_name=self._testMethodName
                file_path=os.path.join(os.path.dirname(os.getcwd())+"\\report\\"+case_name+".png")
                self.driver.save_screenshot(file_path)
        # if sys.exc_info()[0]:
        #
        self.driver.close()
        print("后置条件")
    def test_login_email_error(self):
        email_error=self.login.login_email_error("3664","11111","222",self.file_name)
        self.assertFalse(email_error,"email case")
        # if email_error==True:
        #     print("注册成功了，此条case失败")
    def test_login_username_error(self):
        username_error=self.login.login_name_error("111@163.com","1","11111",self.file_name)
        self.assertFalse(username_error,"name case")
        # if username_error==True:
        #     print("注册成功了，此条case失败")
    def test_login_password_error(self):
        password_error = self.login.login_password_error("111@163.com", "1ii11", "11",self.file_name)
        self.assertFalse(password_error,"password case")
        # if password_error == True:
        #     print("注册成功了，此条case失败")
    def test_login_code_error(self):
        code_error = self.login.login_code_error("111@163.com", "ss", "11111", self.file_name)
        self.assertFalse(code_error,"code case")
        # if code_error == True:
        #     print("注册成功了，此条case失败")
    def test_login_success(self):
        success=self.login.user_base("123@163.com",'ssss','22222',self.file_name)
        self.assertFalse(success)
        # if self.login.register_success()==True:
        #     print("注册成功")
# def main():
#     first=FirstCase()
#     first.test_login_email_error()
#     first.test_login_username_error()
#     first.test_login_password_error()
#     first.test_login_code_error()
#     first.test_login_success()

if __name__ == '__main__':
    # unittest.main()
    file_path=os.path.join(os.path.dirname(os.getcwd())+"\\report\\"+"first_case.html")
    print(file_path)
    f=open(file_path,'wb')
    suite=unittest.TestSuite()
    suite.addTest(FirstCase('test_login_success'))
    suite.addTest(FirstCase('test_login_code_error'))
    suite.addTest(FirstCase('test_login_password_error'))
    suite.addTest(FirstCase('test_login_username_error'))
    suite.addTest(FirstCase('test_login_email_error'))

    # unittest.TextTestRunner().run(suite)
    runner=HTMLTestRunner.HTMLTestRunner(stream=f,title="this is firat report",description="cess",verbosity=2)
    runner.run(suite)