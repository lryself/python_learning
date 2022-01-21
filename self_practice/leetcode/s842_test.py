import unittest
from typing import List

from s842 import Solution


class Solution842Test(unittest.TestCase):
    def __init__(self, methodName: str, p: str, s: List[int]):
        super().__init__(methodName)
        self.param = p
        self.result = s

    def setUp(self) -> None:
        self.s = Solution()

    def test_splitIntoFibonacci(self):
        self.assertEqual(self.s.splitIntoFibonacci(self.param), self.result)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    QAMap = [
        {"param": "17522", "answer": [17, 5, 22]},
        {"param": "539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511", "answer": []},
        {"param": "1101111", "answer": [11,0,11,11]},
        {"param": "123456579", "answer": [123, 456, 579]},
        {"param": "11235813", "answer": [1, 1, 2, 3, 5, 8, 13]},
        {"param": "112358130", "answer": []},
        {"param": "0123", "answer": []},
    ]
    # 测试次数及需要测试的模块
    for i in QAMap:
        suite.addTest(Solution842Test('test_splitIntoFibonacci', p=i.get("param"), s=i.get("answer")))
    unittest.TextTestRunner().run(suite)
