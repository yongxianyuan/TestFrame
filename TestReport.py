import unittest
from BeautifulReport import BeautifulReport

if __name__ == '__main__':
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    tests = loader.discover(u'D:\Dev\PycharmProjects\TestFrame',pattern='*test*.py')
    print(tests)
    suite.addTest(tests)
    result = BeautifulReport(suite)
    result.report(filename='测试报告', description='测试TestFrame单元报告', report_dir='report', theme='theme_default')
