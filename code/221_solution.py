# f(r,c) = max length for the squares with bottom right location at (r, c)

# f(r,c) = 2 
#         c
#   1 0 1 0 0
#   1 0 1 1 1
# r 1 1 1 1 1
#   1 0 0 1 0
    
# f(r,c) ~ min(f(r-1,c-1), f(r-1,c), f(r,c-1)) + 1

# f(r-1,c-1) = 3
#           c
#     0 1 0 0
#   1 1 1 1 0
#   1 1 1 1 1
#   1 1 1 1 1
# r 1 0 0 1 ?


#      c
#     x
# r    ? 
    
# basecae: for r = 0 or c = 0, f(r,c) = matrix[r,c]
    
# maximalSquare(matrix) = max(f(r,c) for r, c in nrows, ncols)^2

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]: return 0
        max_len = 0
        nr, nc = len(matrix), len(matrix[0])
        # dp = [[0] * nc for _ in range(nr)]
        dp = [0] * nc
        for r in range(nr):
            ndp = [0] * nc
            for c in range(nc):
                if matrix[r][c] == '0': continue
                if r == 0 or c == 0: 
                    # dp[r][c] = 1
                    ndp[c] = 1
                else: 
                    # dp[r][c] = min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1]) + 1
                    ndp[c] = min(dp[c], ndp[c-1], dp[c-1]) + 1
                max_len = max(max_len, ndp[c])
            dp = ndp
        return max_len**2
        
        