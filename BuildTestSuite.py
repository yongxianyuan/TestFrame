import unittest
# import AssertMethodTestCase
# from TestSkip import *
import TestIntegerArithmetic
import TestSkip
from AssertMethodTestCase import *


class DemoTestCase(unittest.TestCase):
    def test01(self):
        self.assertIn(1, [1, 2, 3])

    def test02(self):
        self.assertNotIn(1, [2, 3, 4])

    def test03(self):
        self.assertCountEqual("12", '12')


def suite():
    testSuite = unittest.TestSuite()
    case1 = DemoTestCase('test03')
    case2 = TestIntegerArithmetic.IntegerArithmeticTestCase("testAdd")
    case3 = AssertMethodTestCase('testEqual')
    testSuite.addTest(case1)
    testSuite.addTest(case2)
    testSuite.addTest(case3)

    return testSuite


def suite_2():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    testcases = loader.loadTestsFromTestCase(AssertMethodTestCase)
    print(testcases)
    suite.addTest(testcases)

    return suite


def suite_3():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromModule(TestSkip))
    return suite


def suit_4():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(loader.discover(u'D:\Dev\PycharmProjects\TestFrame'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    # suite = unittest.TestSuite()
    # loader = unittest.TestLoader()
    # tests = loader.loadTestsFromModule(TestSkip)
    # print(tests)
    # suite.addTest(tests)
    # print(suite)
    # runner.run(suite())
    # print(suite())
    # runner.run(suite_2())
    runner.run(suite_3())
    # runner.run(suit_4())
    # runner.run(unittest.TestSuite().addTest(unittest.TestLoader().loadTestsFromModule(TestSkip)))
