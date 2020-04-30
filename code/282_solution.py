# 4 choices at N-1 locations -> total possibilities 4^(N-1)
# O(N) to evaluate one possibility
# Time O(N*4^(N-1))

# handle 00 in code when cancatenate

# dfs search O(N) space

# "5-3+4+5*2*3"
# init total = 5 = eval(expr[:i])
#     - total += -3 -> 2
#     + total += 4  -> 6
#     + total += 5  -> 11
#     * total = total - 5 + 5 * 2 -> 16
#     * total = total - 5 * 2 + 5 * 2 * 3 -> 36
# remember the previous addition

# 5-3+4+523
#       ^
#       i
        
# for j in range(i+1, n+1):
#     s = num[i:j]
    

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        solutions = []
        
        def dfs(candidate, i, total, prev_add):
            if i == len(num) and total == target: return solutions.append(candidate)
            for j in range(i+1, len(num)+1):
                s = num[i:j]
                d = int(s)
                if num[i] == '0' and s != '0': continue
                if not candidate:
                    dfs(s, j, d, d)
                else:
                    dfs(candidate + '+' + s, j, total + d,  d)
                    dfs(candidate + '-' + s, j, total - d, -d)
                    dfs(candidate + '*' + s, j, total - prev_add + prev_add * d, prev_add*d)            
        dfs('',0,0,0)
        return solutions