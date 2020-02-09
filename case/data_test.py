import ddt
import unittest
import os
import HTMLTestRunner
@ddt.ddt
class DataTest(unittest.TestCase):
    def setUp(self):
        print("这个是setup")
    def tearDown(self):
        print("这个是teardown")
    @ddt.data(["1","2"],["3","4"],["5","6"])
    @ddt.unpack
    def test_add(self,a,b):
        print(a+b)



if __name__ == '__main__':
    testPath = os.getcwd()
    suite = unittest.defaultTestLoader.discover(testPath, pattern='data_test.py', top_level_dir=None)
    htmlPath = os.path.join(os.path.dirname(os.getcwd()) + "\\report\\" + "first_case1.html")
    with open(htmlPath, 'wb') as f:
        runner = HTMLTestRunner(stream=f, title="ddt report", description="测试报告:", verbosity=0)
        runner.run(suite)




    # unittest.main()

    # suite = unittest.TestLoader().loadTestsFromTestCase(DataTest)

    # unittest.TextTestRunner().run(suite)
