import unittest
from typing import List

from s767 import Solution


class Solution767Test(unittest.TestCase):
    def __init__(self, methodname: str, p: str, s: str):
        super().__init__(methodname)
        self.param = p
        self.result = s

    def setUp(self) -> None:
        self.s = Solution()

    def test_reversePairs(self):
        self.assertEqual(self.s.reorganizeString(self.param), self.result)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    QAMap = [
        {"param": "tndsewnllhrtwsvxenkscbivijfqnysamckzoyfnapuotmdexzkkrpmppttficzerdndssuveompqkemtbwbodrhwsfpbmkafpwyedpcowruntvymxtyyejqtajkcjakghtdwmuygecjncxzcxezgecrxonnszmqmecgvqqkdagvaaucewelchsmebikscciegzoiamovdojrmmwgbxeygibxxltemfgpogjkhobmhwquizuwvhfaiavsxhiknysdghcawcrphaykyashchyomklvghkyabxatmrkmrfsppfhgrwywtlxebgzmevefcqquvhvgounldxkdzndwybxhtycmlybhaaqvodntsvfhwcuhvuccwcsxelafyzushjhfyklvghpfvknprfouevsxmcuhiiiewcluehpmzrjzffnrptwbuhnyahrbzqvirvmffbxvrmynfcnupnukayjghpusewdwrbkhvjnveuiionefmnfxao", "answer": ""},
        {"param": "aab", "answer": "aba"},
        {"param": "aaab", "answer": ""},

    ]
    # 测试次数及需要测试的模块
    for i in QAMap:
        suite.addTest(Solution767Test('test_reversePairs', p=i.get("param"), s=i.get("answer")))
    unittest.TextTestRunner().run(suite)
