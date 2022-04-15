import unittest
from typing import List

from s976 import Solution


class Solution493Test(unittest.TestCase):
    def __init__(self, methodName: str, p: List[int], s: int):
        super().__init__(methodName)
        self.param = p
        self.result = s

    def setUp(self) -> None:
        self.s = Solution()

    def test_largestPerimeter(self):
        self.assertEqual(self.s.largestPerimeter(self.param), self.result)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    QAMap = [
        {"param": [3, 6, 2, 3], "answer": 8},
        {"param": [2, 1, 2], "answer": 5},
        {"param": [1, 2, 1], "answer": 0},
        {"param": [3, 2, 3, 4], "answer": 10},
    ]
    # 测试次数及需要测试的模块
    for i in QAMap:
        suite.addTest(Solution493Test('test_largestPerimeter', p=i.get("param"), s=i.get("answer")))
    unittest.TextTestRunner().run(suite)
