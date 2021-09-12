import unittest
import logging

import BeautifulReport

logging.basicConfig(level=logging.INFO)


def setUpModule():
    logging.info('TestSkip模块开始前初始化...')


def tearDown():
    logging.info('TestSkip模块结束前清理...')


class SkipTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        logging.info('SkipTestCase类模块开始前初始化...')

    @classmethod
    def tearDownClass(cls) -> None:
        logging.info('SkipTestCase类模块结束前清理...')

    def setUp(self) -> None:
        logging.info('测试用例开始前初始化...')

    def tearDown(self) -> None:
        logging.info('测试用例结束前清理...')

    def testTrue(self):
        # self.assertTrue(None, '空对象结果')
        self.assertFalse(bool(1), '数字1转为布尔值结果是True')

    # @BeautifulReport.add_test_img('测试报告.png')
    def testIs(self):
        self.assertIs(10, int(10), '不都是整数10')
        self.assertIsNot('s', str('s'), '都是字符串')


if __name__ == '__main__':
    unittest.main()
