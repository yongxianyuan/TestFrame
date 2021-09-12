import unittest
import logging

logging.basicConfig(level=logging.INFO)


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
        print('testTure用例开始执行')
        self.assertFalse(bool(1), '数字1转为布尔值结果是True')

    # @unittest.skip('这个用例testIs被跳过了')
    # @unittest.skipIf(1<2, '因为1小于2')
    @unittest.skipUnless(1 > 2, '因为1大于2')
    def testIs(self):
        print('testIs用例开始执行')
        self.assertIs(10, int(10), '都是整数1')
        self.assertIsNot('s', str('s'), '都是字符串')


if __name__ == '__main__':
    unittest.main()
