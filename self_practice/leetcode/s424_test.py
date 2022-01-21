import unittest

from s424 import Solution


class SolutionTest(unittest.TestCase):
    def __init__(self, methodname: str, p1, p2, s):
        super().__init__(methodname)
        self.param1 = p1
        self.param2 = p2
        self.result = s

    def setUp(self) -> None:
        self.s = Solution()

    def test_func(self):
        self.assertEqual(self.s.characterReplacement(self.param1, self.param2), self.result)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    QAMap = [
        {"param1": "ABAB", "param2": 2, "answer": 4},
        {"param1": "AABABBA", "param2": 1, "answer": 4},
    ]
    # 测试次数及需要测试的模块
    for i in QAMap:
        suite.addTest(SolutionTest('test_func', p1=i.get("param1"), p2=i.get("param2"), s=i.get("answer")))
    unittest.TextTestRunner().run(suite)
