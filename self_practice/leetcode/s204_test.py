import unittest
from typing import List

from s204 import Solution


class Solution204Test(unittest.TestCase):
    def __init__(self, methodname: str, p1: int, s: int):
        super().__init__(methodname)
        self.param1 = p1
        self.result = s

    def setUp(self) -> None:
        self.s = Solution()

    def test_reversePairs(self):
        self.assertEqual(self.s.countPrimes(self.param1), self.result)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    QAMap = [
        {"param1": 10000, "answer": 1229},
        {"param1": 10, "answer": 4},
        {"param1": 0, "answer": 0},
        {"param1": 1, "answer": 0},
    ]
    # 测试次数及需要测试的模块
    for i in QAMap:
        suite.addTest(Solution204Test('test_reversePairs', p1=i.get("param1"), s=i.get("answer")))
    unittest.TextTestRunner().run(suite)
