import unittest
from typing import List

from s649 import Solution


class SolutionTest(unittest.TestCase):
    def __init__(self, methodname: str, p1: str, s: str):
        super().__init__(methodname)
        self.param1 = p1
        self.result = s

    def setUp(self) -> None:
        self.s = Solution()

    def test_reversePairs(self):
        self.assertEqual(self.s.predictPartyVictory(self.param1), self.result)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    QAMap = [
        {"param1": "RDRDRDD", "answer": "Radiant"},
        {"param1": "RD", "answer": "Radiant"},
        {"param1": "RDD", "answer": "Dire"},
    ]
    # 测试次数及需要测试的模块
    for i in QAMap:
        suite.addTest(SolutionTest('test_reversePairs', p1=i.get("param1"), s=i.get("answer")))
    unittest.TextTestRunner().run(suite)
