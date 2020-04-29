#    [1,    2,   3,    4]
#   2x3x4  3x4   4     1        accum_r
#     1     1   1x2  1x2x3      acuum_l
#     24    12   8     6
#          i=1  ~i

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        accum_l = accum_r = 1
        for i in range(n):
            output[i] *= accum_l
            output[~i] *= accum_r
            accum_l *= nums[i]
            accum_r *= nums[~i]
        return output