import ddt
from business.register_business import RegisterBusiness
from selenium import webdriver
import time,os,sys
import unittest
import HTMLTestRunner
from util.excel_util import ExcelUtil
ex=ExcelUtil()
data=ex.get_data()

@ddt.ddt
class FirstDdtCase(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.get("http://www.5itest.cn/register")
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
    # @ddt.data(
    #     ["1232@", "1234", "123456", "F:\\workspace\\python\\py\\report\\test001.png", "user_email_error", "请输入有效的电子邮件地址"],
    #     # ["@163.com", "1234", "123456", "F:\\workspace\\python\\py\\report\\test001.png", "user_email_error", "请输入有效的电子邮件地址"],
    #     # ["1232@163.com", "1234", "123456", "F:\\workspace\\python\\py\\report\\test001.png", "user_email_error", "请输入有效的电子邮件地址"]
    # )
    # @ddt.unpack

    @ddt.data(*data)
    def test_register_case(self,data):
      email, username, password, code, assertCode, assertText=data
      print('username==',username)
      print('password=',password)
      email_error = self.login.register_function(email,username,password,code,assertCode,assertText)
      print(code)
      self.assertFalse(email_error, "email case")

if __name__ == '__main__':
    # unittest.main()
    print("1111")
    file_path = os.path.join(os.path.dirname(os.getcwd()) + "\\report\\" + "first_case1.html")
    print(file_path)
    fd = open(file_path, 'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)
    # unittest.TextTestRunner().run(suite)
    # suite = unittest.TestSuite()
    # suite.addTest(FirstDdtCase('test_register_case'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=fd, title="this is first report1", description="cess1", verbosity=2)
    runner.run(suite)