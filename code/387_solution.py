class Solution:
    def firstUniqChar(self, s: str) -> int:
        # char_freq = collections.Counter(s)
        # for loc, c in enumerate(s):
        #     if char_freq[c] == 1: return loc
        # return -1
        
        seen = set()
        char_loc = dict()
        for loc, c in enumerate(s):
            if c in seen:
                char_loc.pop(c, -1)
            else:
                seen.add(c)
                char_loc[c] = loc
        return -1 if not char_loc else next(iter(char_loc.values()))