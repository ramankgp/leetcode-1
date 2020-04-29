from itertools import zip_longest
from collections import deque


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        str_to_digit = {val: idx for idx, val in enumerate('0123456789')}
        carry = 0
        result = deque()
        for c1, c2 in zip_longest(reversed(num1), reversed(num2), fillvalue='0'):
            carry, remainder = divmod(str_to_digit[c1] + str_to_digit[c2] + carry, 10)
            result.appendleft(remainder)
        if carry:
            result.appendleft(carry)
        return ''.join(map(str, result))