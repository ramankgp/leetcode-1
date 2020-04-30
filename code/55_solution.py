#  [3,2,2,0,4]
#   ^     ^
#   i=0   m    
# m = i + nums[i] = 0 + 3 = 3

#  [3,2,2,0,4]
#     ^   ^
#     i=1 m
# i < m
# m = max(m, i+nums[i] == 3) = 3

#  [3,2,2,  0,4]
#       ^   ^
#       i=2 m
# i=2 < m =3
# m = max(m, i+nums[i] == 4) = 4

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m = nums[0]        
        for i, step in enumerate(nums):
            if i <= m: # reachable
                m = max(m, i + step)
            else: # non reachable
                return False
            if m >= len(nums) - 1: return True
        return True