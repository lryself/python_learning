import unittest
from typing import List

from s135 import Solution


class SolutionTest(unittest.TestCase):
    def __init__(self, methodname: str, p1, s):
        super().__init__(methodname)
        self.param1 = p1
        self.result = s

    def setUp(self) -> None:
        self.s = Solution()

    def test_func(self):
        self.assertEqual(self.s.candy(self.param1), self.result)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    QAMap = [
        {"param1": [1, 3, 4, 5, 2], "answer": 11},
        {"param1": [1, 6, 10, 8, 7, 3, 2], "answer": 18},
        {"param1": [1, 2, 87, 87, 87, 2, 1], "answer": 13},
        {"param1": [1, 0, 2], "answer": 5},
        {"param1": [1, 2, 2], "answer": 4},
        {"param1": [1, 3, 2, 2, 1], "answer": 7},
    ]
    # 测试次数及需要测试的模块
    for i in QAMap:
        suite.addTest(SolutionTest('test_func', p1=i.get("param1"), s=i.get("answer")))
    unittest.TextTestRunner().run(suite)
