import unittest,os
from case.first_case import FirstCase
import HTMLTestRunner
if __name__ == '__main__':
    # unittest.main()
    file_path=os.path.join(os.getcwd()+"\\report\\"+"first_case.html")
    print(file_path)
    f=open(file_path,'wb')
    suite=unittest.TestSuite()
    suite.addTest(FirstCase('test_login_success'))
   # suite.addTest(FirstCase('test_login_code_error'))
   # suite.addTest(FirstCase('test_login_password_error'))
   # suite.addTest(FirstCase('test_login_username_error'))
   # suite.addTest(FirstCase('test_login_email_error'))

    # unittest.TextTestRunner().run(suite)
    runner=HTMLTestRunner.HTMLTestRunner(stream=f,title="this is firat report",description="cess",verbosity=2)
    runner.run(suite)