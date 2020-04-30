# m = 5 101 >> 1 = 10 >> 1 = 1  << 2 -> 100
#     6 110 >> 1 = 11 >> 1 = 1
# n = 7 111 >> 1 = 11 >> 1 = 1
# -----------------------------
#       100 = 4    
    
# m = 2  010 >> 1 = 01 >> 2 = 0 << 3 -> 0 
#     3  011
#     4  100
#     5  101
# n = 6  110 >> 1 = 11 >> 2 = 0

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        # return functools.reduce(operator.__and__, range(m,n), n)
        shift = 0
        while m != n:
            m >>= 1
            n >>= 1
            shift += 1
        return m << shift