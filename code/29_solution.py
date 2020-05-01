class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN = -2**31
        INT_MAX = 2**30 + (2**30 - 1)

        if dividend == INT_MIN and divisor==-1: return INT_MAX
        if dividend == INT_MIN and divisor==1: return INT_MIN
        
        negative = (dividend < 0) ^ (divisor < 0)
        dividend = -dividend if dividend > 0 else dividend
        divisor = -divisor if divisor > 0 else divisor
        
        quotient, i, accum = 0, 1, divisor
        while accum >= INT_MIN >> 1 and dividend <= accum + accum:
            i <<= 1
            accum += accum
        
        while dividend <= divisor:
            if dividend <= accum:
                dividend -= accum
                quotient += i
            accum >>= 1
            i >>= 1
        return -quotient if negative else quotient
