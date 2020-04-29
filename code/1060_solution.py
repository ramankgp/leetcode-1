# [4,7,9,10]
#    |
#    1
# 7 - 4 - 1 == 2

# [4,7,9,10]
#      |
#      2
# 9 - 4 - 2 = 3   num_missing between 0 and i is: nums[i] - nums[0] - i


class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        
        def num_missing(i):
            return nums[i] - nums[0] - i
        
        l, h = 0, len(nums)
        while l < h:
            mid = (l + h) // 2
            if num_missing(mid) < k: 
                l = mid + 1
            else:
                h = mid
        return nums[l - 1] + k - num_missing(l - 1)
