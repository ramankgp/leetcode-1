# 5| 3 3 
# 4| 2 3 2
# 3| 3 2 3 2   /
# 2| 2 1 4 3 /
# 1| 3 2 1 / 
# 0| 0 3 /   
#  --------------
#    0 1 2 3
    
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = sorted(map(abs, (x, y)))
        memo = {(0,0):0, (1,1):2, (1,0):3, (0,1):3}
        def dfs(x, y):
            if (x,y) not in memo:
                memo[(x,y)] = min(dfs(abs(x-1),abs(y-2)), dfs(abs(x-2),abs(y-1))) + 1
            return memo[(x,y)]
        return dfs(x, y)
        
        