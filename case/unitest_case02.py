import unittest
class FirstCase02(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("所有case执行之前前置")
    @classmethod
    def tearDownClass(cls):
        print("所有case执行之后的后置")
    def setUp(self):
        print("这个是case的前置条件")
    def tearDown(self):
        print("这个是case的后置条件")
    # @unittest.skip("不执行第一条")
    def testfirst001(self):
        print("者是第一001个case")
    def testfirst002(self):
        print("者是第002个case")
if __name__ == '__main__':
   # unittest.main()
    suite=unittest.TestSuite()
    # suite.addTest(FirstCase02('testfirst002'))
    suite.addTest(FirstCase02('testfirst001'))
    unittest.TextTestRunner().run(suite)