import unittest
from ddt import *

test_data1 = ("hello", 123, True, False)

test_data2 = ((1, 2, 3, 4),
              (11, 22, 33, 44),
              (111, 222, 333, 444),
              (1111, 2222, 3333, 4444))


@ddt
class TestDDTCase(unittest.TestCase):

    @data(*test_data1)
    # @unpack
    def test_case01(self, value):
        print(f'本次测试的value是{value}')
        # self.assertTrue(value)

    @data(*test_data2)
    @unpack
    def test_case02(self, a, b, c, d):
        print(f'参数1是{a},参数2是{b},参数3是{c},参数4是{d}')

    @file_data('test.json')
    def test_case03(self, a, b, c):
        print(f'参数1是{a},参数2是{b},参数3是{c}')

    @file_data('test.yml')
    def test_case04(self, name, age, address):
        print(f'姓名{name},年龄:{age},地址：{address}')


if __name__ == '__main__':
    unittest.main()
