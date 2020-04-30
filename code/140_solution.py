# previous: dp(i) = can we break s[0:i]
# now:      dp(i) = ways we can break s[0:i]

# Time O(2^(N-1))
# Space O(N*2^(N-1))


# s = "aaaa"
# wd = ["a", "aa", "aaa", "aaaa"]
# dp[4] = ["a a a a",
#  "a a aa",
#  "a aa a",
#  "a aaa",
#  "aa a a",
#  "aa aa",
#  "aaa a",
#  "aaaa"
# ]
# s = "aaaab"

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        wordDict = set(wordDict)
        
        # O(N^3)
        dp = [1] + [0] * n
        for loc in range(1, n+1): # O(N)
            for last_loc in range(loc): # O(N)
                if not dp[last_loc]: continue
                if s[last_loc:loc] in wordDict: # O(N)
                    dp[loc] = True
        # return dp[-1]
        if not dp[-1]: return []

        dp = collections.defaultdict(list)
        dp[0] = [""]
        for loc in range(1, n+1): # O(N)
            for last_loc in range(loc): # O(N)
                if not dp[last_loc]: continue
                word = s[last_loc:loc]
                if word in wordDict: # O(N)
                    dp[loc].extend([c + " " + word if c else word
                                    for c in dp[last_loc]])
        print(len(dp[n]))
        return dp[n]
                