# lcs(t1, t2) = lcs(t1[:l1], t2[:l2])
#             = if t1[l1] == t2[l2]: lcs(t1[:l1-1], t2[:l2-1]) + 1 
#               else: max(lcs(t1[:l1], t2[:l2-1]), lcs(t1[:l1-1], t2[:l2]))

# base case: lcs(t1[:0), t2[:0)) = 0

class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        t2, t1 = sorted((t1, t2), key=len)
        l1, l2 = len(t1), len(t2)
        # @functools.lru_cache(maxsize=None)
        # def lcs(i, j):
        #     if i < 0 or j < 0: return 0  # basecase 
        #     if t1[i] == t2[j]: return lcs(i-1, j-1) + 1
        #     else: return max(lcs(i, j-1), lcs(i-1, j))
        # return lcs(l1-1, l2-1)
        
        # dp = [[0] * (l2 + 1) for _ in range(l1+1)]
        # for i in range(1, l1+1):
        #     for j in range(1, l2+1):
        #         if t1[i-1] == t2[j-1]: dp[i][j] = 1 + dp[i-1][j-1]
        #         else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        # return dp[-1][-1]
        
        dp = [0] * (l2 + 1)
        for i in range(1, l1+1):
            ndp = [0] * (l2 + 1)
            for j in range(1, l2+1):
                if t1[i-1] == t2[j-1]: ndp[j] = 1 + dp[j-1]
                else: ndp[j] = max(ndp[j-1], dp[j])
            dp = ndp
        return dp[-1]    
        