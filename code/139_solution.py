#            _catsandog
# can_break  1001100100

# can_break(i) = can we break s[0:i]

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordDict = set(wordDict)
        can_break = [1] + [0] * n

        # O(NKL)
        # for loc in range(n): # O(N) length of s
        #     if not can_break[loc]: continue
        #     for word in wordDict: # O(K) size of word_dict
        #         if s[loc:loc+len(word)] == word:  # O(L) average length of words
        #             can_break[loc+len(word)] = 1
        
        # O(N^3)
        for loc in range(1, n+1): # O(N)
            for last_loc in range(loc): # O(N)
                if not can_break[last_loc]: continue
                if s[last_loc:loc] in wordDict: # O(N)
                    can_break[loc] = True
        return can_break[-1]
