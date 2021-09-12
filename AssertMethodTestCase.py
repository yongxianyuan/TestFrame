import unittest
import logging

logging.basicConfig(level=logging.DEBUG)


class AssertMethodTestCase(unittest.TestCase):

    def testEqual(self):
        logging.debug("testEqual方法被执行")
        self.assertEqual('1', 1, msg='数据类型不同')
        self.assertNotEqual(365, 365, '这两个数字相等')

    def testTrue(self):
        # self.assertTrue(None, '空对象结果')
        self.assertFalse(bool(1), '数字1转为布尔值结果是True')

    def testIs(self):
        self.assertIs(10, int(10), '都是整数1')
        self.assertIsNot('s', str('s'), '都是字符串')

    def testIn(self):
        self.assertIn('s', 'school')
        self.assertNotIn(1, (1, 2, 3))

    def testIsInstance(self):
        self.assertIsInstance('hello', str, '这不是一个str的实例')
        self.assertNotIsInstance(10, int, '这是一个整数的')

    def testMultiLineEqual(self):
        a = '''
        line1
        line2
        line3
        '''
        b = """
        line1
        line2
        line3
        """
        self.assertMultiLineEqual(a, b, '这两个多行字符串不相等')

    def testListEqual(self):
        x = [1, 2, 3]
        y = [(1, 2, 3)]
        self.assertListEqual(x, y, '这两个列表不一样')

    def test_split(self):
        s = 'hello world'
        # self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

        # try:
        #     s.split(2)
        #     self.assertRaises(TypeError)
        # except Exception as e:
        #     print(e)
        print('test_split测试结束')


if __name__ == '__main__':
    unittest.main()
