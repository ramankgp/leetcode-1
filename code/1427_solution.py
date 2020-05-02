# s = abcd, length 4
# 0,1 abcd -> bcda
# 1,3 abcd -> dabc->cdab->bcda
# 1,4 abcd -> dabc->cdab->bcda->abcd
# 1,7 = 1,3 
class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        rshift = 0
        l = len(s)
        for d, amt in shift:
            if d: rshift += amt % l
            else: rshift += -amt % l
        rshift %= l
        return s[-rshift:] + s[:-rshift]