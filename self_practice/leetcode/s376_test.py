import unittest

from s376 import Solution


class SolutionTest(unittest.TestCase):
    def __init__(self, methodname: str, p, s):
        super().__init__(methodname)
        self.param = p
        self.result = s

    def setUp(self) -> None:
        self.s = Solution()

    def test_func(self):
        self.assertEqual(self.s.wiggleMaxLength(self.param), self.result)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    QAMap = [
        {"param": [3, 3, 3, 2, 5], "answer": 3},
        {"param": [0, 0], "answer": 1},
        {"param": [1, 7, 4, 9, 2, 5], "answer": 6},
        {"param": [1, 17, 5, 10, 13, 15, 10, 5, 16, 8], "answer": 7},
        {"param": [1, 2, 3, 4, 5, 6, 7, 8, 9], "answer": 2},

    ]
    # 测试次数及需要测试的模块
    for i in QAMap:
        suite.addTest(SolutionTest('test_func', p=i.get("param"), s=i.get("answer")))
    unittest.TextTestRunner().run(suite)
