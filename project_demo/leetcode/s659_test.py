import unittest
from typing import List

from s659 import Solution


class Solution659Test(unittest.TestCase):
    def __init__(self, methodname: str, p1: List[int], s: bool):
        super().__init__(methodname)
        self.param1 = p1
        self.result = s

    def setUp(self) -> None:
        self.s = Solution()

    def test_reversePairs(self):
        self.assertEqual(self.s.isPossible(self.param1), self.result)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    QAMap = [
        {"param1": [1, 2, 3, 3, 4, 5], "answer": True},
        {"param1": [1, 2, 3, 3, 4, 4, 5, 5], "answer": True},
        {"param1": [1, 2, 3, 4, 4, 5], "answer": False},
    ]
    # 测试次数及需要测试的模块
    for i in QAMap:
        suite.addTest(Solution659Test('test_reversePairs', p1=i.get("param1"), s=i.get("answer")))
    unittest.TextTestRunner().run(suite)
