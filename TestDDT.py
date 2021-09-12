import unittest

import ddt as ddt

testData = [{'a': 11}, {'b': 22}, {'c': 33}]
myList = ['苹果', '梨子', '香蕉', '橘子']
myDicts = {'name': 'wing', 'age': 30, 'code': 1001}, {'name': 'Ghassan', 'age': 28, 'code': 1004}


@ddt.ddt
class CalculatorTestCase(unittest.TestCase):

    @classmethod
    def setUp(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    @unittest.skip('skip2')
    @ddt.data(*testData)
    def testData(self, data):
        # print(data.key(), data.value())
        for k, v in data.items():
            print(k, v)
        self.assertTrue(True)

    @unittest.skip('skip')
    @ddt.data(*myList)
    def testList(self, lst):
        print(lst)

    @ddt.file_data('test.json')
    def testFile(self, a, b, c):
        print(a, b, c)

    @ddt.file_data('test.yml')
    def testYml(self, name, age, address):
        print(name, age, address)

    @ddt.data(*myDicts)
    @ddt.unpack
    def testDict(self, name, age, code):
        print(name, age, code)


if __name__ == '__main__':
    unittest.main()
    # testData = [{'a': 11}, {'b': 22}, {'c': 33}]
    # d = {'b': 22}
