import unittest
from typing import List

from s860 import Solution


class SolutionTest(unittest.TestCase):
    def __init__(self, methodName: str, p: List[int], s: bool):
        super().__init__(methodName)
        self.param = p
        self.result = s

    def setUp(self) -> None:
        self.s = Solution()

    def test_largestPerimeter(self):
        self.assertEqual(self.s.lemonadeChange(self.param), self.result)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    QAMap = [
        {"param": [5, 5, 5, 10, 20], "answer": True},
        {"param": [5, 5, 10], "answer": True},
        {"param": [10, 10], "answer": False},
        {"param": [5, 5, 10, 10, 20], "answer": False},
    ]
    # 测试次数及需要测试的模块
    for i in QAMap:
        suite.addTest(SolutionTest('test_largestPerimeter', p=i.get("param"), s=i.get("answer")))
    unittest.TextTestRunner().run(suite)
