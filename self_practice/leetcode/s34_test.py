import unittest
from typing import List

from s34 import Solution


class Solution34Test(unittest.TestCase):
    def __init__(self, methodname: str, p1: List[int], p2: int, s: int):
        super().__init__(methodname)
        self.param1 = p1
        self.param2 = p2
        self.result = s

    def setUp(self) -> None:
        self.s = Solution()

    def test_reversePairs(self):
        self.assertEqual(self.s.searchRange(self.param1, self.param2), self.result)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    QAMap = [
        {"param1": [5, 7, 7, 8, 8, 10], "param2": 8, "answer": [3, 4]},
        {"param1": [5, 7, 7, 8, 8, 10], "param2": 6, "answer": [-1, -1]},
        {"param1": [], "param2": 0, "answer": [-1, -1]},
    ]
    # 测试次数及需要测试的模块
    for i in QAMap:
        suite.addTest(Solution34Test('test_reversePairs', p1=i.get("param1"), p2=i.get("param2"), s=i.get("answer")))
    unittest.TextTestRunner().run(suite)
