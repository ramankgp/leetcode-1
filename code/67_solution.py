#  1010
#  1011
#  0100
# 10000
#+-----
# 10101

# ^ gives the remainder
# & gives the unshifted carry
# << 1 get the correct carry

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = int(a, 2), int(b, 2)
        while b:
            a, b = a ^ b, (a & b) << 1
        return bin(a)[2:]

# from itertools import zip_longest
# from collections import deque

# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         carry = 0
#         result = deque()
#         for ca, cb in zip_longest(reversed(a), reversed(b), fillvalue='0'):
#             carry, remainder = divmod(int(ca) + int(cb) + carry, 2)
#             result.appendleft(remainder)
#         if carry:
#             result.appendleft(carry)
#         return ''.join(map(str, result))