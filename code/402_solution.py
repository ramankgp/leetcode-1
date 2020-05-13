# 10200
# ^

# 12345
#     ^
    
# 54321
# ^

# 15426
#   

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
#         def remove_one_digit(num):
#             l = 1
#             while l < len(num) and num[l-1] <= num[l]: l += 1
#             return num[:l-1] + num[l:]
        
#         for _ in range(k): num = remove_one_digit(num)

        stack = []
        for digit in num:
            while stack and k and stack[-1] > digit:
                k -= 1
                stack.pop()
            stack.append(digit)
        
        if k: stack = stack[:-k]
        num = ''.join(stack)            
        l = 0
        while l < len(num) and num[l] == '0': l += 1
        return num[l:] if num[l:] else '0'
