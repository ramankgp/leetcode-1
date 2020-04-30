#  1 
#  1 * 1/2 , 1/2
#  1/2 * 2/3 = 1/3, 1/2 * 2/3 = 1/3, 1/3

class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        ret = None
        cnt = 0
        for idx, num in enumerate(self.nums):
            if num == target:
                if random.randint(0, cnt) == cnt:
                    ret = idx
                cnt += 1
        return ret

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)