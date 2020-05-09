# f(x) = x^2 - num

# 0 = f(x+h) ~= f(x) + f'(x)*h
# h = - f(x) / f'(x) = - (x^2 - num) / (2*x)
# x_{n+1} = x_n + h_n


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
#         l, h = 1, num
#         while l < h:
#             m = (l + h) // 2
#             if m * m >= num:
#                 h = m
#             else:
#                 l = m + 1
#         return l * l == num
        h = lambda x: - (x ** 2 - num) // (2 * x)
        x = num
        while x * x > num: x += h(x)
        return x * x == num
